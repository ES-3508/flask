import jwt
import os
import bcrypt
from dotenv import load_dotenv
from datetime import datetime, timedelta
from ...infra.logger import log_exceptions
from ...domain.features.user.repositories.i_identity_repository import IIdentityRepository 
from ...domain.features.user.aggregates.user import User
from ...domain.features.user.valueobjects.token import Token
from ...domain.features.user.valueobjects.password import Password


load_dotenv()
class IdentityRepository(IIdentityRepository):
    def __init__(self):
        self.secret_key = os.getenv('SECRET_KEY')
    
    @log_exceptions
    def generate_token(self, user:User):
        # JWT token generation logic
        expiration_time = datetime.utcnow() + timedelta(hours=1) 
        payload = {'user_id': user.id, 'username': user.username.Value}
        payload['exp'] = expiration_time
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    @log_exceptions
    def verify_token(self, token:Token):
            # Extract the token from the "Bearer" format
            # token = token.split('Bearer')[1]

            # JWT token verification logic
        payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
        return payload
    
    @log_exceptions
    def verify_password(self,user:User, password:Password):
        return True
        # stored_hashed_password = user.password.Value.encode('utf-8')
        # provided_password = self.encrypt_password(password)
        # result = bcrypt.checkpw(provided_password, stored_hashed_password)
        # if result:
        #     return True
        # else:
        #     return False
        
    @log_exceptions
    def encrypt_password(self, password:Password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.Value.encode('utf-8'), salt)
        return hashed_password

