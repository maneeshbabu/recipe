FROM python:3.8-alpine

LABEL author="Maneesh Babu M"

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

RUN mkdir /app
WORKDIR /app

COPY Pipfile .
RUN pipenv install

COPY ./app /app

RUN adduser -D user
USER user

