from flask import jsonify, Blueprint

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    resp = jsonify("message: Welcome to the API of the Fitness Center!")
    resp.status_code = 200
    return resp
