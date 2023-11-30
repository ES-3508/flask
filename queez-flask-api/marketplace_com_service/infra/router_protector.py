# import jwt
# import os
# from dotenv import load_dotenv
# from datetime import datetime, timedelta
# from functools import wraps
# from flask import request, jsonify



# load_dotenv()

# def token_required(func):
#     @wraps(func)
    
#     def decorated_function(*args, **kwargs):
#         token = None

#         # Check if 'Authorization' header is present
#         if 'Authorization' in request.headers:
#             auth_header = request.headers['Authorization']
#             # Extract the token from the header
#             token = auth_header.split()[1] if len(auth_header.split()) > 1 else None

#         # Return 401 if token is missing
#         if not token:
#             return jsonify({'message': 'Token is missing'}), 401

#         token_repo = IdentityRepository()

#         # Verify the token using the TokenCommandRepository's verify_token method
#         payload =token_repo.verify_token(token)

#         if not payload:
#             return jsonify({'message': 'Invalid token'}), 401

#         # Attach the decoded payload to the request context
#         request.current_user = payload

#         # If the token is valid, proceed with the decorated function
#         return func(*args, **kwargs)

#     return decorated_function
