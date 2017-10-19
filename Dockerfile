FROM ubuntu:17.04

RUN mkdir /app && mkdir /data && mkdir /data/db \
&& apt-get update \
&& apt-get -y install python3-pip \
&& apt-get -y install mongodb \
&& pip3 install Flask \
&& pip3 install pymongo \
&& apt-get -y install net-tools \
&& apt-get -y install vim 

COPY python/maalserver.py /app/.
COPY python/container_init.sh /app/.
COPY python/readme.md /app/.
COPY python/static/ /app/static
COPY python/templates/ /app/templates

EXPOSE 25

CMD ["/app/container_init.sh"]
