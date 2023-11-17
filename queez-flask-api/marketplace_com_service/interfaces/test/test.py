import pytest
import requests
import json

BASE_URL = 'http://localhost:5000'

@pytest.fixture

def test_default_route():
    url = f'{BASE_URL}/'
    response = requests.get(url)
    assert response.status_code == 200
    assert response.text == "Welcome to the default route!"

def test_get_all_hierarchical_data():
    url = f'{BASE_URL}/api/landing/quary/get_all_hierarchical_data'
    response = requests.get(url)
    assert response.status_code == 200
    # Add more assertions based on the expected behavior of the route

def test_get_element_by_id():
    url = f'{BASE_URL}/api/landing/quary/get_element_by_id/1'
    response = requests.get(url)
    try:
        assert response.status_code == 200
    except AssertionError:
        print(response.content)
        raise


def test_get_all_filter_data():
    url = f'{BASE_URL}/api/landing/quary/get_all_filter_data'
    response = requests.get(url)
    assert response.status_code == 200
    # Add more assertions based on the expected behavior of the route

def test_get_all():
    url = f'{BASE_URL}/api/landing/quary/get_all'
    response = requests.get(url)
    assert response.status_code == 200
    # Add more assertions based on the expected behavior of the route

# Add more test cases for other routes



if __name__ == '__main__':
    pytest.main()
