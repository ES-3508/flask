
from .....infra.logger import log_exceptions
from .....application.utils.response_object  import ResponseObject
from .....application.features.landing.responce_objects.hierarchicaldata_responce_object import HierarchicalDataResponseObject

class HierarchicalDataQueryService:
    def __init__(self,hierarchicaldata_query_service):
        self.hierarchicaldata_query_service = hierarchicaldata_query_service

    
    def get_all_data(self):
        hierarchicaldatas = self.hierarchicaldata_query_service.get_all_data()
        hierarchicaldata_response_objects = []
       
        for hierarchical_data in hierarchicaldatas:
            hierarchicaldata_response_objects.append(HierarchicalDataResponseObject(
                id=hierarchical_data.id,
                name=hierarchical_data.name,
                level = hierarchical_data.level,
                parent = hierarchical_data.parent,
                is_active = hierarchical_data.is_active,
                category = hierarchical_data.category
            ))
        response_object = ResponseObject(is_error=False)
        response_object.add_payload(hierarchicaldata_response_objects)
        return hierarchicaldata_response_objects
    

    def get_data_by_id(self, id):
        hierarchical_data = self.hierarchicaldata_query_service.get_data_by_id(id)

        if hierarchical_data is None:
           
            response_object = ResponseObject(is_error=True)
            
            return None

        hierarchicaldata_response_object = HierarchicalDataResponseObject(
            id=hierarchical_data.id,
            name=hierarchical_data.name,
            level=hierarchical_data.level,
            parent=hierarchical_data.parent,
            is_active=hierarchical_data.is_active,
            category=hierarchical_data.category
        )

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(hierarchicaldata_response_object)

        return response_object
