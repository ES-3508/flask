from dotenv import load_dotenv
from ...infra.logger import log_exceptions
from ...domain.features.landing.repositories.i_filter_quary_repository import IFilterQueryRepository
from ...domain.features.landing.aggregates.filters import Filter
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..db_settings.mysql_database_orm import db_context_orm
from ..orm_mapper.filter_mapper import FilterOrm
from ..db_settings.mysql_database_orm import Session



class FilterQueryRepository(IFilterQueryRepository):
    def __init__(self):
        self.db = db_context_orm
        
    @log_exceptions
    def get_filter_by_code(self, code: str) -> Filter:
        session = Session()
        filter_entity = session.query(FilterOrm).filter_by(code=code).first()
        session.close()

        if filter_entity is not None:
            return Filter(filter_entity.code, filter_entity.name, filter_entity.level, filter_entity.parent,filter_entity.Type)
        else:
            return None

    @log_exceptions
    def get_all_filter(self) -> List[Filter]:
            session = Session()
            filter_entities = session.query(FilterOrm).all()
            session.close()

            return [Filter(filter_entity.id, filter_entity.name, filter_entity.description, filter_entity.ref_id, filter_entity.type, filter_entity.is_active, filter_entity.sql_statement ) for filter_entity in filter_entities]