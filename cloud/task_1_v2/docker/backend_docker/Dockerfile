FROM python:3.8-slim

WORKDIR /src
COPY ./src .

COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir

CMD gunicorn app:app -c gunicorn_config.py
