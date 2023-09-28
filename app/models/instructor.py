from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from app import db

class Instructor(db.Model):
    __tablename__ = 'Instructor'
    __name = db.Column('name', db.String, primary_key=True)
    __specialty = db.Column('specialty', db.String)

    @hybrid_property
    def name(self) -> int:
        return self.__name
    
    @name.setter
    def name(self, name) -> int:
        self.__name = name

    @hybrid_property
    def specialty(self) -> str:
        return self.__specialty
    
    @specialty.setter
    def specialty(self, specialty) -> str:
        self.__specialty = specialty
        
    def __repr__(self) -> str:
        return f'Instructor: [Name: {self.name}, Specialty: {self.specialty}]'
    
    def __eq__(self, o: object) -> bool:
        return self.name == o.name and self.specialty == o.specialty


    def serialize(self) -> dict:
        return {
            'name': self.name,
            'specialty': self.specialty
        }
    