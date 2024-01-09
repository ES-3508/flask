from flask import Blueprint, request, jsonify, current_app
from ....application.features.advertisement.quarry.advertisement_query_service import AdvertisementQueryService

from ....application import advertisement_query_service

from ....application import filter_query_service
from ...utils.response_object_encoder import ResponseObjectEncoder
from flask import jsonify
import json
from ...utils.error_responce import ErrorResponse

advertisement_query_routes = Blueprint('advertisement_query_routes', __name__)

@advertisement_query_routes.route('/get_advertisement_by_id/<int:advertisement_id>', methods=['GET'])
def get_advertisement_by_id_endpoint(advertisement_id):
    print("eee")
    response_object = advertisement_query_service.get_advertisement_by_id(advertisement_id)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)

    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)
 


@advertisement_query_routes.route('/get_advertisement_by_filter', methods=['GET'])
def get_advertisement_by_filter_endpoint():
    
        # Get filter_id and value from request parameters
    # Get filter_id and value from request parameters
    filter_id = request.args.get('filter_id')
    value = request.args.get('value')
    # customer_id = request.args.get('customer_id')
    customer_id = 2
        # Validate filter_id and value
    if not filter_id or not value:
        raise ValueError("Both filter_id and value are required.")

        # Convert filter_id to integer if needed
    filter_id = int(filter_id)

        # Call the service method to get advertisements by filter_id and value
    response_object = advertisement_query_service.get_advertisement_by_filter_id_and_value(filter_id, value, customer_id)

    

        # Return the JSON response
    return json.dumps(response_object, cls=ResponseObjectEncoder)

      
      

# @advertisement_query_routes.route('/get_all_advertisements', methods=['GET'])
# def get_all_advertisements():
#     # service = AdvertisementQueryService(advertisement_query_service)
#     response_object = advertisement_query_service.get_all_advertisements()

#     if response_object:
#         return json.dumps(response_object, cls=ResponseObjectEncoder)

#     error_response = ErrorResponse()
#     return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)




