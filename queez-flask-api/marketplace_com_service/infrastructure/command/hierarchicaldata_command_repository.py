from dotenv import load_dotenv
from ...infra.logger import log_exceptions
from ...domain.features.landing.repositories.i_hierarchicaldata_command_repository import IHierarchicalDataCommandRepository
from ...domain.features.landing.aggregates.hierarchical_Data import HierarchicalData
from ..orm_mapper.hierarchicaldata_mapper import HierarchicalDataOrm
from ..db_settings.mysql_database_orm import db_context_orm
from ..db_settings.mysql_database_orm import Session


load_dotenv()

class HierarchicalDataCommandRepository(IHierarchicalDataCommandRepository):
    def __init__(self):
        self.db = db_context_orm
    
    @log_exceptions
    def create_data(self, data: HierarchicalData) -> None:
        session = Session()
        data_entity = HierarchicalDataOrm(
            name=data.name,
            level=data.level,
            parent=data.parent,
            is_active=data.is_active,
            category=data.category
        )
        session.add(data_entity)
        session.commit()
        session.close()

    @log_exceptions
    def update_data(self, data_id: int, updated_data: HierarchicalData) -> None:
        session = Session()
        data_entity = session.query(HierarchicalDataOrm).filter_by(id=data_id).first()
        if data_entity is not None:
            data_entity.name = updated_data.name
            data_entity.level = updated_data.level
            data_entity.parent = updated_data.parent
            data_entity.is_active = updated_data.is_active
            data_entity.category = updated_data.category
            session.commit()
        session.close()

    @log_exceptions
    def delete_data(self, data_id: int) -> None:
        session = Session()
        data_entity = session.query(HierarchicalDataOrm).filter_by(id=data_id).first()
        if data_entity is not None:
            session.delete(data_entity)
            session.commit()
        session.close()
