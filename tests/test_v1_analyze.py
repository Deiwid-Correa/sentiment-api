from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
API_KEY = "dev-key-123"


def test_analyze_model_failure():
    """
    2.2 — Resiliencia:
    El modelo falla internamente pero la API responde bien
    """

    with patch("app.services.sentiment_service.get_model") as mock_get_model:
        mock_model = mock_get_model.return_value
        mock_model.predict_proba.side_effect = Exception("Modelo caído")

        response = client.post(
            "/v1/analyze",
            headers={"x-api-key": API_KEY},
            json={"text": "Excelente servicio"}
        )

    assert response.status_code == 200
    assert response.json()["sentimiento"] == "error"

