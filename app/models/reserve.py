from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Reserve(db.Model):
    __tablename__ = 'reserve'
    __user = db.Column(db.Integer, unique=True, primary_key=True)
    __class = db.Column(db.Integer, ForeignKey('fitnessClass.name'))
    __date = db.Column(db.DateTime, default=datetime.utcnow)
    __schedule = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def user(self) -> int:
        return self.__user
    
    @user.setter
    def user(self, user) -> int:
        self.__user = user
        
    @property
    def __class(self) -> str:
        return self.__class
    
    @__class.setter
    def __class(self, __class) -> str:
        self.__class = __class
        
    @property
    def date(self) -> str:
        return self.__date
    
    @date.setter
    def date(self, date) -> str:
        self.__date = date
    
    @property
    def schedule(self) -> str:
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule) -> str:
        self.__schedule = schedule
    
    def __repr__(self) -> str:
        return f'Reserve: [user: {self.user}, class: {self.__class}, date: {self.date}, schedule: {self.schedule}]'
    
    def __eq__(self, o: object) -> bool:
        return self.user == o.user and self.__class == o.__class and self.date == o.date and self.schedule == o.schedule
    
    def serialize(self) -> dict:
        return {
            'user': self.user,
            'class': self.__class,
            'date': self.date,
            'schedule': self.schedule
        }
        