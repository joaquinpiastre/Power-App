from app.models.booking import Booking
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class BookingRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.model = Booking
    
    def find_all(self, user_id):
        return db.session.query(self.model).filter(self.model.user_id == user_id).all()    
                    
    def find_by_id(self, id) -> Booking:
        return super().find_by_id(id)
        
    def create(self, booking: Booking) -> Booking:
        return super().create(booking)
    
    def update(self, class_data: dict, id: int) -> Booking:
        return super().update(id, **class_data)

    def delete(self, id: int):
        return super().delete(id)