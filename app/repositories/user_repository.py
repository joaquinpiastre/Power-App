from app.models.user import User
from app.config.database import db

class UserRepository():
    def __init__(self) -> None:
        pass

    def find_all(self):
        return User.query.all()

    def find_by_id(self, id):
        return User.query.get(id)

    def find_by_email(self, email):
        return User.query.filter_by(email=email).first()

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