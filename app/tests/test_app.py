from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    # Отправляем GET-запрос к корневому эндпоинту
    response = client.get("/api/v1/app")

    # Проверяем статус код
    assert response.status_code == 401


def test_invalid_endpoint():
    # Проверяем несуществующий эндпоинт
    response = client.get("/api/v1/invalid")

    # Проверяем статус код 404 (Not Found)
    assert response.status_code == 404
