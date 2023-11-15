from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from app import db
from dataclasses import dataclass

@dataclass
class GymClass(db.Model):
    __tablename__ = 'gym_classes'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String)
    instructor = db.Column('instructor', db.String)
    type_class = db.Column('type_class', db.String)
    capacity = db.Column('capacity', db.Integer)
