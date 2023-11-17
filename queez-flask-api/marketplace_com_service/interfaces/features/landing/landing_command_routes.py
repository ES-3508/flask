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

landing_command_routes = Blueprint('landing_command_routes', __name__)

@landing_command_routes.route('/create_filter_data', methods=['POST'])
def create_filter_data():
    data = request.json  # Assuming the request contains data for creating a filter
    
    service = FilterCommandService(filter_Command_Service)
    response_object = service.create_filter(data)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)

@landing_command_routes.route('/update_filter_data/<int:id>', methods=['PUT'])
def update_filter_data(id):
    updated_data = request.json  # Assuming the request contains updated data for a filter
    service = FilterCommandService(filter_Command_Service)
    response_object = service.update_filter(id, updated_data)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)

@landing_command_routes.route('/delete_filter_data/<int:id>', methods=['DELETE'])
def delete_filter_data(id):
    service = FilterCommandService(filter_Command_Service)
    response_object = service.delete_filter(id)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)

@landing_command_routes.route('/create_hierarchical_data', methods=['POST'])
def create_hierarchical_data():
    data = request.json  # Assuming the request contains data for creating hierarchical data
    service = HierarchicalDataCommandService(hierarchicalData_command_Service)
    response_object = service.create_data(data)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)

@landing_command_routes.route('/update_hierarchical_data/<int:id>', methods=['PUT'])
def update_hierarchical_data(id):
    updated_data = request.json  # Assuming the request contains updated data for hierarchical data
    service = HierarchicalDataCommandService(hierarchicalData_command_Service)
    response_object = service.update_data(id, updated_data)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)

@landing_command_routes.route('/delete_hierarchical_data/<int:id>', methods=['DELETE'])
def delete_hierarchical_data(id):
    service = HierarchicalDataCommandService(hierarchicalData_command_Service)
    response_object = service.delete_data(id)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)
