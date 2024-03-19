"""
Config
"""
import os

#basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Config
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'guess_this'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'postgresql+psycopg2://Syntra_RL:raf+syntra@localhost:5432/Syntra_RL'
                               #postgresql+psycopg2://username:wachtwoord@localhost:5432/database
                               # Op localhost:5432 draait Postgres
