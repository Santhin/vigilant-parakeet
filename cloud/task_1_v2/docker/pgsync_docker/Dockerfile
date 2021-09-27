FROM python:3.7-slim

WORKDIR /src
COPY ./airbnb .


RUN pip install pgsync

COPY ./docker/pgsync_docker/wait-for-it.sh wait-for-it.sh
COPY ./docker/pgsync_docker/runserver.sh runserver.sh

RUN chmod +x wait-for-it.sh
RUN chmod +x runserver.sh