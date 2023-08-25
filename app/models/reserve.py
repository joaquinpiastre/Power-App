from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(120), unique=True)
    _email = db.Column(db.String(120), unique=True)
    _password = db.Column(db.String(120))
    reservations = relationship('Reservation', back_populates='user')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password

    def __repr__(self):
        return f'User: [ID: {self.id}, Name: {self.name}, Email: {self.email}, Password: {self.password}]'

class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    _time = db.Column(db.String(10), nullable=False, unique=True)
    reservations = relationship('Reservation', back_populates='schedule')

    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, time):
        self._time = time

    def __repr__(self):
        return f'Schedule: [ID: {self.id}, Time: {self.time}]'

class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    schedule_id = db.Column(db.Integer, ForeignKey('schedule.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user = relationship('User', back_populates='reservations')
    schedule = relationship('Schedule', back_populates='reservations')

    def __repr__(self):
        return f'Reservation: [ID: {self.id}, User: {self.user.name}, Schedule: {self.schedule.time}, Date: {self.date}]'

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user.name,
            'schedule': self.schedule.time,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S')
        }
