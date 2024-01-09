from sqlalchemy import Column, Integer, Boolean, String, Float, ForeignKey, Date
from sqlalchemy.orm import registry, relationship
from .add_header_mapper import Base
# WorkflowHistory Table


class WorkflowHistory_Orm(Base):
    __tablename__ = 'workflow_history'

    workflow_history_id = Column(Integer, primary_key=True)
    transec_ref_id = Column(Integer, ForeignKey('advertisement_header.header_id'))
    advertisement_header_workflow_history = relationship('AdvertisementHeader_Orm', back_populates='workflow_history')
    state_id = Column(Integer)
    state = Column(String(100))
    transection_type = Column(String(100))