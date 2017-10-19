#!/usr/bin/env python3

import smtplib
import email.utils
from email.mime.text import MIMEText

print("In script")
# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'kroooooo@test.com'))
msg['From'] = email.utils.formataddr(('Author', 'sender@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('localhost')
server.set_debuglevel(True) # show communication with the server
print("smtp server.....")

try:
    server.sendmail('jack@testing.com', ['davis@dinhoo.com'], msg.as_string())
    print("sending......")
finally:
    server.quit()
