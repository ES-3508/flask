from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .filter_mapper import Base

class Sys_keyOrm(Base):
    __tablename__ = 'sys_keys'
    id = Column(Integer, primary_key=True)
    key = Column(String(100))
    description = Column(String(250))
    
    # hierarchical_data = relationship('HierarchicalDataOrm', back_populates='sys_keys')



    