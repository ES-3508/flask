
class UserCreateCommandService:
    def __init__(self, user_command_repository,user_quary_repository):
        self.user_command_repository = user_command_repository
        self.user_quary_repository = user_quary_repository

    def create_user_async(self, user_json):
        # Business logic for saving a user
        result=self.user_command_repository.create_user_async(user_json)
        return result
