from .....infra.logger import log_exceptions
from .....application.utils.response_object  import ResponseObject
from ..responce_objects.customerportal_responce_object import CustomerportalResponseObject



class CustomerportalQueryService:
    def __init__(self, customerportal_query_repository):
        self.customerportal_query_repository = customerportal_query_repository

    def get_pinned_items_by_customer_id(self, customer_id):
        pinned_items = self.customerportal_query_repository.get_pinned_items_by_customer_id(customer_id)

        response_objects = [
            CustomerportalResponseObject(
                
                customer_id=item.customer_id,
                add_id=item.add_id
            )
            for item in pinned_items
        ]

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(response_objects)
        return response_object

    def get_saved_filters_by_customer_id(self, customer_id):
        saved_filters = self.customerportal_query_repository.get_saved_filters_by_customer_id(customer_id)
        response_objects=[]
        for item in saved_filters:
            response_objects.append(CustomerportalResponseObject(
                
                customer_id=item.customer_id,
                filter_id=item.filter_id,
                value=item.value
            )
            )
        

        response_object = ResponseObject(is_error=False)
        response_object.add_payload(response_objects)
        return response_object

    def get_customer_details_by_id(self, customer_id):
        customer_details = self.customerportal_query_repository.get_customer_details_by_id(customer_id)

        if customer_details:
            response_object = CustomerportalResponseObject(
                customer_id=customer_details.customer_id,
                name=customer_details.name,
                sys_user_id=customer_details.sys_user_id
            )
            return response_object
        else:
            return ResponseObject(is_error=True, message="Customer not found.")

   

        








