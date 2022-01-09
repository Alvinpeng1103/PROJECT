FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /app2
WORKDIR /app2

COPY requirements.txt /app2/
RUN pip install -r requirements.txt

COPY . /app2/
