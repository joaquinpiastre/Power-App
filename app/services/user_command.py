from app.models import Booking
from abc import ABC, abstractmethod
from datetime import datetime

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class BookGymClassCommand(Command):
    def __init__(self, booking_service, user_id, gym_class_id):
        self.booking_service = booking_service
        self.user_id = user_id
        self.gym_class_id = gym_class_id

    def execute(self):
        booking = Booking(user_id=self.user_id, gym_class_id=self.gym_class_id, booking_date=datetime.now())
        self.booking_service.add(booking)

class CancelGymClassCommand(Command):
    def __init__(self, booking_service, booking_id):
        self.booking_service = booking_service
        self.booking_id = booking_id

    def execute(self):
        self.booking_service.delete(self.booking_id)      