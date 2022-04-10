FROM python:3.8-slim

LABEL maintainer="juancarvajaling@gmail.com"

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

COPY . /habiapp

RUN pip install --upgrade pip && \
    pip install -r /habiapp/requirements.txt

WORKDIR /habiapp
