from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry, relationship
from sqlalchemy.ext.declarative import declarative_base

from .add_detail_mapper import Base

class ImageDetails_Orm(Base):
    __tablename__ = 'image_details'

    image_details_id = Column(Integer, primary_key=True)
    image_url = Column(String(200))
    transec_ref_id = Column(Integer, ForeignKey('advertisement_header.header_id'))
    
    advertisement_header = relationship('AdvertisementHeader_Orm', back_populates='image_details')
