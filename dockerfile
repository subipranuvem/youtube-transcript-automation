FROM python:3.11-slim-buster

ARG PORT=8000

WORKDIR /api

COPY ./ /api

# Install poetry
RUN pip install "poetry==2.1.1"

RUN poetry install

ENTRYPOINT ["poetry", "run"]
CMD ["fastapi", "run", "app.py", "--port", "8001"]