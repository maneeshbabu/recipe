FROM python:3.8-alpine

LABEL author="Maneesh Babu M"

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

RUN mkdir /app
WORKDIR /app

COPY . /app
RUN pipenv install


RUN adduser -D user
USER user

