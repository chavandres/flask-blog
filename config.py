import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-secret-is-my-secret'