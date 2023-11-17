from abc import ABC, abstractmethod
from ..aggregates.user import User
from ..valueobjects.token import Token
from ..valueobjects.password import Password

class IIdentityRepository(ABC):

    @abstractmethod
    def generate_token(self, user: User) -> str:
        pass

    @abstractmethod
    def verify_token(self, token: Token) -> bool:
        pass

    @abstractmethod
    def verify_password(self,user: User, password: Password) -> bool:
        pass

    @abstractmethod
    def encrypt_password(self,password: Password) -> str:
        pass

    