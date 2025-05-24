import smtplib
from email.mime.text import MIMEText
import os

def send_email(data):
    body = '\n'.join([f"{k}: {v}" for k, v in data.items() if k != "recaptchaToken"])
    msg = MIMEText(body)
    msg['Subject'] = 'New Quote Request'
    msg['From'] = os.getenv("SMTP_USERNAME")
    msg['To'] = os.getenv("EMAIL_RECEIVER")

    with smtplib.SMTP(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
        server.send_message(msg)
