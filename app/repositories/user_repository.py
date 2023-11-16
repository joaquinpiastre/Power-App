from app.models.user import User
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class UserRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__model = User
    
    def create(self, user: User) -> db.Model:
        db.session.add(user)
        db.session.commit()
        return user
    
    def find_all(self):
        return db.session.query(User).all()
    
    def find_by_id(self, id) -> User:
        return db.session.query(self.__model).filter(self.__model.id == id).one_or_none()
    
    def find_by_name(self, name) -> User:
        return db.session.query(self.__model).filter(self.__model.name == name).one_or_none()
    
    def find_by_email(self, email) -> User:
        return db.session.query(self.__model).filter(self.__model.email == email).one_or_none()

    def update(self, id: int, new_data: dict) -> User:
        user = self.find_by_id(id)
        user.name = new_data['name']
        user.email = new_data['email']
        db.session.commit()
        return user

    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
