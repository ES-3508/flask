from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .pinned_items_mapper import Base

class CustomerSavedFilters(Base):
    __tablename__ = 'customer_saved_filters'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    filter_id = Column(Integer, ForeignKey('filters.id'))
    value = Column(String(200))

    # Define relationships
    customer_s = relationship("Customer_Orm", back_populates="customer")
    filter = relationship("FilterOrm", back_populates="saved_filters")
