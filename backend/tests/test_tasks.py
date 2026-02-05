from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "test123"
        }
    )
    return response.json()["access_token"]

def test_create_task():
    token = get_token()
    response = client.post(
        "/api/v1/tasks",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Test Task"}
    )
    assert response.status_code == 201
