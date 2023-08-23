FROM python:3.11.4-bookworm AS prod

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get install -y pipenv \
    && rm -rf /var/lib/apt/lists/*

COPY Pipfile* /app/

RUN pipenv install --system --deploy

COPY . /app/


# Development image used by engineers on the local environment.
FROM prod as dev

RUN pipenv install --system --deploy --dev
