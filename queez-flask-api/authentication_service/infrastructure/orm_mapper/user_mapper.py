from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from ...infrastructure.db_settings.mysql_database_orm import engine
from ...infrastructure.db_settings.mysql_database_orm import db_context_orm

# mapper_registry = registry()
# Base=declarative_base()

# class UserOrm(Base):
#     __tablename__ = 'sys_users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), nullable=False)
#     password = Column(String(100), nullable=False)
#     user_fullname = Column(String(100))
#     user_address = Column(String(100))
#     user_email = Column(String(100))
#     user_contact = Column(String(100))
#     user_role = Column(String(100))
from sqlalchemy.orm import registry

mapper_registry = registry()

@mapper_registry.mapped
class UserOrm:
    __tablename__ = 'sys_users'
    id: int = Column(Integer, primary_key=True)
    username: str = Column(String(50), nullable=False)
    password: str = Column(String(100), nullable=False)
    user_fullname: str = Column(String(100))
    user_address: str = Column(String(100))
    user_email: str = Column(String(100))
    user_contact: str = Column(String(100))
    user_role: str = Column(String(100))

# mapper_registry.metadata.create_all(db_context_orm.bind)

class UserMapper:
    @staticmethod
    def create_user_table():
        mapper_registry.metadata.create_all(db_context_orm.bind)
        # Base.metadata.create_all(bind=engine)
