from app.models import User
from app.repositories.user_repository import UserRepository
from app.services.security_service import SecurityService
from app.services.email_service import EmailService
from sqlalchemy.orm.exc import NoResultFound
from app.services.user_balance import UserBalance
from app.services.command import TareaCommand
from werkzeug.security import check_password_hash

class UserService(TareaCommand):
    def __init__(self) -> None:
        self.__repo = UserRepository()
        
    def execute(self, model):
        self.register(model.name, model.email, model.password)
    
    def register_user(self, name, email, password):
        self.__repo.register_user(name, email, password)
    
    def login_user(self, name, password):
        self.__repo.login_user(name, password)
    
    def find (self, id) -> User:
        return self.__repo.find_by_id(id)
    
    def find_all (self) -> list[User]:
        return self.__repo.find_all()

    def create(self, entity: User) -> User:
        entity.password = SecurityService.generate_hash(entity.password)
        return UserRepository().create(entity)
    
    def update (self, id: int, entity: User) -> User:
        return self.__repo.update(id, entity)
    
    def delete (self, entity: User) -> bool:
        return self.__repo.delete(entity)

    def find_by_name (self, username: str) -> User:
        return self.__repo.find_by_name(username)
    
    def check_password(self, user: User, password: str) -> bool:
        return check_password_hash(user.password, password)
    
    def check_auth(self, name, password):
        try:
            user = self.find_by_name(name)
        except NoResultFound:
            return False
        return self.check_password(user, password)
    
    def user_balance(self, country):
        userBalance = UserBalance()
        userBalance.execute(country)
            