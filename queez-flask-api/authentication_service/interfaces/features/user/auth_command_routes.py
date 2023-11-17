from flask import Blueprint, request, jsonify, current_app
import json
from ....application import identity_service
from ....application import user_create_command_service
from ....infra.router_protector import token_required
from ....interfaces.utils.response_object_encoder import ResponseObjectEncoder
from ....interfaces.utils.error_responce import ErrorResponse

from ....infra.logger import log_exceptions

auth_command_routes = Blueprint('auth_command_routes', __name__)

@auth_command_routes.post('/login')
@log_exceptions
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    response_object = identity_service.authenticate(username, password)

    if response_object:
        return json.dumps(response_object, cls=ResponseObjectEncoder)
    
    error_response = ErrorResponse()
    return json.dumps(error_response.add_payload(), cls=ResponseObjectEncoder)




@auth_command_routes.get('/protected')
@token_required
def protected():
    return jsonify({'message': 'Protected resource'})

@auth_command_routes.post('/saveuser')
def create_euser():
    user_json  = {
                'username': "kanchan",
                'password': "password",
                'token': "token",
                'user_fullname': "user_fullname",
            }
    
    result =user_create_command_service.create_user_async(user_json)

    if result:
        return jsonify({'message': result})

    return jsonify({'message': result}), 401
