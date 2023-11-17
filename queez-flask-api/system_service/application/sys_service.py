
class SysService:
    def __init__(self, user_repository, token_service):
        self.user_repository = user_repository
        self.token_service = token_service

    def authenticate(self, username, password):
        # Business logic for user authentication
        user = self.user_repository.get_user_by_username(username)
        if user and self.user_repository.verify_password(user,password):
            # Generate JWT token
            token = self.token_service.generate_token(user)
            user.token=token
            return user

        return None

    def decode_token(self, token):
        payload = self.token_service.verify_token(token)
        return payload
