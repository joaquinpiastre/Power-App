from app import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Gym(db.Model):
    __tablename__ = 'gym'
    __name = db.Column(db.String(120), primary_key=True)
    __location = db.Column(db.String(120), unique=True)
    __offeredClasses = db.Column(db.String(120), unique=True)

    @property
    def name(self) -> int:
        return self.__name
    
    @name.setter
    def name(self, name) -> int:
        self.__name = name
        
    @property
    def location(self) -> str:
        return self.__location
    
    @location.setter
    def location(self, location) -> str:
        self.__location = location
        
    @property
    def offeredClasses(self) -> str:
        return self.__offeredClasses
    
    @offeredClasses.setter
    def offeredClasses(self, offeredClasses) -> str:
        self.__offeredClasses = offeredClasses
        
    def __repr__(self) -> str:
        return f'Gym: [Name: {self.name}, Location: {self.location}, Offered Classes: {self.offeredClasses}]'
    
    def __eq__(self, o: object) -> bool:
        return self.name == o.name and self.location == o.location and self.offeredClasses == o.offeredClasses


    def serialize(self) -> dict:
        return {
            'name': self.name,
            'location': self.location,
            'offeredClasses': self.offeredClasses
        }
    