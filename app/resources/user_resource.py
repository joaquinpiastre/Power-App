from flask import jsonify, Blueprint, request
from app.services.user_service import UserService
from app.mapping.response_schema import ResponseSchema
from app.mapping.user_schema import UserSchema
from app.models.response_message import ResponseBuilder
from app.services.command import BookGymClassCommand
from app.services.gym_class_service import GymClassService
from app.services.booking_service import BookingService
from app.resources.instructor_resource import GymClassServiceImpl

user = Blueprint('user', __name__)
user_schema = UserSchema()
    
# find all
@user.route('/find_all', methods=['GET'])
def index():
    service = UserService()
    users = service.find_all()
    return jsonify({"users": users}), 200

#find
@user.route('/find/<int:id>', methods=['GET'])
def find(id):
    service = UserService()
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado")\
        .add_status_code(200)\
        .add_data(UserSchema().dump(service.find_by_id(id)))
    return ResponseSchema().dump(response_builder.build()), 200

#delete
@user.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    service = UserService()
    service.delete(id)
    return {"message": "Usuario eliminado"}, 200

#update
@user.route('/update/<int:id>', methods=['PUT'])
def update(id):
    service = UserService()
    user_data = request.json
    service.update(id, user_data)
    return {"message": "Usuario actualizado"}, 200

@user.route('/book_class/<int:user_id>/<int:gym_class_id>', methods=['POST'])
def book_gym_class(user_id, gym_class_id):
    user_service = UserService()
    gym_class_service = GymClassServiceImpl()
    booking_service = BookingService()
    command = BookGymClassCommand(user_service, gym_class_service, booking_service, user_id, gym_class_id)
    command.execute()
    return {"message": "Clase de gimnasio reservada"}, 200