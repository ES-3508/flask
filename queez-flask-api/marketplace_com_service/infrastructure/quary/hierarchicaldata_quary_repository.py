from dotenv import load_dotenv
from ...infra.logger import log_exceptions
from ...domain.features.landing.repositories.i_hierarchicaldata_quary_repository import IHierarchicalDataQueryRepository
from ...domain.features.landing.aggregates.hierarchical_Data import HierarchicalData
from ..orm_mapper.hierarchicaldata_mapper import HierarchicalDataOrm
from ..db_settings.mysql_database_orm import db_context_orm
from typing import List
from ..db_settings.mysql_database_orm import Session


load_dotenv()
class HierarchicalDataQueryRepository(IHierarchicalDataQueryRepository):
    def __init__(self):
        self.db = db_context_orm
        
    
    @log_exceptions
    def get_data_by_id(self, id: int) -> HierarchicalData:
            session = Session()
            data_entity = session.query(HierarchicalDataOrm).filter_by(id=id).first()
            session.close()

            if data_entity is not None:
                return HierarchicalData(data_entity.id, data_entity.name, data_entity.level, data_entity.parent,data_entity.is_active,data_entity.category)
            else:
                return None
            
    @log_exceptions
    def get_all_data(self) -> List[HierarchicalData]:
        session = Session()
        data_entities = session.query(HierarchicalDataOrm).all()
        session.close()

        return [HierarchicalData(data_entity.id, data_entity.name, data_entity.level, data_entity.parent,data_entity.is_active,data_entity.category) for data_entity in data_entities]            