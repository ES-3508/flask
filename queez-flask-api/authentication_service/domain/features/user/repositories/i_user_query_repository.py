from abc import ABC, abstractmethod
from ..aggregates.user import User
from ..valueobjects.username import Username

class IUserQueryRepository(ABC):

    @abstractmethod
    def get_user_by_username_sql(self, user: Username) -> User:
        pass

    @abstractmethod
    def get_user_by_username_orm(self, user: Username) -> User:
        pass

    @abstractmethod
    async def get_user_by_username_async(self, user: Username) -> User:
        pass
    
    