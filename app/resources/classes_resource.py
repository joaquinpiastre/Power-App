from flask import jsonify, Blueprint, request
from app.services.classes_service import ClassesService
from app.mapping.response_schema import ResponseSchema
from app.mapping.classes_schema import ClassesSchema
from app.models.responseMessage import ResponseBuilder

classes = Blueprint('classes', __name__)
class_schema = ClassesSchema()

# find all
@classes.route('/find_all_classes', methods=['GET'])
def get_classes():
    service = ClassesService()
    class_data = class_schema.load(request.json)
    classes = service.find_all(class_data)
    return jsonify({"Classes": classes}), 200

#find by id
@classes.route('/find_class/<int:id>', methods=['GET'])
def get_class(id):
    service = ClassesService()
    response_builder = ResponseBuilder()
    response_builder.add_message("Clase encontrada")\
        .add_status_code(200)\
        .add_data(ClassesSchema().dump(service.find(id)))
    return ResponseSchema().dump(response_builder.build()), 200

#create
@classes.route('/add_class', methods=['POST'])
def create_class():
    service = ClassesService()
    class_data = request.get_json()
    new_class = service.create(class_data)
    return {"message": "Clase creada", "class": ClassesSchema().dump(new_class)}, 201

#update
@classes.route('/update_class/<int:id>', methods=['PUT'])
def update_class(id):
    service = ClassesService()
    class_data = request.json
    updated_class = service.update(class_data, id)
    return {"message": "Clase actualizada", "class": ClassesSchema().dump(updated_class)}, 200

#delete
@classes.route('/delete_class/<int:id>', methods=['DELETE'])
def delete_class(id):
    service = ClassesService()
    service.delete(id)
    return {"message": "Clase eliminada"}, 200
