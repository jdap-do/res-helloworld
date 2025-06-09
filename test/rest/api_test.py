import pytest
from app.api import api_application

@pytest.fixture
def client():
    api_application.config['TESTING'] = True
    with api_application.test_client() as client:
        yield client

def test_add_route(client):
    response = client.get('/calc/add/3/2')
    assert response.status_code == 200
    assert response.data.decode() == '5'

def test_sub_route(client):
    response = client.get('/calc/subtract/5/2')
    assert response.status_code == 200
    assert response.data.decode() == '3'

def test_mul_route(client):
    response = client.get('/mul?a=3&b=4')
    assert response.status_code == 200
    assert response.data.decode() == '12'

def test_div_route(client):
    response = client.get('/div?a=10&b=2')
    assert response.status_code == 200
    assert response.data.decode() == '5'

def test_divide_by_zero(client):
    response = client.get('/div?a=10&b=0')
    assert "error" in response.data.decode().lower()
