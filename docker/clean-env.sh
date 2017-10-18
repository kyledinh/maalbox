#!/bin/bash
docker image rm maalbox-img -f
docker container rm $(docker container ls -a -q)
