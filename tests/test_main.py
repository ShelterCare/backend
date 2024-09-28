from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == "Test route"


def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200


def test_non_existing_route():
    response = client.get("/non-existing-route")
    assert response.status_code == 404