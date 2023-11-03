from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from app import db

class Classes(db.Model):
    __tablename__ = 'Classes'
    __id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name', db.String)
    __instructor = db.Column('instructor', db.String)
    __type = db.Column('type', db.String)
    __capacity = db.Column('capacity', db.Integer)

    @hybrid_property
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id) -> int:
        self.__id = id

    @hybrid_property
    def name(self) -> int:
        return self.__name
    
    @name.setter
    def name(self, name) -> int:
        self.__name = name

    @hybrid_property
    def instructor(self) -> str:
        return self.__instructor
    
    @instructor.setter
    def instructor(self, instructor) -> str:
        self.__instructor = instructor
        
    @hybrid_property
    def type(self) -> str:
        return self.__type
    
    @type.setter
    def type(self, type) -> str:
        self.__type = type
    
    @hybrid_property
    def capacity(self) -> str:
        return self.__capacity
    
    @capacity.setter
    def capacity(self, capacity) -> str:
        self.__capacity = capacity

    def __repr__(self) -> str:
        return f'Classes: [ID: {self.id}, Name: {self.name}, Instructor: {self.instructor}, Type: {self.type}, Capacity: {self.capacity}]'

    def __eq__(self, o: object) -> bool:
        return self.id == o.id and self.name == o.name and self.instructor == o.instructor and self.type == o.type and self.capacity == o.capacity

    def serialize(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'instructor': self.instructor,
            'type': self.type,
            'capacity': self.capacity
        }
    