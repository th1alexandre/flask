## Base stage, set environment variables
FROM python:3.10-slim-bullseye as python-base

# Python envs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random

# Pip envs
ENV PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# Poetry envs
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.2.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_IN_PROJECT=true

# Other envs
ENV PYSETUP_PATH=/opt/pysetup \
    VENV_PATH=/opt/pysetup/.venv \
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


## Building stage, installs poetry and dependencies
FROM python-base as poetry-builder

# Installs essential tools for building poetry
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry, respects $POETRY_VERSION and $POETRY_HOME
RUN curl -sSL https://install.python-poetry.org | python

# Cache requirements and installs only main dependencies
WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --only main
