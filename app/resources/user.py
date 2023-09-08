from flask import jsonify, Blueprint
from app.services.user_service import UserService

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def index():
    service = UserService()
    list = service.find_all()
    return jsonify(list), 200
