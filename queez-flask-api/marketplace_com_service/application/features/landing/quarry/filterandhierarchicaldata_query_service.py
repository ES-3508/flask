from .....infra.logger import log_exceptions
from .....application.utils.response_object  import ResponseObject
from .....application.utils.exception_collector import ExceptionCollector
from .....infrastructure.quary.filter_quary_repository import FilterQueryRepository
from .....application.features.landing.responce_objects.filterandhierarchicaldata_responce_object import FilterandhierarcHicaldataResponceObject
from .....domain.features.landing.valueobjects.id import Id
from .....application.features.landing.responce_objects.filter_responce_object import FilterResponseObject
from .....application.features.landing.responce_objects.hierarchicaldata_responce_object import HierarchicalDataResponseObject

class FilterandHierarchicaldataQueryService:
    def __init__(self, hierarchicaldata_query_service, filter_query_service):
        self.hierarchicaldata_query_service = hierarchicaldata_query_service
        self.filter_query_service = filter_query_service

    def get_all_data_and_filter(self):
        hierarchicaldatas = self.hierarchicaldata_query_service.get_all_data()
        filters = self.filter_query_service.get_all_filter()

        hierarchicaldata_response_objects = []
        filter_response_objects = []

        for hierarchical_data in hierarchicaldatas:
            hierarchicaldata_response_objects.append(HierarchicalDataResponseObject(
                id=hierarchical_data.id,
                name=hierarchical_data.name,
                level=hierarchical_data.level,
                parent=hierarchical_data.parent,
                is_active=hierarchical_data.is_active,
                category=hierarchical_data.category
            ))

        for filter in filters:
            filter_response_objects.append(FilterResponseObject(
                id=filter.id,
                name=filter.name,
                description=filter.description,
                ref_id=filter.ref_id,
                type=filter.type,
                is_active=filter.is_active,
                sql_statement=filter.sql_statement
            ))

        response_object = ResponseObject(is_error=False)
        response_object.add_payload({
            'hierarchicaldata': hierarchicaldata_response_objects,
            'filters': filter_response_objects
        })

        return response_object
