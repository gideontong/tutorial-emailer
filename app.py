import json
import smtplib
import time

recipients = [
    "person1@example.com",
    "person2@example.com",
    "person3@example.com"
]

secrets = json.load(open("secrets.json"))


server = smtplib.SMTP_SSL("smtp.gmail.com")
server.login(secrets["username"], secrets["password"])
# server.sendmail(secrets["username"], secrets["username"], email)

for recipient in recipients:
    email = f"""From: {secrets["username"]}
    To: {recipient}
    Subject: Test email

    Hello world from our first email!
    """
    
    server.sendmail(secrets["username"], recipient, email)

server.close()
