from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    # When it accesses the ~/
    response = client.get("/")
    # check whether it return 200
    assert response.status_code == 200
    # check if it returns {"msg": "Hello World"}
    assert response.json() == {"msg": "Hello World"}