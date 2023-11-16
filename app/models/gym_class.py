from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import db
from dataclasses import dataclass

@dataclass
class GymClass(db.Model):
    __tablename__ = 'gym_classes'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    gym_name = db.Column('gym_name', db.String)
    type_class = db.Column('type_class', db.String)
    instructor_id = db.Column('instructor_id', db.Integer, ForeignKey('instructors.id'))
    
    instructors = db.relationship("Instructor", back_populates="gym_classes")