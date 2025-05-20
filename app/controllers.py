# 📄 app/controllers.py
from flask import jsonify
from .utils import verify_recaptcha
from .telegram import send_telegram_message

def handle_form_submission(data):
    try:
        token = data.get('recaptchaToken')
        if not token:
            return jsonify({ 'message': 'Missing reCAPTCHA token' }), 400

        if not verify_recaptcha(token):
            return jsonify({ 'message': 'Failed reCAPTCHA verification' }), 403

        send_telegram_message(data)
        return jsonify({ 'message': 'Form submitted and sent to Telegram!' }), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({ 'message': 'Server error', 'error': str(e) }), 500