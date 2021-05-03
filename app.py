from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import smtplib
import time

recipients = open('contacts.txt').readlines()
secrets = json.load(open('secrets.json'))

server = smtplib.SMTP_SSL('smtp.gmail.com')
server.login(secrets['username'], secrets['password'])

resume = open('resume.pdf', 'rb')
attachment = resume.read()

for recipient in recipients:
    recipient = recipient.strip()

    message = MIMEMultipart()
    message['Subject'] = 'Lab positions'
    message['From'] = secrets['username']
    message['To'] = recipient

    body = """
    To whom it may concern,

    I'm interested in working in your lab this summer
    and I have attached my resume.

    Best,
    Billy Bob Joe
    """

    message.attach(MIMEText(body, 'plain'))

    filename = 'resume.pdf'
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')

    message.attach(part)
    
    server.sendmail(secrets['username'], recipient, message.as_string())
    print(f'Succecssfully sent email to {recipient}')

    time.sleep(15)

server.close()
