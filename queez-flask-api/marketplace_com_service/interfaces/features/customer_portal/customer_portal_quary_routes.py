from flask import Blueprint
from flask import jsonify
import json

from ....application.utils.exception_collector import ExceptionCollector
from ...utils.response_object_encoder import ResponseObjectEncoder
from ...utils.error_responce import ErrorResponse
from authentication_service.infra.router_protector import token_required
from ....application.features.costomerportal.quarry.customerportal_query_service import CustomerportalQueryService
from ....application import customerportal_query_service

from flask import Blueprint, request, json

customerportal_query_routes = Blueprint('customerportal_query_routes', __name__)

@customerportal_query_routes.route('/get_pinned_items', methods=['GET'])
def get_pinned_items():
    customer_id = request.args.get('customer_id')

    if not customer_id:
        error_response = ErrorResponse()
        return json.dumps(error_response.add_payload(message="Customer ID is required."), cls=ResponseObjectEncoder)

    
    response_object = customerportal_query_service.get_pinned_items_by_customer_id(customer_id)

    response_dict = response_object.__dict__
    return json.dumps(response_dict, cls=ResponseObjectEncoder)

@customerportal_query_routes.route('/get_saved_filters', methods=['GET'])
def get_saved_filters():
    customer_id = request.args.get('customer_id')

    if not customer_id:
        error_response = ErrorResponse()
        return json.dumps(error_response.add_payload(message="Customer ID is required."), cls=ResponseObjectEncoder)

    
    response_object = customerportal_query_service.get_saved_filters_by_customer_id(customer_id)
    response_dict = response_object.__dict__
    return json.dumps(response_dict, cls=ResponseObjectEncoder)

@customerportal_query_routes.route('/get_customer_details', methods=['GET'])
def get_customer_details():
    customer_id = request.args.get('customer_id')

    if not customer_id:
        error_response = ErrorResponse()
        return json.dumps(error_response.add_payload(message="Customer ID is required."), cls=ResponseObjectEncoder)

    service = CustomerportalQueryService(customerportal_query_service)
    response_object = service.get_customer_details_by_id(customer_id)

    return json.dumps(response_object, cls=ResponseObjectEncoder)


        


