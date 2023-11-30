from dotenv import load_dotenv
from ...infra.logger import log_exceptions
from ...domain.features.landing.repositories.i_filter_command_repository import IFilterCommandRepository
from ...domain.features.landing.aggregates.filters import Filter
from ..orm_mapper.filter_mapper import FilterOrm
from ..db_settings.mysql_database_orm import db_context_orm
from ..db_settings.mysql_database_orm import Session

load_dotenv()

class FilterCommandRepository(IFilterCommandRepository):
    def __init__(self):
        self.db = db_context_orm
    
    @log_exceptions
    def create_filter(self, filter_data: Filter) -> None:
        session = Session()
        filter_entity = FilterOrm(
            id=filter_data.id,
            name=filter_data.name,
            description=filter_data.description,
            is_active=filter_data.is_active,
            ref_id=filter_data.ref_id,
            type=filter_data.type,
            sql_statement=filter_data.sql_statement
            
            
        )
        session.add(filter_entity)
        session.commit()
        session.close()

    @log_exceptions
    def update_filter(self, filter_id: int, updated_filter_data: Filter) -> None:
        session = Session()
        filter_entity = session.query(FilterOrm).filter_by(id=filter_id).first()
        if filter_entity is not None:
            filter_entity.code = updated_filter_data.code
            filter_entity.name = updated_filter_data.name
            filter_entity.category = updated_filter_data.category
            filter_entity.is_active = updated_filter_data.is_active
            session.commit()
        session.close()

    @log_exceptions
    def delete_filter(self, filter_id: int) -> None:
        session = Session()
        filter_entity = session.query(FilterOrm).filter_by(id=filter_id).first()
        if filter_entity is not None:
            session.delete(filter_entity)
            session.commit()
        session.close()
