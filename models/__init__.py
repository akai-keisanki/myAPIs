from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from factory import db

class User (db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, index=True, nullable=False)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.Text, unique=False, index=False, nullable=False)
    creation_date = db.Column(db.DateTime, unique=False, index=True, nullable=False, default=datetime.utcnow())