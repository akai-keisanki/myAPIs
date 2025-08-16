from flask import Blueprint

example_controller = Blueprint('example_controller', __name__, url_prefix='/example')

@example_controller.route('/', methods = ['GET'])
def example_get (): return 'Route successfully called with the GET method!', 200

@example_controller.route('/', methods = ['POST'])
def example_post (): return 'Route successfully called with the POST method!', 200

@example_controller.route('/', methods = ['PUT'])
def example_put (): return 'Route successfully called with the DELETE method!', 200

@example_controller.route('/', methods = ['DELETE'])
def example_delete (): return 'Route successfully called with the DELETE method!', 200

