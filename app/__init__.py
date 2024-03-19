"""
Main file of app
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)   # definieert context waarbinnen je connecteert met db (via config file)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models   # Moet hier staan om circulaire imports te vermijden.
