from app.models import User
from app.repositories.user_repository import UserRepository
from app.services.security_service import SecurityService
from app.services.email_service import EmailService
from app.services.validate_country import ValidateCountry
from werkzeug.security import check_password_hash

class UserService():
    def __init__(self) -> None:
        self.__repo = UserRepository()
    
    def find (self, id) -> User:
        return self.__repo.find_by_id(id)
    
    def find_all (self) -> list[User]:
        return self.__repo.find_all()

    def register(self, name, email, password):
        validateCountry = ValidateCountry("Argentina")
        validateCountry.validate_country()
        self.create_user(name, email, password)
        emailService = EmailService()
        emailService.send_email(email, "Bienvenido a nuestra plataforma")
        #TODO: Registrar en el log
                
    def create (self, entity: User) -> User:
        entity_password = SecurityService.generate_password_hash(entity_password)
        return self.__repo.create(entity)
    
    def update (self, entity: User) -> User:
        return self.__repo.update(entity, id)

    def find_by_username (self, username: str) -> User:
        return self.__repo.find_by_username(username)
    
    def check_password(self, user: User, password: str) -> bool:
        return check_password_hash(user.password, password)
    
    def check_auth(self, username, password):
        try:
            user = self.find_by_username(username)
        except User.DoesNotExist:
            return False
        return self.check_password(user, password)
