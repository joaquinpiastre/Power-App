from app.models.classes import Classes
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class ClassRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__model = Classes

    def create(self, class_data: Classes) -> db.Model:
        new_class = Classes(
            name=class_data['name'],
            instructor=class_data['instructor'],
            type=class_data['type'],
            capacity=class_data['capacity'],
        )
        db.session.add(new_class)
        db.session.commit()
        return new_class
    
    def exist_by_id(self, id) -> bool:
        pass
    
    def find_all(self):
        return db.session.query(self.__model).all()
        
    def find_by_id(self, id) -> Classes:
        return db.session.query(self.__model).filter_by(id=id).first()

    def update(self, class_data: dict, id: int) -> Classes:
        entity = self.find_by_id(id)
        entity.instructor = class_data['instructor']
        entity.type = class_data['type']
        entity.capacity = class_data['capacity']
        db.session.commit()
        return entity

    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()