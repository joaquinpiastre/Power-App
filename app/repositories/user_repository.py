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
    
    def exist_by_id(self, id) -> bool:
        pass
    
    def find_all(self):
        return db.session.query(User).all()
    
    def find_by_id(self, id) -> User:
        return db.session.query(self.__model).filter_by(id=id).first()

    def update(self, user: User, id: int) -> User:
        entity = self.find_by_id(id)
        entity.name = user.name
        entity.email = user.email
        db.session.add(entity)
        db.session.commit()
        return entity

    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
