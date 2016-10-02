import urllib2
import re
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

number=str(123456)
# response = urllib2.urlopen('')
# data = json.load(response)
# for i in range(len(data)):

msg=MIMEMultipart('alternative')
msg['Subject'] = 'Confirmation: Tech-Trek-2016'
msg['From'] = ''
msg['To'] = ''

htmly = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       Here is the token no: {number}  
    </p>
  </body>
</html>
""".format(number=number)


part1 = MIMEText(htmly, 'html')
msg.attach(part1)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("", "")
server.sendmail("", "", msg.as_string())
server.quit()
print "Emails Sent Successfully!"