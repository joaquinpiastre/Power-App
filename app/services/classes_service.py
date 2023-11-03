from app.models.classes import Classes
from app.repositories.repository_base import Create, Read, Update, Delete
from app.repositories.classes_repository import ClassRepository
from app import db

class ClassesService:
    def __init__(self) -> None:
        self.__repo = ClassRepository()
    
    def find_all(self):
        return self.__repo.find_all()

    def find(self, id):
        return Classes.query.get(id)

    def create(self, class_data):
        return self.__repo.create(class_data)

    def update(self, id, class_data):
        return self.__repo.update(id, class_data)

    def delete(self, id):
        return self.__repo.delete(id)