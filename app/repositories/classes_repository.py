from app.models.class_model import ClassModel
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class ClassRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__model = ClassModel

    def create(self, class_data: ClassModel) -> db.Model:
        new_class = ClassModel(
            name=class_data.name,
            description=class_data.description,
            start_time=class_data.start_time,
            end_time=class_data.end_time,
            instructor=class_data.instructor
        )
        db.session.add(new_class)
        db.session.commit()
        return new_class
    
    def exist_by_id(self, id) -> bool:
        pass
    
    def find_all(self):
        return db.session.query(ClassModel).all()
    
    def find_by_id(self, id, init) -> ClassModel:
        return db.session.query(self.__model).filter_by(id=id).first()

    def update(self, class_data: ClassModel, id: int) -> ClassModel:
        entity = self.find_by_id(id)
        entity.name = class_data.name
        entity.description = class_data.description
        entity.start_time = class_data.start_time
        entity.end_time = class_data.end_time
        entity.instructor = class_data.instructor
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()