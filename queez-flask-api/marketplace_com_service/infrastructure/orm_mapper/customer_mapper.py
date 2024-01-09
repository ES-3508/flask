from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey, Date 
from sqlalchemy.orm import registry, relationship
from .sys_keys_mapper import Base

class Customer_Orm(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    sys_user_id = Column(Integer)

    advertisement_headers_customer = relationship('AdvertisementHeader_Orm', back_populates='customer',
                                         foreign_keys='AdvertisementHeader_Orm.publisher_id')
    
    pinned_items = relationship("CustomerPinnedItems", back_populates="customer",foreign_keys='CustomerPinnedItems.customer_id')
    customer = relationship("CustomerSavedFilters", back_populates="customer_s")
    
    sent_chats = relationship("ChatOrm", back_populates="sender")
    received_chats = relationship("ChatOrm", back_populates="receiver")