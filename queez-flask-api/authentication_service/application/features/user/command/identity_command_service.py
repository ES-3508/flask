# from .....infra.logger import log_exceptions
# from authentication_service.infra.logger import log_exceptions
from marketplace_com_service.infra.logger import log_exceptions
from .....domain.features.user.enums.user_message import UserMessages
from .....domain.features.user.valueobjects.username import Username
from .....domain.features.user.valueobjects.password import Password
from .....application.features.user.responce_objects.user_responce_object import UserResponceObjct
from .....application.utils.response_object import ResponseObject
from ....utils.exception_collector import ExceptionCollector
from .....domain.features.user.aggregates.user import User

class IdentityCommandService:
    def __init__(self, user_quary_repository, identity_repository):
        self.user_quary_repository=user_quary_repository
        self.identity_repository = identity_repository
    
    # @log_exceptions
    # def  authenticate(self, username, password):
    #     # Business logic for user authentication
    #     username_value_obj=Username(username)
    #     password_value_obj=Password(password)

    #     user = self.user_quary_repository.get_user_by_username_sql(username_value_obj)
    #     if user is None:
    #         raise ValueError(UserMessages.USER_NOT_FOUND_MSG)
        
    #     # user = self.user_quary_repository.get_user_by_username_async(username_value_obj)
    #     # if user is None:
    #     #     raise ValueError(UserMessages.USER_NOT_FOUND_MSG)


    #     password_verification = self.identity_repository.verify_password(user,password_value_obj)
    #     if password_verification is False:
    #         raise ValueError(UserMessages.INVALID_PASSWORD_MSG)


    #     # Generate token
    #     token = self.identity_repository.generate_token(user)
    #     result =UserResponceObjct(user.id,user.username.Value,token)
    #     responce_object = ResponseObject(True,result)
    #     responce_object.add_payload(result)
    #     return responce_object







    @log_exceptions
    def  authenticate(self, username, password):
        # Business logic for user authentication
        username_value_obj=Username(username)
        password_value_obj=Password(password)

        username = Username("sample_username")
        password = Password("Jason@ui-lib.com123")
      

# Create a User object
        user = User(id=1, username=username,  password=password)


        # Generate token
        token = self.identity_repository.generate_token(user)
        result =UserResponceObjct(user.id,user.username.Value,token)
        responce_object = ResponseObject(False,result)
        responce_object.add_payload(result)
        return responce_object

# Assuming you have the necessary classes (Username, FullName, Address, Contact, Email, Password, Token, UserRole) defined

# Create instances of the related classes





