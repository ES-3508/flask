from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .image_mapper import Base

class CustomerPinnedItems(Base):
    __tablename__ = 'customer_pinned_items'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    add_id = Column(Integer, ForeignKey('advertisement_header.header_id'))

    # Define relationships
    customer = relationship("Customer_Orm", back_populates="pinned_items")
    advertisement_header = relationship("AdvertisementHeader_Orm", back_populates="pinned_items")
