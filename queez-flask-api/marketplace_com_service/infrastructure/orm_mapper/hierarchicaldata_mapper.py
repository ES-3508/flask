from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from ..db_settings.mysql_database_orm import engine
from ..db_settings.mysql_database_orm import Base


# mapper_registry = registry()

# @mapper_registry.mapped
class HierarchicalDataOrm(Base):
    __tablename__ = 'hierarchical_data'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    level = Column(Integer)
    parent = Column(Integer)
    is_active = Column(Boolean)
    category = Column(String(100))
    # detailsss = relationship("DetailTable", back_populates="hierarchicaldata" )
    

    filterss = relationship("FilterOrm", back_populates="hierarchical_data")
# mapper_registry.metadata.create_all(db_context_orm.bind)

# class HierarchicalDataMapper:
#     @staticmethod
#     def create_table():
#         Base.metadata.create_all(db_context_orm.bind)



    