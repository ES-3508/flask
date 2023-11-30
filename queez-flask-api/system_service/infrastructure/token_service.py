import jwt
import os
from dotenv import load_dotenv

load_dotenv();
class TokenService:
    def __init__(self):
        self.secret_key = os.getenv('SECRET_KEY')

    def generate_token(self, user):
        # JWT token generation logic
        payload = {'user_id': user.id, 'username': user.username}
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def verify_token(self, token):
        try:
            # Extract the token from the "Bearer" format
            token = token.split('Bearer ')[1]

            # JWT token verification logic
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            # Handle expired token error
            return None
        except jwt.InvalidTokenError:
            # Handle invalid token error
            return None
