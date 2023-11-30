from abc import ABC, abstractmethod
from ..aggregates.user import User
from ..valueobjects.username import Username

class IUserCommandRepository(ABC):

    @abstractmethod
    def create_user_async(self, user: str) -> bool:
        pass

    
    