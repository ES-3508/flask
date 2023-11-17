from .....infra.logger import log_exceptions
from .....application.utils.response_object import ResponseObject
from .....application.features.landing.responce_objects.filter_responce_object import FilterResponseObject

class FilterCommandService:
    def __init__(self, filter_command_service):
        self.filter_command_service = filter_command_service
    
    @log_exceptions
    def create_filter(self, filter_data):
        # Assuming that self.filter_command_service.create_filter returns the created filter data
        created_filter = self.filter_command_service.create_filter(filter_data)

        filter_response_object = FilterResponseObject(
            id=created_filter.id,
            name=created_filter.name,
            description=created_filter.description,
            ref_id=created_filter.ref_id,
            type=created_filter.type,
            is_active=created_filter.is_active,
            sql_statement=created_filter.sql_statement
        )

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(filter_response_object)

        return response_object

    @log_exceptions
    def update_filter(self, filter_id, updated_filter_data):
        # Assuming that self.filter_command_service.update_filter returns the updated filter data
        updated_filter = self.filter_command_service.update_filter(filter_id, updated_filter_data)

        filter_response_object = FilterResponseObject(
            id=updated_filter.id,
            name=updated_filter.name,
            description=updated_filter.description,
            ref_id=updated_filter.ref_id,
            type=updated_filter.type,
            is_active=updated_filter.is_active,
            sql_statement=updated_filter.sql_statement
        )

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(filter_response_object)

        return response_object

    @log_exceptions
    def delete_filter(self, filter_id):
        # Assuming that self.filter_command_service.delete_filter returns a success indicator
        success = self.filter_command_service.delete_filter(filter_id)

        response_object = ResponseObject(is_error=not success)

        return response_object
