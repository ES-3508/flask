from ..application.features.user.command.identity_command_service import IdentityCommandService
from ..application.features.user.command.user_create_command_service import UserCreateCommandService



from ..infrastructure.command.user_command_repository import UserCommandRepository
from ..infrastructure.quary.user_quary_repository import UserQuaryRepository
from authentication_service.infrastructure.command.identity_repository import IdentityRepository


# Create instances of the required dependencies
user_create_comand_repository = UserCommandRepository()
user_quary_repository = UserQuaryRepository()

identity_command_repository = IdentityRepository()


# Instantiate the AuthService with the dependencies
identity_service = IdentityCommandService(user_quary_repository, identity_command_repository)
user_create_command_service = UserCreateCommandService(user_create_comand_repository,user_quary_repository)

