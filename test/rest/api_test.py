import pytest
from app.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_route(client):
    response = client.get('/add?a=3&b=2')
    assert response.status_code == 200
    assert response.data.decode() == '5'

def test_sub_route(client):
    response = client.get('/sub?a=5&b=2')
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
    assert response.status_code == 200
    assert "error" in response.data.decode().lower()
