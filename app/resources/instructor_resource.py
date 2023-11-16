from flask import jsonify, Blueprint, request
from app.services.instructor_service import InstructorService
from app.mapping.response_schema import ResponseSchema
from app.mapping.instructor_schema import InstructorSchema
from app.models.response_message import ResponseBuilder

instructor = Blueprint('instructor', __name__)
instructor_schema = InstructorSchema()

# find all
@instructor.route('/find_all', methods=['GET'])
def get_classes():
    service = InstructorService()
    class_data = instructor_schema.load(request.json)
    classes = service.find_all(class_data)
    return jsonify({"Classes": classes}), 200

#find by id
@instructor.route('/find/<int:id>', methods=['GET'])
def get_class(id):
    service = InstructorService()
    response_builder = ResponseBuilder()
    response_builder.add_message("Clase encontrada")\
        .add_status_code(200)\
        .add_data(InstructorSchema().dump(service.find(id)))
    return ResponseSchema().dump(response_builder.build()), 200

#update
@instructor.route('/update_class/<int:id>', methods=['PUT'])
def update_class(id):
    service = InstructorService()
    class_data = request.json
    updated_class = service.update(class_data, id)
    return {"message": "Instructor actualizado", "instructor": InstructorSchema().dump(updated_class)}, 200

#delete
@instructor.route('/delete_class/<int:id>', methods=['DELETE'])
def delete_class(id):
    service = InstructorService()
    service.delete(id)
    return {"message": "Instructor eliminado"}, 200
