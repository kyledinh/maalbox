#!/usr/bin/env python3

import asyncore
import smtpd
import threading
import time

from flask import Flask

class CustomSMTPServer(smtpd.SMTPServer):
    
   def process_message(self, peer, mailfrom, rcpttos, data):
      print('Receiving message from:', peer)
      print('Message addressed from:', mailfrom)
      print('Message addressed to  :', rcpttos)
      print('Message length        :', len(data))
      return

# Flask Webserver
flaskapp = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"


if __name__ == "__main__":
   
   #smtpd runs via asyncore
   smtpServer = CustomSMTPServer(('127.0.0.1', 25), None) 
   loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
   loop_thread.start()
  
   #start the wbserver
   flaskapp.run()  
   print("other stuff")


