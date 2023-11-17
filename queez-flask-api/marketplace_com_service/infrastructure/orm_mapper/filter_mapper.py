from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from ..db_settings.mysql_database_orm import db_context_orm

mapper_registry = registry()
Base1=declarative_base()

@mapper_registry.mapped
class FilterOrm:
    __tablename__ = 'filters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(100))
    ref_id = Column(Integer)
    type = Column(String(100))
    is_active = Column(Boolean)
    sql_statement = Column(String(250))
    
    # sys_key = relationship('Sys_keyOrm', back_populates='filters')
    # hierarchical_data = relationship('HierarchicalDataOrm', back_populates='filters')

# mapper_registry.metadata.create_all(db_context_orm.bind)

class FilterMapper:
    @staticmethod
    def create_table():
        mapper_registry.metadata.create_all(db_context_orm.bind)







    

