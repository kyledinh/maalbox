#!/bin/bash
docker container rm $(docker container ls -a -q)
docker image rm maalbox-img
