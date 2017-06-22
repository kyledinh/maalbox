#! /bin/sh

# run the servers: database and webserver
sudo ~/code/bin/start_mongo.sh > ~/mongo.log 2>&1 &
sudo ~/code/maalserver.py > ~/maalserver.log 2>&1 &
