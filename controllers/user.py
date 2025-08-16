from flask import Blueprint, jsonify
from flask_sqlalchemy import SQLAlchemy

from factory import db
from models import User

user_controller = Blueprint('user_controller', __name__, url_prefix='/user')

@user_controller.route('/list', methods=['GET'])
def user_list ():

    users = User.query.all()
    response = [{'username': user.username, 'email': user.email} for user in users]

    return jsonify(response), 200