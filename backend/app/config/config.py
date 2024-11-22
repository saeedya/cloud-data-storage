from os import environ
import secrets

# Generate a URL-safe text string
secret_key = secrets.token_urlsafe(32)

class Config:
    #############Basic configuration ###################
    ENV = environ.get("BACKEND_ENV", "development")

    DEBUG = bool(int(environ.get("BACKEND_DEBUG", "0")))

    SECRET_KEY = secret_key

