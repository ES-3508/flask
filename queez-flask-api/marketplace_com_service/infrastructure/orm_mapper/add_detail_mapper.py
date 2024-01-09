from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey, Date
from sqlalchemy.orm import registry, relationship
from sqlalchemy.ext.declarative import declarative_base
from ..orm_mapper.filter_mapper import FilterOrm


# from ..orm_mapper.add_header_mapper import AdvertisementHeader
from ..db_settings.mysql_database_orm import Base


class AdvertisementDetails_Orm(Base):
    __tablename__ = 'advertisement_details'

    advertisement_details_id = Column(Integer, primary_key=True)
    add_id = Column(Integer)
    filter_id = Column(Integer, ForeignKey('filters.id'))
    value = Column(String(100))
    header_id = Column(Integer, ForeignKey('advertisement_header.header_id'))
    advertisement_header = relationship('AdvertisementHeader_Orm', back_populates='advertisement_details')
    filters = relationship('FilterOrm', back_populates='advertisement_details')



