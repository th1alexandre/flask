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
