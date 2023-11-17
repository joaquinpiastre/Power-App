from app.models.gym_class import GymClass
from app.repositories.repository_base import Create, Read, Update, Delete
from app.repositories.gym_class_repository import GymClassRepository
from abc import ABC, abstractmethod

class GymClassService(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__repo = GymClassRepository()
    
    def find_all(self):
        return self.__repo.find_all()

    def find_by_id(self, id):
        return self.__repo.find_by_id(id)

    def create(self, class_data):
        return self.__repo.create(class_data)

    def update(self, id, class_data):
        return self.__repo.update(id, class_data)

    def delete(self, id):
        return self.__repo.delete(id)