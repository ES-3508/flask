from flask import Blueprint
from flask import jsonify
import json
from ....application.features.landing.quarry.hierarchical_data_query_service import HierarchicalDataQueryService
from ....application.features.landing.quarry.filter_query_service import FilterQueryService
from ....application import hierarchicaldata_query_service
from ....application import filter_query_service
from ....application.utils.exception_collector import ExceptionCollector
from ...utils.response_object_encoder import ResponseObjectEncoder
from ...utils.error_responce import ErrorResponse
from authentication_service.infra.router_protector import token_required





landing_quary_routes = Blueprint('landing_quary_routes', __name__)


@landing_quary_routes.route('/get_all_hierarchical_data', methods=['GET'])
@token_required
def get_all_hierarchical_data():
    service = HierarchicalDataQueryService(hierarchicaldata_query_service)
    response_object = service.get_all_data()
    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)
    
    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)




@landing_quary_routes.route('/get_element_by_id/<int:id>', methods=['GET'])

def get_element_by_id(id):
    # service = HierarchicalDataQueryService(hierarchicaldata_query_service) 
    response_object = hierarchicaldata_query_service.get_data_by_id(id)
    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)
    
    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)



@landing_quary_routes.route('/get_all_filter_data', methods=['GET'])

def get_all_filter_data():
    service = FilterQueryService(filter_query_service)
    response_object = service.get_all_filter()
    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)
    
    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)



from ....application.features.landing.quarry.filterandhierarchicaldata_query_service import FilterandHierarchicaldataQueryService


@landing_quary_routes.route('/get_all', methods=['GET'])
def get_all():
    
    service_data = FilterandHierarchicaldataQueryService(hierarchicaldata_query_service,filter_query_service)
        
    response_object = service_data.get_all_data_and_filter()
   
        
    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)
    
    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)

        


