from app.models import User
from app.repositories.user_repository import UserRepository
from app.services.security_service import SecurityService
from app.services.email_service import EmailService
from app.services.user_balance import UserBalance
from app.services.command import TareaCommand
from werkzeug.security import check_password_hash

class UserService(TareaCommand):
    def __init__(self) -> None:
        self.__repo = UserRepository()
        
    def execute(self, model):
        self.register(model.name, model.email, model.password)
    
    def find (self, id) -> User:
        return self.__repo.find_by_id(id)
    
    def find_all (self) -> list[User]:
        return self.__repo.find_all()

    def register(self, name, email, password):
        self.user_balance()
        self.create(name, email, password)
        emailService = EmailService()
        emailService.send_email(email, "Bienvenido a nuestra plataforma")

    def create(self, entity: User) -> User:
        entity.password = SecurityService.generate_hash(entity.password)
        return UserRepository().create(entity)
    
    def update (self, id: int, entity: User) -> User:
        return self.__repo.update(id, entity)
    
    def delete (self, entity: User) -> bool:
        return self.__repo.delete(entity)

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
    
    def user_balance(self, country):
        userBalance = UserBalance()
        userBalance.execute(country)
            