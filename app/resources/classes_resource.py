from flask import jsonify, Blueprint, request
from app.services.classes_service import ClassesService
from app.mapping.response_schema import ResponseSchema
from app.mapping.classes_schema import ClassesSchema
from app.models.response_message import ResponseBuilder

classes = Blueprint('classes', __name__)
class_schema = ClassesSchema()

@classes.route('/classes', methods=['GET'])
def get_classes():
    service = ClassesService()
    classes = service.find_all()
    return jsonify({"classes": classes}), 200

@classes.route('/classes/<int:id>', methods=['GET'])
def get_class(id):
    service = ClassesService()
    response_builder = ResponseBuilder()
    response_builder.add_message("Class found")\
        .add_status_code(200)\
        .add_data(ClassesSchema().dump(service.find(id)))
    return ResponseSchema().dump(response_builder.build()), 200

@classes.route('/classes', methods=['POST'])
def create_class():
    service = ClassesService()
    class_data = request.get_json()
    new_class = service.create(class_data)
    return {"message": "Class created", "class": ClassesSchema().dump(new_class)}, 201

@classes.route('/classes/<int:id>', methods=['PUT'])
def update_class(id):
    service = ClassesService()
    class_data = request.get_json()
    updated_class = service.update(id, class_data)
    return {"message": "Class updated", "class": ClassesSchema().dump(updated_class)}, 200

@classes.route('/classes/<int:id>', methods=['DELETE'])
def delete_class(id):
    service = ClassesService()
    service.delete(id)
    return {"message": "Class deleted"}, 200
