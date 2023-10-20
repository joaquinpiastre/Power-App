from app.models import User
from app.services import UserService, EmailService, UserBalance, Tarea

class UserTarea:
    def __init__(self):
        self.__tarea = Tarea()
        self.__tarea.add_tarea(UserService())
        self.__tarea.add_tarea(EmailService())
        self.__tarea.add_tarea(UserBalance())
        self.__tarea.execute(User)
        
    def register(self, user):
        self.__tarea.execute(User)
