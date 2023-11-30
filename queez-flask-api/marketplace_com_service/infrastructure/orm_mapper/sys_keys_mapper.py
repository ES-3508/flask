from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from ..db_settings.mysql_database_orm import db_context_orm

mapper_registry = registry()
Base2=declarative_base()

@mapper_registry.mapped
class Sys_keyOrm:
    __tablename__ = 'sys_keys'
    id = Column(Integer, primary_key=True)
    key = Column(String(100))
    description = Column(String(250))
    
    # hierarchical_data = relationship('HierarchicalDataOrm', back_populates='sys_keys')


class Sys_key_Mapper:
    @staticmethod
    def create_table():
        mapper_registry.metadata.create_all(db_context_orm.bind)

    