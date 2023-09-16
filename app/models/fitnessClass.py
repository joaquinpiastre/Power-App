from app import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class FitnessClass(db.Model):
    __tablename__ = 'fitnessClass'
    __name = db.Column(db.String(80), primary_key=True)
    __instructor = db.Column(db.String(120), unique=True)
    __schedule = db.Column(db.DateTime, default=datetime.utcnow)
    __maxCapacity = db.Column(db.Integer, unique=True)

    @property
    def name(self) -> int:
        return self.__name
    
    @name.setter
    def name(self, name) -> int:
        self.__name = name

    @property
    def instructor(self) -> str:
        return self.__instructor
    
    @instructor.setter
    def instructor(self, instructor) -> str:
        self.__instructor = instructor
        
    @property
    def schedule(self) -> str:
        return self.__schedule
    
    @schedule.setter
    def schedule(self, schedule) -> str:
        self.__schedule = schedule
    
    @property
    def maxCapacity(self) -> str:
        return self.__maxCapacity
    
    @maxCapacity.setter
    def maxCapacity(self, maxCapacity) -> str:
        self.__maxCapacity = maxCapacity

    def __repr__(self) -> str:
        return f'fitnessClass: [name: {self.name}, instructor: {self.instructor}, schedule: {self.schedule} maxCapacity: {self.maxCapacity}]'

    def __eq__(self, o: object) -> bool:
        return self.name == o.name and self.instructor == o.instructor and self.schedule == o.schedule and self.maxCapacity == o.maxCapacity

    def serialize(self) -> dict:
        return {
            'name': self.name,
            'instructor': self.instructor,
            'schedule': self.schedule,
            'maxCapacity': self.maxCapacity
        }
    