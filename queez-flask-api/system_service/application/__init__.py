from system_service.application.auth_service import AuthService
from infrastructure.token_service import TokenService
from infrastructure.user_repository import UserRepository


# Create instances of the required dependencies
user_repository = UserRepository()
token_service = TokenService()

# Instantiate the AuthService with the dependencies
auth_service = AuthService(user_repository, token_service)
