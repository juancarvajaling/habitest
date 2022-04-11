FROM python:3.8-slim

LABEL maintainer="juancarvajaling@gmail.com"

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

COPY . /habiapi

RUN pip install --upgrade pip && \
    pip install -r /habiapi/requirements.txt

WORKDIR /habiapi
