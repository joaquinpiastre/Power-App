from app.models.class_model import ClassModel
from app import db

class ClassesService:
    def find_all(self):
        return ClassModel.query.all()

    def find(self, id):
        return ClassModel.query.get(id)

    def create(self, class_data):
        new_class = ClassModel(
            name=class_data['name'],
            description=class_data['description'],
            start_time=class_data['start_time'],
            end_time=class_data['end_time'],
            instructor=class_data['instructor']
        )
        db.session.add(new_class)
        db.session.commit()
        return new_class

    def update(self, id, class_data):
        class_to_update = ClassModel.query.get(id)
        class_to_update.name = class_data['name']
        class_to_update.description = class_data['description']
        class_to_update.start_time = class_data['start_time']
        class_to_update.end_time = class_data['end_time']
        class_to_update.instructor = class_data['instructor']
        db.session.commit()
        return class_to_update

    def delete(self, id):
        class_to_delete = ClassModel.query.get(id)
        db.session.delete(class_to_delete)
        db.session.commit()
