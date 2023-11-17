from app.models.instructor import Instructor
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class InstructorRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__model = Instructor
    
    def create(self, instructor: Instructor) -> db.Model:
        db.session.add(instructor)
        db.session.commit()
        return instructor
    
    def find_all(self):
        return db.session.query(Instructor).all()
    
    def find_by_id(self, id) -> Instructor:
        return db.session.query(self.__model).filter(self.__model.id == id).one_or_none()
    
    def find_by_name(self, name) -> Instructor:
        return db.session.query(self.__model).filter(self.__model.name == name).one_or_none()
    
    def find_by_email(self, email) -> Instructor:
        return db.session.query(self.__model).filter(self.__model.email == email).one_or_none()

    def update(self, id: int, new_data: dict) -> Instructor:
        instructor = self.find_by_id(id)
        if instructor:
            instructor.name = new_data.get('name', instructor.name)
            instructor.password = new_data.get('password', instructor.password)
            db.session.commit()
            return instructor
        else:
            raise ValueError("Instructor with id {} not found".format(id))

    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
