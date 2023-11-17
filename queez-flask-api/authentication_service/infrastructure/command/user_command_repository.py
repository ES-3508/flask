from ...domain.features.user.repositories.i_user_command_repository import IUserCommandRepository
from sqlalchemy import text
from ...infrastructure.db_settings.mysql_database_orm import db_context_orm

from marketplace_com_service.infra.logger import log_exceptions
from ...infra.select_quary_runner import SelectQuaryRunner
from ...infra.mongo_quary_runner import MongoDRunner
from ...infra.common_method import CommonMethod

@log_exceptions
class UserCommandRepository(IUserCommandRepository):
    def __init__(self):
        self.db = db_context_orm  # Database context
    
    def create_user_async(self, user_json: str):
        # Save the user to the mongo db
        # user_json=CommonMethod.convert_object_to_json(user)
        MongoDRunner.create_user_async('user_collection',user_json)
        # Save the user to the database
        # self.db.add(user)()
        # self.db.commit()
        return True
        