from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from app import db
from dataclasses import dataclass

@dataclass
class Instructor(db.Model):
    __tablename__ = 'Instructor'
    name = db.Column('name', db.String, primary_key=True)
    specialty = db.Column('specialty', db.String)
