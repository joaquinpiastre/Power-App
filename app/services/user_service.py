from app.models import User
from app.repositories import UserRepository

class UserService():
    def __init__(self) -> None:
        pass
    def find_all(self):
        list_user = []
        user1 = User()
        user1.name = "Santiago"
        user1.email = "test@example.com.ar"
        user1.password = "123456"
        list_user.append(user1)
        return self.__repo.find_all()
