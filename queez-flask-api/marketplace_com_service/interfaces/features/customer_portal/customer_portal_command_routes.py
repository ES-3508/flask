from flask import Blueprint, request, jsonify
from ....application.features.landing.command.filter_command_service import FilterCommandService
from ....application.features.landing.command.hierarchicaldata_command_service import HierarchicalDataCommandService

from ....application import filter_Command_Service
from ....application import hierarchicalData_command_Service

from ....application.utils.exception_collector import ExceptionCollector
from ...utils.response_object_encoder import ResponseObjectEncoder
from flask import jsonify
import json
from ...utils.error_responce import ErrorResponse

from flask import Blueprint, request, json
from ....application import customerportal_command_service


customerportal_command_routes = Blueprint('customerportal_command_routes', __name__)

@customerportal_command_routes.route('/save_pinned_item', methods=['POST'])
def save_pinned_item():
    data = request.json

    customer_id = data.get('customer_id')
    add_id = data.get('add_id')

    if not customer_id or not add_id:
        error_response = ErrorResponse()
        return json.dumps(error_response.add_payload(message="Customer ID and Add ID are required."), cls=ResponseObjectEncoder)

    
    response_object = customerportal_command_service.save_pinned_item(customer_id, add_id)

    response_dict = response_object.__dict__
    return json.dumps(response_dict, cls=ResponseObjectEncoder)

@customerportal_command_routes.route('/save_saved_filter', methods=['POST'])
def save_saved_filter():
    data = request.json

    customer_id = data.get('customer_id')
    filter_id = data.get('filter_id')
    value = data.get('value')

    if not customer_id or not filter_id or not value:
        error_response = ErrorResponse()
        return json.dumps(error_response.add_payload(message="Customer ID, Filter ID, and Value are required."), cls=ResponseObjectEncoder)

    
    response_object = customerportal_command_service.save_saved_filter(customer_id, filter_id, value)

    response_dict = response_object.__dict__
    return json.dumps(response_dict, cls=ResponseObjectEncoder)
