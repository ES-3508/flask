from .....infra.logger import log_exceptions
from .....domain.features.customer_portal.aggregates.pinnedItems import PinnedItems
from .....domain.features.customer_portal.aggregates.savedfilters import SavedFilters
from .....domain.features.customer_portal.aggregates.customerdetails import CustomerDetails

from .....application.utils.response_object import ResponseObject
from .....infrastructure.orm_mapper.pinned_items_mapper import CustomerPinnedItems
from .....infrastructure.orm_mapper.saved_filters_mapper import CustomerSavedFilters
from ..responce_objects.customerportal_responce_object import CustomerportalResponseObject

class CustomerportalCommandService:
    def __init__(self, customerportal_command_repository):
        self.customerportal_command_repository = customerportal_command_repository
    
    @log_exceptions
    def save_pinned_item(self, customer_id, add_id):
        pinned_item = CustomerPinnedItems(
            customer_id=customer_id,
            add_id=add_id
        )
        self.customerportal_command_repository.save_pinned_item(pinned_item)

        response_object = ResponseObject(is_error=False)
        return response_object
    
    
    @log_exceptions
    def save_saved_filter(self, customer_id, filter_id, value):
        saved_filter = CustomerSavedFilters(
            customer_id=customer_id,
            filter_id=filter_id,
            value=value
        )
        self.customerportal_command_repository.save_saved_filter(saved_filter)

        response_object = ResponseObject(is_error=False)
        return response_object


    @log_exceptions
    def save_customer_details(self, customer_id, name, sys_user_id):
        
        customer_details = CustomerDetails(customer_id=customer_id, name=name, sys_user_id=sys_user_id)
            # Assuming that save_customer_details method returns the saved customer details data
        self.customer_command_repository.save_customer_details(customer_details)
            
            # Assuming that get_customer_details_by_id method returns the saved customer details
        saved_customer_details = self.customer_query_repository.get_customer_details_by_id(customer_id)

            # Construct response object
        response_object = CustomerportalResponseObject(
            customer_id=saved_customer_details.customer_id,
            name=saved_customer_details.name,
            sys_user_id=saved_customer_details.sys_user_id
        )
            
        return response_object
    

