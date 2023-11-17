from sqlalchemy import Column, Integer, String, Float, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from dataclasses import dataclass
from app import db
from .relations import user_roles

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String)
    email = db.Column('email', db.String, unique=True)
    password = db.Column('password', db.String)
    
    roles = db.relationship("Role", secondary="user_roles", back_populates="users")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }