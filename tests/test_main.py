from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_all_vacunas():
    # Verifica que el endpoint principal responda correctamente y retorne una lista
    response = client.get("/vacunas")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_existing_year():
    # Prueba con un dato conocido (2022 está en nuestro mock_db)
    response = client.get("/vacunas/2022")
    assert response.status_code == 200
    assert response.json()["year"] == 2022
    assert response.json()["country"] == "Panama"

def test_read_non_existent_year():
    # Verifica que la API maneje correctamente los errores 404
    response = client.get("/vacunas/1800")
    assert response.status_code == 404