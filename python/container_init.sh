#! /bin/sh

# run the servers: database and webserver
mongod --port 27017 > /app/mongo.log 2>&1 &
/app/maalserver.py > /app/maalserver.log 2>&1 &
