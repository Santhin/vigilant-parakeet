FROM python:3.8-slim

WORKDIR /src
COPY ./starcraft .

COPY ./docker/pgsync_docker/wait-for-it.sh wait-for-it.sh
COPY ./docker/pgsync_docker/runserver.sh runserver.sh

RUN pip install pgsync

RUN chmod +x wait-for-it.sh
RUN chmod +x runserver.sh
