# 📄 app/utils.py
import os
import requests

def verify_recaptcha(token):
    secret = os.getenv('RECAPTCHA_SECRET_KEY')
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
        'secret': secret,
        'response': token
    })
    result = response.json()
    print("🔎 Recaptcha verify result:", result)
    return result.get('success', False)