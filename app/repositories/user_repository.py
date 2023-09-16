from app.models.user import User
from app import db

class UserRepository():
    def __init__(self) -> None:
        self.__model = User

    def find_all(self):
        return db.session.query(User).all()
    
    def find_by_id(self, id, init) -> User:
        return db.session.query(self.__model).filter_by(id=id).first()

    def create(self, user):
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user):
        db.session.merge(user)
        db.session.commit()
        return user

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()
        return user