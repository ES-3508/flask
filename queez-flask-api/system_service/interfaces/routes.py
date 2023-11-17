import os
from flask import Blueprint, request, jsonify, current_app
from application import auth_service

auth_app = Blueprint('auth_app', __name__)
@auth_app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = auth_service.authenticate(username, password)

    if user.token:
        return jsonify({'user': user.__dict__})

    return jsonify({'message': 'Invalid username or password'}), 401

@auth_app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Missing token'}), 401


    payload = auth_service.decode_token(token)
    if not payload:
        return jsonify({'message': 'Invalid token'}), 401

    # Token is valid, perform further protected operations here
    return jsonify({'message': 'Protected resource'})
