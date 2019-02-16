import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_CONNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
