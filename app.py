import json
import smtplib

secrets = json.load("secrets.json")

email = """From: 
To: example@example.com
Subject: Example subject

Our body text goes here
"""

server = smtplib.SMTP_SSL("smtp.gmail.com")
server.login(secrets["username"], secrets["password"])
server.sendmail(secrets["username"], "example@example.com", email)
server.close()
