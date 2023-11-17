import pytest
import requests
import pdb
import json
# Define the base URL for your API
BASE_URL = 'http://localhost:5000'

# Define the global authentication token variable
auth_token = None

def test_authenticate_user():
    global auth_token  # Use the global auth_token variable

    # Define the endpoint URL
    url = f'{BASE_URL}/api/auth/command/login'

    # Define the request payload
    payload = {
        'username': 'jason@ui-lib.com',
        'password': 'Jason@ui-lib.com123'
        # Add more fields as needed
    }

    # Send a POST request to authenticate a user
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    response_data = json.loads(response.content)
    token = response_data["payload"]["token"]
    auth_token = token
    # Check if the token is not None (i.e., it exists in the response)
    assert token is not None
    assert isinstance(token, str)

    

def test_protected():
    global auth_token  # Use the global auth_token variable

    # Define the endpoint URL
    url = f'{BASE_URL}/api/auth/command/protected'

    # Set the Authorization header with the auth_token
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    # Send a GET request to the /protected endpoint with the token
    response = requests.get(url, headers=headers)

    # Assert the response status code and any other expected behavior
    assert response.status_code == 200
    assert response.json()['message'] == 'Protected resource'

if __name__ == '__main__':
    test_authenticate_user()
    test_protected()