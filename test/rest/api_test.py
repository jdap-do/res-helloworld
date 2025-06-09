import pytest
from app.api import api_application as app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_add_route(client):
    response = client.get("/calc/add/3/2")
    assert response.status_code == 200
    assert response.data.decode() == "5"


def test_sub_route(client):
    response = client.get("/calc/subtract/5/2")
    assert response.status_code == 200
    assert response.data.decode() == "3"


def test_mul_route(client):
    response = client.get("/calc/multiply/3/4")
    assert response.status_code == 200
    assert response.data.decode() == "12"


def test_div_route(client):
    response = client.get("/calc/divide/10/2")
    assert response.status_code == 200
    assert response.data.decode() == "5"


def test_divide_by_zero(client):
    response = client.get("/calc/divide/10/0")
    assert response.status_code == 400
    assert "error" in response.data.decode().lower()