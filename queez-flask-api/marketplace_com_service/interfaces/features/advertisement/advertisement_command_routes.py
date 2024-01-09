from flask import Blueprint, request, jsonify
from ....application.features.advertisement.command.advertisement_command_service import AdvertisementCommandService
from ....domain.features.adverticement.aggregates.adverticement import AdvertisementHeader
from ....domain.features.adverticement.aggregates.adverticementpackage import AdvertisementPackage

from ....domain.features.adverticement.aggregates.advertisementdetails import AdvertisementDetails
from ....domain.features.adverticement.aggregates.imageurl import ImageDetails
from ....domain.features.adverticement.aggregates.workflow import WorkflowHistory
from ....domain.features.adverticement.aggregates.customer import Customer
from ....application import advertisement_command_service

from ....application.utils.exception_collector import ExceptionCollector
from ...utils.response_object_encoder import ResponseObjectEncoder
from flask import jsonify
import json
from ...utils.error_responce import ErrorResponse

advertisement_command_routes = Blueprint('advertisement_command_routes', __name__)

@advertisement_command_routes.route('/create_advertisement', methods=['POST'])
def create_advertisement():
    
        # Parse request data, assuming it's in JSON format
    request_data = request.get_json()

        # Extract data for AdvertisementHeader, AdvertisementPackage, AdvertisementDetails, ImageDetails, WorkflowHistory, Customer
    header_data = request_data.get('header')
    package_data = request_data.get('package')
    details_data = request_data.get('details')
    image_data = request_data.get('image')
    history_data = request_data.get('history')
    customer_data = request_data.get('customer')

    advertisement_header = AdvertisementHeader(**header_data)
    advertisement_package = AdvertisementPackage(**package_data)
    advertisement_details = AdvertisementDetails(**details_data)
    image_details = ImageDetails(**image_data)
    workflow_history = WorkflowHistory(**history_data)
    customer = Customer(**customer_data)

        # Call the service to create the advertisement
    response_object = advertisement_command_service.create_advertisement(customer,advertisement_header, advertisement_package, advertisement_details, image_details, workflow_history
        )
    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)
    




@advertisement_command_routes.route('/update_advertisement/<int:id>', methods=['PUT'])
def update_advertisement(id):
    updated_data = request.json  # Assuming the request contains updated data for an advertisement
    service = AdvertisementCommandService(advertisement_command_service)
    response_object = service.update_advertisement(id, updated_data)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)

@advertisement_command_routes.route('/delete_advertisement/<int:id>', methods=['DELETE'])
def delete_advertisement(id):
    service = AdvertisementCommandService(advertisement_command_service)
    response_object = service.delete_advertisement(id)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)
