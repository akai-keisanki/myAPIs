from flask import Blueprint, jsonify
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy

from factory import db
from models import User

user_controller = Blueprint('user_controller', __name__, url_prefix='/user')

@user_controller.route('/list', methods=['GET'])
def user_list ():

    users = User.query.all()
    response = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]

    return jsonify(response), 200

@user_controller.route('/<int:id>', methods=['GET'])
def user_id_get (id : int):

    user = User.query.filter_by(id = id).first()
    if not user: return {'message': f'User with id {id} not found!'}, 404

    response = {'id': user.id, 'username': user.username, 'email': user.email}

    return jsonify(response), 200

@user_controller.route('/', methods=['POST'])
def user_post ():

    data = request.json
    if not all(key in data for key in ['username', 'email', 'password']): return {'message': 'Bad request!'}, 400

    user = User(username=data['username'], email=data['email'], password=data['password'])

    db.session.add(user)
    db.session.commit()

    response = {'id': user.id, 'username': user.username, 'email': user.email}

    return jsonify(response), 201

@user_controller.route('/<int:id>', methods=['DELETE'])
def user_id_delete (id : int):

    data = request.json
    if 'password' not in data: return {'message': 'Bad request!'}, 400

    user = User.query.filter_by(id = id).first()
    if not user: return {'message': f'User with id {id} not found!'}, 404

    if data['password'] != user.password: return {'message': f'Wrong password for user with id {id}!'}, 403

    db.session.delete(user)
    db.session.commit()

    return {'message': f'User with id {id} successfully deleted!'}, 200