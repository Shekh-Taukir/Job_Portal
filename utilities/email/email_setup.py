import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
from dotenv import load_dotenv

load_dotenv()

subject = "Email subject"
body = "This is the email's body"
# sender = "taukirshekh4732@gmail.com"
# default_receiver = "shekhtaukir13@gmail.com"
# password = "cnlaozbwfcdjuuzt"

sender = str(os.getenv("default_sender"))
default_receiver = str(os.getenv("default_receiver"))
password = str(os.getenv("app_password"))

recipients = [sender]


# app name : FastAPI_JobPortal in taukirshekh4732@gmail.com


# subject, body, sender, recipients, password
def of_send_email(as_subject: str, as_body: str, as_email: str):

    body = as_body if as_body is not None else body
    subject = as_subject if as_subject is not None else subject
    as_email = as_email if as_email is not None else default_receiver

    recipients.append(as_email)

    print(f"Email scheduled for {' '.join(recipients)}")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = " ".join(recipients)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
