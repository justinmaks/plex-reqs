import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///requests.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
