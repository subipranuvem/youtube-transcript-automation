import os
import re
from http import HTTPStatus
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field, model_validator
from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    YouTubeTranscriptApi,
)
from youtube_transcript_api.formatters import TextFormatter

app = FastAPI()


class VideoID(BaseModel):
    video_id: Optional[str] = None
    video_url: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def extract_video_id(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        video_id: Optional[str] = values.get("video_id")
        video_url: Optional[str] = values.get("video_url")

        if not video_id and video_url:
            pattern: str = (
                r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
            )
            match: Optional[re.Match] = re.search(pattern, video_url)
            if match:
                values["video_id"] = match.group(1)
            else:
                raise ValueError("Invalid YouTube video URL format")
        elif not video_id:
            raise ValueError("A valid YouTube video ID or URL must be provided")

        return values


class TranscriptResponse(BaseModel):
    transcription: str = Field(
        description="Transcription of the video", examples=["Hello everyone ..."]
    )
    language: str = Field(
        description="Language of the transcription", examples=["English"]
    )
    language_code: str = Field(
        description="Language code of the transcription",
        examples=["en"],
    )
    is_generated: bool = Field(
        description="Whether the transcription is auto-generated or manually created",
        examples=[True],
    )


@app.get(
    "/youtube/transcript",
    response_model=TranscriptResponse,
    response_description="Get a YouTube video transcription",
    responses={
        HTTPStatus.NOT_FOUND: {
            "description": "Transcript not found for this video",
            "content": {"application/json": {"example": {"detail": "Not Found"}}},
        },
        HTTPStatus.INTERNAL_SERVER_ERROR: {
            "description": "An error occurred while fetching the transcript",
            "content": {
                "application/json": {"example": {"detail": "Internal Server Error"}}
            },
        },
        HTTPStatus.BAD_REQUEST: {
            "description": "Invalid YouTube video ID or URL format",
            "content": {"application/json": {"example": {"detail": "Bad Request"}}},
        },
    },
    status_code=HTTPStatus.OK,
    tags=["YouTube"],
    operation_id="get_transcript",
    summary="Get a YouTube video transcription",
    description="Get a YouTube video transcription given a video ID or URL",
)
async def get_transcript(
    video_id: Optional[str] = Query(None, description="YouTube video ID"),
    video_url: Optional[str] = Query(None, description="YouTube video URL"),
    preferred_languages: Optional[List[str]] = Query(
        ["en"],
        description="Preferred language for transcript",
    ),
) -> TranscriptResponse:
    video: VideoID = VideoID(video_id=video_id, video_url=video_url)
    try:
        # Get transcript list
        transcript_list = YouTubeTranscriptApi.list_transcripts(video.video_id)

        generated_transcripts: List[str] = list(
            dict.keys(transcript_list._generated_transcripts)
        )
        manually_created_transcripts: List[str] = list(
            dict.keys(transcript_list._manually_created_transcripts)
        )

        preferred_languages_available: List[str] = list(
            set(
                preferred_languages
                + generated_transcripts
                + manually_created_transcripts,
            )
        )

        # Try to find generated transcript in preferred language
        transcript = transcript_list.find_transcript(preferred_languages_available)

        # Format transcript
        formatter: TextFormatter = TextFormatter()
        transcript_text: str = formatter.format_transcript(transcript.fetch())

        # Clean transcript
        transcript_text = re.sub(r"\[\d+:\d+:\d+\]", "", transcript_text)
        transcript_text = re.sub(r"<\w+>", "", transcript_text)

        return TranscriptResponse(
            transcription=transcript_text,
            language=transcript.language.replace("(auto-generated)", ""),
            language_code=transcript.language_code,
            is_generated=transcript.is_generated,
        )

    except (NoTranscriptFound, TranscriptsDisabled):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Transcript not found for this video",
        )
    except ValueError as e:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
