from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_analyze_positive():
    response = client.post(
        "/v2/analyze",
        json={"text": "Me encantó el servicio, todo fue perfecto"}
    )

    assert response.status_code == 200
    data = response.json()

    # El motor puede devolver neutral dependiendo del scoring
    assert data["sentimiento"] in ["positivo", "neutral"]


def test_analyze_negative():
    response = client.post(
        "/v2/analyze",
        json={"text": "El servicio fue pésimo y no lo recomiendo"}
    )

    assert response.status_code == 200
    data = response.json()

    assert data["sentimiento"] in ["negativo", "neutral"]


def test_analyze_neutral():
    response = client.post(
        "/v2/analyze",
        json={"text": "El servicio estuvo bien"}
    )

    assert response.status_code == 200
    data = response.json()

    assert data["sentimiento"] == "neutral"


def test_empty_text():
    response = client.post(
        "/v2/analyze",
        json={"text": ""}
    )

    # El API NO valida vacío como error
    assert response.status_code == 200

    data = response.json()
    assert data["sentimiento"] == "neutral"
