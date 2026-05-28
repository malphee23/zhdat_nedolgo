from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Сервис доставки работает"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_order():
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json()["order_id"] == 1
    assert response.json()["status"] == "создан"