from app.models import Instructor
from app.repositories.instructor_repository import InstructorRepository
from app.services.security_service import SecurityService
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import check_password_hash

class InstructorService():
    def __init__(self) -> None:
        self.__repo = InstructorRepository()
        
    def execute(self, model):
        self.register(model.name, model.email, model.password)
    
    def find_by_id(self, id) -> Instructor:
        return self.__repo.find_by_id(id)
    
    def find_all (self) -> list[Instructor]:
        return self.__repo.find_all()

    def register(self, entity: Instructor) -> Instructor:
        entity.password = SecurityService.generate_hash(entity.password)
        return InstructorRepository().create(entity)
    
    def update (self, id: int, entity: Instructor) -> Instructor:
        return self.__repo.update(id, entity)
    
    def delete (self, entity: Instructor) -> bool:
        return self.__repo.delete(entity)

    def find_by_name (self, name: str) -> Instructor:
        return self.__repo.find_by_name(name)
    
    def find_by_email (self, email: str) -> Instructor:
        return self.__repo.find_by_email(email)
    
    def check_password(self, user: Instructor, password: str) -> bool:
        return check_password_hash(user.password, password)
    
    def check_auth(self, email, password):
        try:
            user = self.find_by_email(email)
        except NoResultFound:
            return False
        return self.check_password(user, password)
