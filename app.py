import smtplib

username = ""
password = ""

email = """From: 
To: example@example.com
Subject: Example subject

Our body text goes here
"""

server = smtplib.SMTP_SSL("smtp.gmail.com")
server.login(username, password)
server.sendmail(username, "example@example.com", email)
server.close()
