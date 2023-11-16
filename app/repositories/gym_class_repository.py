from app.models.gym_class import GymClass
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class GymClassRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__model = GymClass
    
    def find_all(self):
        return db.session.query(self.__model).all()
        
    def find_by_id(self, id) -> GymClass:
        return db.session.query(self.__model).filter(self.__model.id == id).one_or_none()

    def create(self, class_data: GymClass) -> db.Model:
        new_class = GymClass(
            gym_name=class_data['gym_name'],
            instructor_name=class_data['instructor_name'],
            type_class=class_data['type_class'],
        )
        db.session.add(new_class)
        db.session.commit()
        return new_class
    
    def update(self, class_data: dict, id: int) -> GymClass:
        entity = self.find_by_id(id)
        entity.gym_name = class_data['gym_name']
        entity.instructor_name = class_data['instructor_name']
        entity.type_class = class_data['type_class']
        db.session.commit()
        return entity

    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()