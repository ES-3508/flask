from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey, Date
from sqlalchemy.orm import registry, relationship

from .customer_mapper import Base



class AdvertisementPackage_Orm(Base):
    __tablename__ = 'advertisement_package'

    package_id = Column(Integer, primary_key=True)
    description = Column(String(100))
    number_of_add = Column(Integer)
    num_days = Column(Integer)
    is_active = Column(Boolean)
    price = Column(Integer)

    advertisement_headers_r = relationship('AdvertisementHeader_Orm', back_populates='advertisement_package_r')
