from flask import jsonify, Blueprint, request
from app.services.user_service import UserService
from app.mapping.response_schema import ResponseSchema
from app.mapping.user_schema import UserSchema
from app.models.responseMessage import ResponseBuilder

user = Blueprint('user', __name__)
user_schema = UserSchema()

@user.route('/user', methods=['GET'])
def index():
    service = UserService()
    users = service.find_all()
    return jsonify({"users": users}), 200

"""
id: int ingresado por el usuario
return: json con los datos del usuario
"""
#find
@user.route('/find_user/<int:id>', methods=['GET'])
def find(id):
    service = UserService()
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado")\
        .add_status_code(200)\
        .add_data(UserSchema().dump(service.find(id)))
    return ResponseSchema().dump(response_builder.build()), 200

#create
@user.route('/add_user', methods=['POST'])
def create():
    service = UserService()
    user = user_schema.load(request.json)
    service.create(user)
    return {"message": "Usuario creado"}, 200

#delete
@user.route('/delete_user/<int:id>', methods=['DELETE'])
def delete(id):
    service = UserService()
    service.delete(id)
    return {"message": "Usuario eliminado"}, 200

#update
@user.route('/update_user/<int:id>', methods=['PUT'])
def update(user):
    service = UserService()
    user = user_schema.load(request.json)
    service.update(user)
    return {"message": "Usuario actualizado"}, 200
