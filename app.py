import json
import smtplib
import time

recipients = open("contacts.txt").readlines()
secrets = json.load(open("secrets.json"))

server = smtplib.SMTP_SSL("smtp.gmail.com")
server.login(secrets["username"], secrets["password"])

for recipient in recipients:
    recipient = recipient.strip()

    email = f"""From: {secrets["username"]}
    To: {recipient}
    Subject: Test email

    Hello world from our first email!
    """

    # server.sendmail(secrets["username"], recipient, email)
    print(f"Succecssfully sent email to {recipient}")

    time.sleep(15)

server.close()
