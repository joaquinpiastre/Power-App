from app.config.database import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'
    __id = db.Column(db.Integer, primary_key=True)
    __name = db.Column(db.String(120), unique=True)
    __email = db.Column(db.String(120), unique=True)
    __password = db.Column(db.String(120))

    @property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id) -> int:
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name) -> str:
        self.__name = name
        
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email) -> str:
        self.__email = email
    
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, password) -> str:
        self.__password = password

    def __repr__(self) -> str:
        return f'User: [ID: {self.id}, Name: {self.name}, Email: {self.email} Password: {self.password}]'

    def __eq__(self, o: object) -> bool:
        return self.id == o.id and self.name == o.name and self.email == o.email and self.password == o.password

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }