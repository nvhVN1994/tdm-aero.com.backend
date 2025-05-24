import smtplib
from email.message import EmailMessage
import os

def send_email(data):
    msg = EmailMessage()
    msg["Subject"] = "New Quote Request"
    msg["From"] = os.getenv("SMTP_USERNAME")
    msg["To"] = os.getenv("EMAIL_RECIPIENT")  

    msg.set_content("\n".join(f"{k}: {v}" for k, v in data.items()))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
        server.send_message(msg)
