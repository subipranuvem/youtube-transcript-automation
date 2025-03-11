FROM python:3.11-slim-buster

WORKDIR /api

COPY ./ /api

# Install poetry
RUN pip install "poetry==2.1.1"

RUN poetry install

CMD ["poetry", "run", "python", "app.py"]