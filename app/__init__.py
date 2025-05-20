# 📄 app/__init__.py
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app