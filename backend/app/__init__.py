from flask import Flask
from app.routes.auth import auth_blueprint
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
    return app