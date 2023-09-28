from sqlalchemy import Column, Integer, String, Float, ForeignKeyConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from app import db

class User(db.Model):
    __tablename__ = 'User'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String, unique=True)
    __email = db.Column('email', db.String, unique=True)
    __password = db.Column('password', db.String)

    @hybrid_property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id) -> int:
        self.__id = id

    @hybrid_property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name) -> str:
        self.__name = name
        
    @hybrid_property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email) -> str:
        self.__email = email
    
    @hybrid_property
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