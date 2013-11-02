#!/usr/bin/env python3

from datetime import datetime
import asyncore
from smtpd import SMTPServer

class EmlServer(SMTPServer):
   no = 0
   def process_message(self, peer, mailfrom, rcpttos, data):
      print('From %s ' % mailfrom)
      filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'), self.no)
      f = open(filename, 'w')
      f.write(data)
      f.close()
      print('%s saved.' % filename)
      self.no += 1

def run():
   print('Python SMTP server')
   print('Quit the server with CONTROL-C.')
   maalserver = EmlServer(('127.0.0.1', 1025), None)
   try:
      asyncore.loop()
   except KeyboardInterrupt:
      pass

if __name__ == '__main__':
   run()


