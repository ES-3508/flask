from .....infra.logger import log_exceptions
from .....application.utils.response_object import ResponseObject
from .....application.features.landing.responce_objects.hierarchicaldata_responce_object import HierarchicalDataResponseObject

class HierarchicalDataCommandService:
    def __init__(self, hierarchicalData_command_service):
        self.hierarchicalData_command_service = hierarchicalData_command_service
    
    @log_exceptions
    def create_data(self, data):
        # Assuming that self.hierarchicalData_command_service.create_data returns the created data
        created_data = self.hierarchicalData_command_service.create_data(data)

        hierarchical_data_response_object = HierarchicalDataResponseObject(
            id=created_data.id,
            name=created_data.name,
            level=created_data.level,
            parent=created_data.parent,
            is_active=created_data.is_active,
            category=created_data.category
        )

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(hierarchical_data_response_object)

        return response_object

    @log_exceptions
    def update_data(self, data_id, updated_data):
        # Assuming that self.hierarchicalData_command_service.update_data returns the updated data
        updated_data = self.hierarchicalData_command_service.update_data(data_id, updated_data)

        hierarchical_data_response_object = HierarchicalDataResponseObject(
            id=updated_data.id,
            name=updated_data.name,
            level=updated_data.level,
            parent=updated_data.parent,
            is_active=updated_data.is_active,
            category=updated_data.category
        )

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(hierarchical_data_response_object)

        return response_object

    @log_exceptions
    def delete_data(self, data_id):
        # Assuming that self.hierarchicalData_command_service.delete_data returns a success indicator
        success = self.hierarchicalData_command_service.delete_data(data_id)

        response_object = ResponseObject(is_error=not success)

        return response_object
