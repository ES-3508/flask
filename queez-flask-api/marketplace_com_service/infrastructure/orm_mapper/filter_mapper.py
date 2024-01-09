from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .hierarchicaldata_mapper import HierarchicalDataOrm

from ..db_settings.mysql_database_orm import engine
from .hierarchicaldata_mapper import Base

class FilterOrm(Base):
    __tablename__ = 'filters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(100))
    ref_id = Column(ForeignKey('hierarchical_data.id'))
    type = Column(String(100))
    is_active = Column(Boolean)
    sql_statement = Column(String(250))
    
    hierarchical_data = relationship("HierarchicalDataOrm", back_populates="filterss")
    advertisement_details = relationship("AdvertisementDetails_Orm", back_populates="filters", cascade="all, delete-orphan")
    saved_filters = relationship("CustomerSavedFilters", back_populates="filter",foreign_keys='CustomerSavedFilters.filter_id')
    # detailss = relationship("DetailTable", back_populates="filter")
    
# class FilterMapper:
#     @staticmethod
#     def create_table():
#         Base.metadata.create_all(db_context_orm.bind)







    

