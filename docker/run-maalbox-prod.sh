#!/bin/bash
docker run -it --rm --expose=25 -p 8000:8000 -p 25:25 --name maalbox-prod-ctnr maalbox-img bash
