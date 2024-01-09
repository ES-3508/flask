from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey, Date
from sqlalchemy.orm import registry, relationship
from sqlalchemy.ext.declarative import declarative_base
# from .filter_mapper import FilterOrm

from .add_pkg_mapper import Base



class AdvertisementHeader_Orm(Base):
    __tablename__ = 'advertisement_header'

    header_id = Column(Integer, primary_key=True)
    
    # Specify the foreign key explicitly for publisher_id
    publisher_id = Column(Integer, ForeignKey('customer.customer_id'))
    customer = relationship('Customer_Orm', back_populates='advertisement_headers_customer', foreign_keys=[publisher_id])
    
    time_period = Column(Integer)
    is_active = Column(Boolean)
    coordinates = Column(String(100))
    
    # Specify the foreign key explicitly for wf_state_id
    wf_state = Column(String(100))
    # workflow_history = relationship('WorkflowHistory', back_populates='advertisement_header')
    
    date = Column(String(100))
    
    # Specify the foreign key explicitly for user_id
    user_id = Column(Integer, ForeignKey('customer.customer_id'))
    
    # Specify the foreign key explicitly for package_id
    package_id = Column(Integer, ForeignKey('advertisement_package.package_id'))
    advertisement_package_r = relationship('AdvertisementPackage_Orm', back_populates='advertisement_headers_r', foreign_keys=[package_id])

    
    workflow_history = relationship("WorkflowHistory_Orm", back_populates="advertisement_header_workflow_history")

    # One-to-Many Relationship: One AdvertisementHeader can have multiple AdvertisementDetails
    advertisement_details = relationship("AdvertisementDetails_Orm", back_populates="advertisement_header", cascade="all, delete-orphan")

    # One-to-Many Relationship: One AdvertisementHeader can have multiple ImageDetails
    image_details = relationship("ImageDetails_Orm", back_populates="advertisement_header", cascade="all, delete-orphan")
    
    pinned_items = relationship("CustomerPinnedItems", back_populates="advertisement_header")






