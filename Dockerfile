FROM python:3.6.10-slim-stretch
MAINTAINER Md. Mohaymenul Islam

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
