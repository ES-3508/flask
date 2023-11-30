# authentication_service/infrastructure/repositories.py
from domain.models import User

class UserRepository:
    def __init__(self):
        self.users = [
            User(id=1, username='jason@ui-lib.com', password='dummyPass',token=''),  # Dummy user for demonstration
            # Add more users here if needed
        ]

    def get_user_by_username(self, username: str) -> User:
        for user in self.users:
            if user.username == username:
                return user
        return None

    def get_user_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def verify_password(self, user: User, password: str) -> bool:
        return user.password == password