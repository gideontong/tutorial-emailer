import email.mime.multipart
import json
import smtplib
import time

recipients = open('contacts.txt').readlines()
secrets = json.load(open('secrets.json'))

server = smtplib.SMTP_SSL('smtp.gmail.com')
server.login(secrets['username'], secrets['password'])

for recipient in recipients:
    recipient = recipient.strip()

    message = email.mime.multipart.MIMEMultipart()
    message['Subject'] = 'Lab positions'
    message['From'] = secrets['username']
    message['To'] = recipient
    
    server.sendmail(secrets['username'], recipient, message.as_string())
    print(f'Succecssfully sent email to {recipient}')

    time.sleep(15)

server.close()
