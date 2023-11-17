from flask import Blueprint, request, jsonify, current_app

from ....domain.features.user.aggregates.user import User

auth_quary_routes = Blueprint('auth_quary_routes', __name__)

@auth_quary_routes.get('/getuserbyid')
def getuserbyid():
    username = request.json.get('userid')
    return jsonify({'message': 'Invalid username or password'}), 401
