#!/usr/bin/env python3

import asyncore
import datetime
import smtpd
import threading
import time

from flask import Flask, render_template
from pymongo import MongoClient

# Global and configs
SMTP_IP = "127.0.0.1"
SMTP_PORT = 25
FLASK_SERVER = "localhost:5000"
MONGO_DB = "maal-database"
MONGO_SERVER = "localhost"

mongo_client = MongoClient(MONGO_SERVER, 27017)
mongo_db = mongo_client[MONGO_DB]

flaskapp = Flask(__name__)
flaskapp.config.update(
   SERVER_NAME=FLASK_SERVER,
   DEBUG=False
)

class CustomSMTPServer(smtpd.SMTPServer):
    
   def process_message(self, peer, mailfrom, rcpttos, data):
      print("Receiving message from:", peer)
      print("Message addressed from:", mailfrom)
      print("Message addressed to  :", rcpttos)
      print("Message length        :", len(data))
      
      email = { "from": mailfrom,
                "to": rcpttos[0],
                "data": data,
                "date": datetime.datetime.utcnow() }

      emails = mongo_db.emails
      eid = emails.insert(email)
      print("Inserted into db:", eid)
      return

# Database Cleanup
def cleanup_db(cutoff, name):
   while True:
      print(name, " for emails older than ", cutoff, " minutes.")
      time.sleep(300) # 300 = 5 minutes
      emails = mongo_db.emails
      time_ago = datetime.datetime.utcnow() - datetime.timedelta(minutes=cutoff)
      found = emails.find({"date" : { "$lt" : time_ago }}).count()
      print("Found ", found, " past cutoff, set to be removed.")
      if found > 0:
         emails.remove({"date" : { "$lt" : time_ago }})
         print("Deleted ", found, " emails.")

def getEmails():
   emails = mongo_db.emails
   return emails.find()

def findEmails():
   emails = mongo_db.emails
   return emails.find_one({})

def getOldEmails():
   emails = mongo_db.emails
   time_10minago = datetime.datetime.utcnow() - datetime.timedelta(minutes=10)
   return emails.find({"date" : { "$lt" : time_10minago }})


# Flask Webserver Routing
@flaskapp.route("/")
def hello():
   return render_template("home.html")

@flaskapp.route("/mail/<username>")
def mail(username):
   mails = findEmails(username)
   msg = username 
   return render_template("all.html", msg=msg, emails=mails)

@flaskapp.route("/about")
def about():
   return render_template("about.html")

@flaskapp.route("/all")
def all():
   mails = getEmails()
   msg = "ALL"
   return render_template("all.html", msg=msg, emails=mails)

@flaskapp.route("/old")
def old():
   mails = getOldEmails()
   msg = "OLD Messsages"
   return render_template("all.html", msg=msg, emails=mails)

if __name__ == "__main__":
   
   # smtpd runs via asyncore
   smtpServer = CustomSMTPServer((SMTP_IP, SMTP_PORT), None) 
   smtp_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
   cleanup_thread = threading.Thread(target=cleanup_db, args=(60, "DB Cleanup Thread", ))

   # start the wbserver and threads
   try:
      smtp_thread.start()
      cleanup_thread.start()     
      flaskapp.run(host='0.0.0.0') 

   except KeyboardInterrupt:
      print("attempting to close threads...")
      smtp_thread.join()
      cleanup_thread.join()
      flaskapp.join()
      print("threads successfully closed")   
