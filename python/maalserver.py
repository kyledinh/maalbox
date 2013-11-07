#!/usr/bin/env python3

import asyncore
import datetime
import smtpd
import threading
import time

from flask import Flask, render_template
from pymongo import MongoClient

# MongoDB
mgo_client = MongoClient('localhost', 27017)
maal_db = mgo_client['maal-database']

class CustomSMTPServer(smtpd.SMTPServer):
    
   def process_message(self, peer, mailfrom, rcpttos, data):
      print('Receiving message from:', peer)
      print('Message addressed from:', mailfrom)
      print('Message addressed to  :', rcpttos)
      print('Message length        :', len(data))
      
      email = { "from": mailfrom,
                "to": rcpttos[0],
                "data": data,
                "date": datetime.datetime.utcnow() }

      emails = maal_db.emails
      eid = emails.insert(email)
      print('Inserted into db:', eid)
      return

# Database Cleanup
def cleanup_db(count, name):
   while count > 0:
      print(name, " cleaning the db", count)
      count -= 1
      time.sleep(10)
   print("cleanup_db has ended!")


def getEmails():
   emails = maal_db.emails
   return emails.find()


# Flask Webserver
flaskapp = Flask(__name__)

@flaskapp.route("/")
def hello():
   return render_template("home.html")

@flaskapp.route("/about")
def about():
   return render_template("about.html")

@flaskapp.route("/all")
def all():
   print("AAAAA")
   mails = getEmails()
   msg = "GORMDO"
   print("BBBBB")
   return render_template("all.html", msg=msg, emails=mails)

if __name__ == "__main__":
   
   #smtpd runs via asyncore
   smtpServer = CustomSMTPServer(('127.0.0.1', 25), None) 
   loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
   loop_thread.start()
  
   cleanup_thread = threading.Thread(target=cleanup_db, args=(10, "Algo", ))
   cleanup_thread.start()

   #start the wbserver
   flaskapp.run()  

   #Not executed
   loop_thread.join()
   cleanup_thread.join()
   print("shutdown")
