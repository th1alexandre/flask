FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

ENV PYTHONPATH=$(pwd)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 5000

VOLUME /app/src
VOLUME /app/test

ENTRYPOINT python -u src/main.py
