from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app () -> Flask:

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from models import *

    migrate.init_app(app, db)

    @app.route('/', methods = ['GET'])
    def root (): return 'The application is running successfully!', 200

    return app