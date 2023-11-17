from app.models import Booking
from abc import ABC, abstractmethod
from datetime import datetime

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class BookGymClassCommand(Command):
    def __init__(self, user_service, gym_class_service, booking_service, user_id, gym_class_id):
        self.user_service = user_service
        self.gym_class_service = gym_class_service
        self.booking_service = booking_service
        self.user_id = user_id
        self.gym_class_id = gym_class_id

    def execute(self):
        user_id = self.user_service.find_by_id(self.user_id)
        gym_class_id = self.gym_class_service.find_by_id(self.gym_class_id)
        booking = Booking(user_id=self.user_id, gym_class_id=self.gym_class_id, booking_date=datetime.now())
        self.booking_service.add(booking)