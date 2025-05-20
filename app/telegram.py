# 📄 app/telegram.py
import os
import requests

def send_telegram_message(form):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    text_lines = [f"✈️ New Quote Request"]
    for key, value in form.items():
        if key != 'recaptchaToken':
            text_lines.append(f"{key}: {value}")
    text = "\n".join(text_lines)

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url, json=payload)
    print("📤 Telegram status:", r.status_code)
