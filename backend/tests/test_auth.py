from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "test123"
        }
    )
    assert response.status_code == 201


def test_login_user():
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "test123"
        }
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
