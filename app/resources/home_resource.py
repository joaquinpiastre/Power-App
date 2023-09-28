from flask import jsonify, Blueprint

home = Blueprint('home', __name__)

@home.route('/home', methods=['GET'])
def index():
    resp = jsonify("message: Welcome to the API of PowerAPP!")
    resp.status_code = 200
    return resp
