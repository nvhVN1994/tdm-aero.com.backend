# 📄 app/routes.py
from flask import Blueprint, request, jsonify
from .controllers import handle_form_submission

main = Blueprint('main', __name__)

@main.route('/api/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    return handle_form_submission(data)