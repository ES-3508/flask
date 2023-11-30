from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from ...domain.features.user.aggregates.user import User
from ...infrastructure.db_settings.mysql_database_orm import db_context_orm
from ...infrastructure.db_settings.mysql_database_async import db_context_async

from marketplace_com_service.infra.logger import log_exceptions
from ...infra.select_quary_runner import SelectQuaryRunner
from ...domain.features.user.repositories.i_user_query_repository import IUserQueryRepository
from ...domain.features.user.valueobjects.username import Username
from ...domain.features.user.valueobjects.full_name import FullName
from ...domain.features.user.valueobjects.address import Address
from ...domain.features.user.valueobjects.contact import Contact
from ...domain.features.user.valueobjects.email import Email
from ...domain.features.user.valueobjects.password import Password
from ...domain.features.user.valueobjects.user_role import UserRole
from ...infrastructure.orm_mapper.user_mapper import UserOrm

class UserQuaryRepository(IUserQueryRepository):
    def __init__(self):
        self.orm_db_context = db_context_orm.bind
        self.Session_sync = sessionmaker(bind=self.orm_db_context, expire_on_commit=False)  # Added expire_on_commit=False

        self.async_db_context = db_context_async.bind
        self.async_engine = create_async_engine(self.async_db_context.url)


    @log_exceptions
    def get_user_by_username_sql(self, username: Username) -> User:
        quary_filter_values_array = []
        quary_filter_values_array.append(username.Value)
        user_data = SelectQuaryRunner.fetch_run_sql_select_query_string('get_user_by_username',quary_filter_values_array)

        if user_data:
        # Extract the column values from the fetched data
            id, username,password,  user_fullname, user_email,user_address, user_contact, user_role = user_data

        # Create a new instance of the User class and populate its properties
            user = User(
                id=id,
                username=Username(username),
                password = Password(password),
                user_fullname = FullName(user_fullname),
                user_address = Address(user_address),
                user_email = Email(user_email),
                user_contact =Contact( user_contact),
                user_role = UserRole(user_role)
            )
        # Retrieve the user from the database by username
        # user = self.db.query(User).filter_by(username=username).first()
            return user
        else:
            return None

    @log_exceptions
    def get_user_by_username_orm(self, username: Username) -> User:
        with self.Session_sync() as session:
            user_data = session.query(UserOrm).filter(UserOrm.username == username.Value).first()

        if user_data:
        # Create a new instance of the User class and populate its properties
            user = User(
                id=user_data.id,
                username=Username(user_data.username),
                password = Password(user_data.password),
                user_fullname = FullName(user_data.user_fullname),
                user_address = Address(user_data.user_address),
                user_email = Email(user_data.user_email),
                user_contact =Contact( user_data.user_contact),
                user_role = UserRole(user_data.user_role)
            )
        # Retrieve the user from the database by username
        # user = self.db.query(User).filter_by(username=username).first()
            return user
        else:
            return None
       
    @log_exceptions
    async def get_user_by_username_async(self, username: Username) -> User:
       async with self.async_session() as session:
            user_data = await session.execute(UserOrm.__table__.select().where(UserOrm.username == username.Value))
            user_data = user_data.fetchone()

            if user_data:
                user = User(
                    id=user_data.id,
                    username=Username(user_data.username),
                    password=Password(user_data.password),
                    user_fullname=FullName(user_data.user_fullname),
                    user_address=Address(user_data.user_address),
                    user_email=Email(user_data.user_email),
                    user_contact=Contact(user_data.user_contact),
                    user_role=UserRole(user_data.user_role)
                )
                return user
            else:
                return None
       
    

        