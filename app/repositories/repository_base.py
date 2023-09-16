from abc import ABC, abstractmethod
from app import db

class Create(ABC):
    
    @abstractmethod
    def create(self, obj):
        pass
    
class Read(ABC):
    
    @abstractmethod
    def find_all(self):
        pass
    
    @abstractmethod
    def find_by_id(self, id):
        pass
    
class Update(ABC):
    
    @abstractmethod
    def update(self, obj):
        pass
    
class Delete(ABC):
    
    @abstractmethod
    def delete(self, obj):
        pass
