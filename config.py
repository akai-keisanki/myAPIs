import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY : str = os.environ.get('SECRET_KEY')
    APP_TITLE : str = 'myAPIs'

    SQLALCHEMY_DATABASE_URI : str = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False

    def init_app (app : Flask) -> None: pass