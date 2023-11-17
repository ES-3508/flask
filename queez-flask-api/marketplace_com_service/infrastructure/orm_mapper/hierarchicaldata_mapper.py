from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from ..db_settings.mysql_database_orm import db_context_orm

mapper_registry = registry()
Base=declarative_base()

@mapper_registry.mapped
class HierarchicalDataOrm:
    __tablename__ = 'hierarchical_data'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    level = Column(Integer)
    parent = Column(Integer)
    is_active = Column(Boolean)
    category = Column(String(100))
    
    # sys_keys = relationship('Sys_keyOrm', back_populates='hierarchical_data')


# mapper_registry.metadata.create_all(db_context_orm.bind)

class HierarchicalDataMapper:
    @staticmethod
    def create_table():
        mapper_registry.metadata.create_all(db_context_orm.bind)



    