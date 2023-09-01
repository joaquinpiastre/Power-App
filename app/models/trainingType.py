from app import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class trainingType(db.Model):
    __tablename__ = 'trainingType'
    __name = db.Column(db.String(120), primary_key=True)

    @property
    def name(self) -> int:
        return self.__name
    
    @name.setter
    def name(self, name) -> int:
        self.__name = name
        
    def __repr__(self) -> str:
        return f'TrainingType: [Name: {self.name}]'
    
    def __eq__(self, o: object) -> bool:
        return self.name == o.name
    
    def serialize(self) -> dict:
        return {
            'name': self.name
        }
        