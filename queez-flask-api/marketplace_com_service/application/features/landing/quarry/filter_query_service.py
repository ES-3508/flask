from .....infra.logger import log_exceptions
from .....application.utils.response_object  import ResponseObject
from .....application.utils.exception_collector import ExceptionCollector
from .....infrastructure.quary.filter_quary_repository import FilterQueryRepository
from .....application.features.landing.responce_objects.filter_responce_object import FilterResponseObject
from .....domain.features.landing.valueobjects.id import Id



class FilterQueryService:
    def __init__(self,filter_query_service,):
        self.filter_query_service = filter_query_service

    

    def get_filter_by_id(self, id):
        
        id_value_obj=Id(id)
        
        filter_data = self.filter_query_service.get_filter_by_id(id_value_obj)
        filter_response_object = FilterResponseObject(
            id=filter_data.id,
            name=filter_data.name,
            description=filter_data.description,
            # ref_id=filter_data.ref_id,
            # type=filter_data.type,
            # is_active=filter_data.is_active,
            # sql_statement=filter_data.sql_statement
        )

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(filter_response_object)

        return response_object

    def get_all_filter(self):
        filters = self.filter_query_service.get_all_filter()
        filter_response_objects = []
       
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
        response_object.add_payload(filter_response_objects)
        return filter_response_objects


   

        








