from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db

class Reservation(db.Model):
    __tablename__ = 'Reservation'
    __user = db.Column('user', db.Integer, unique=True, primary_key=True)
    __class = db.Column('class', db.Integer)
    __date = db.Column('date', db.DateTime)
    
    @hybrid_property
    def user(self) -> int:
        return self.__user
    
    @user.setter
    def user(self, user) -> int:
        self.__user = user
        
    @hybrid_property
    def __class(self) -> str:
        return self.__class
    
    @__class.setter
    def __class(self, __class) -> str:
        self.__class = __class
        
    @hybrid_property
    def date(self) -> str:
        return self.__date
    
    @date.setter
    def date(self, date) -> str:
        self.__date = date
 
    def __repr__(self) -> str:
        return f'Reservation: [user: {self.user}, class: {self.__class}, date: {self.date}]'
    
    def __eq__(self, o: object) -> bool:
        return self.user == o.user and self.__class == o.__class and self.date == o.date
    
    def serialize(self) -> dict:
        return {
            'user': self.user,
            'class': self.__class,
            'date': self.date,
        }
        