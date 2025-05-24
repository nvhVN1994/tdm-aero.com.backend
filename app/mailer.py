import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(data):
    msg = MIMEMultipart()
    msg['From'] = os.getenv('SMTP_USERNAME')
    msg['To'] = os.getenv('EMAIL_RECIPIENT')
    msg['Subject'] = 'New Quote Request from Website'

    content = "\n".join([f"{k}: {v}" for k, v in data.items()])
    msg.attach(MIMEText(content, 'plain'))

    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
        server.starttls()
        server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
        server.send_message(msg)
