from dataclasses import dataclass
from app import db
from .relations import user_roles

@dataclass
class Role(db.Model):
    id: int
    name: str
    description: str

    __tablename__ = "role"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(50), nullable=False)
    description = db.Column('description', db.String(120), nullable=False)
    #users = db.relationship("User", secondary=user_roles, back_populates="roles")