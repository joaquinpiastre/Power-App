from flask import jsonify, Blueprint
from app.services.user_service import UserService
from app.mapping.response_schema import ResponseSchema
from app.mapping.user_schema import UserSchema
from app.models.responseMessage import ResponseBuilder


user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def index():
    service = UserService()
    list = service.find_all()
    return jsonify(list, "W"), 200

"""
id: int ingresado por el usuario
return: json con los datos del usuario
"""
@user.route('/user/<int:id>', methods=['GET'])
def find(id):
    service = UserService()
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado")\
        .add_status_code(200)\
        .add_data(UserSchema().dump(service.find(id)))
    return ResponseSchema().dump(response_builder.build()), 200