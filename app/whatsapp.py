# app/whatsapp.py
import os
from twilio.rest import Client

def send_whatsapp_message(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")  # usually: whatsapp:+14155238886
    to_whatsapp = os.getenv("WHATSAPP_TO")  # e.g. whatsapp:+849xxxxxxxx

    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=from_whatsapp,
        to=to_whatsapp
    )
