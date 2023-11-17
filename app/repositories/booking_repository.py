from app.models.booking import Booking
from app.repositories.repository_base import Create, Read, Update, Delete
from app import db

class BookingRepository(Create, Read, Update, Delete):
    def __init__(self) -> None:
        self.__model = Booking
    
    def find_all(self):
        return db.session.query(self.__model).all()
        
    def find_by_id(self, id) -> Booking:
        return db.session.query(self.__model).filter(self.__model.id == id).one_or_none()

    def create(self, booking: Booking) -> Booking:
        new_booking = Booking(
            user_id=booking.user_id,
            gym_class_id=booking.gym_class_id,
            booking_date=booking.booking_date
        )
        db.session.add(new_booking)
        db.session.commit()
        return new_booking
    
    def update(self, class_data: dict, id: int) -> Booking:
        entity = self.find_by_id(id)
        entity.gym_name = class_data['gym_name']
        db.session.commit()
        return entity

    def delete(self, id: int):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()