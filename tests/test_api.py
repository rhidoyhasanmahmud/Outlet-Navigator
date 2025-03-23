from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_api_outlets():
    response = client.get("/outlets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
