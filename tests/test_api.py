from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

payload = {
    "text": "El servicio fue rápido y muy profesional"
}


def test_v1_analyze():
    response = client.post("/v1/analyze", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "sentimiento" in body


def test_v2_analyze():
    response = client.post("/v2/analyze", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "sentimiento" in body


def test_v3_analyze():
    response = client.post("/v3/analyze", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "sentimiento" in body
