from flask import jsonify
from .utils import verify_recaptcha
from .telegram import send_telegram_message
from .whatsapp import send_whatsapp_message  # 👈 THÊM DÒNG NÀY

def handle_form_submission(data):
    try:
        token = data.get('recaptchaToken')
        if not token:
            return jsonify({ 'message': 'Missing reCAPTCHA token' }), 400

        if not verify_recaptcha(token):
            return jsonify({ 'message': 'Failed reCAPTCHA verification' }), 403

        # Soạn tin nhắn
        message = "\n".join([f"{k}: {v}" for k, v in data.items() if k != 'recaptchaToken'])

        # Gửi qua Telegram và WhatsApp
        send_telegram_message(data)
        send_whatsapp_message(f"📨 New RFQ Submission:\n{message}")  # 👈 GỌI WHATSAPP

        return jsonify({ 'message': 'Form submitted and sent to Telegram & WhatsApp!' }), 200

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({ 'message': 'Server error', 'error': str(e) }), 500
