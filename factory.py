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

    # Models

    from models import User

    migrate.init_app(app, db)

    # Main routes

    @app.route('/', methods = ['GET'])
    def root (): return 'The application is running successfully!', 200

    # Controllers

    from controllers import example_controller

    app.register_blueprint(example_controller)

    return app