from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db
from dataclasses import dataclass

@dataclass
class Booking(db.Model):
    __tablename__ = 'bookings'
    user = db.Column('user', db.Integer, unique=True, primary_key=True)
    clazz = db.Column('class', db.Integer)
    date = db.Column('date', db.DateTime)