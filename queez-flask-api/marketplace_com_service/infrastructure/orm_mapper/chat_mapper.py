from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import registry, relationship
from datetime import datetime
from .customer_mapper import Base 

class ChatOrm(Base):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
    receiver_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
    message = Column(String(255), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Define relationships
    sender = relationship("Customer_Orm", back_populates="sent_chats")
    receiver = relationship("Customer_Orm", back_populates="received_chats")
