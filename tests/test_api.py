import pytest
from src.backend.api import app
from src.database.db import init_db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        init_db()
        yield client


def test_get_items(client):
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_create_item(client):
    item = {"name": "Test Item", "quantity": 10, "price": 5.99, "category": "Test"}
    response = client.post("/items", json=item)
    assert response.status_code == 201
    assert response.json["message"] == "Item added"
