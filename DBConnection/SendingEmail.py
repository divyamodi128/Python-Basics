import smtplib

sender = 'modidivya16@gamil.com'
receivers = ['pranavdave893@gmail.com']

message = """From: From Person <modidivya16@gamil.com>
To: To Person <pranavdave893@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"