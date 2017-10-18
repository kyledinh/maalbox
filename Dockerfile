FROM ubuntu:16.04

RUN mkdir -p /app/tmp && mkdir -p /data/db && cd /app/tmp

COPY python/maalserver.py /app/.
COPY python/readme.md /app/.
COPY python/static/ /app/static
