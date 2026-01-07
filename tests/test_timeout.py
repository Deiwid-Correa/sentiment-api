import time
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def slow_infer(*args, **kwargs):
    time.sleep(3)  # > TIMEOUT_SECONDS
    return "positivo", 0.9


def test_v2_timeout_protection():
    with patch(
        "app.services.sentiment_service_v2._inferir",
        side_effect=slow_infer
    ):
        response = client.post(
            "/v2/analyze",
            json={"text": "Excelente servicio"}
        )

    assert response.status_code == 200
    body = response.json()

    assert body["sentimiento"] == "error"
    assert body["probabilidad"] == 0.0
    assert body["modelo"] == "sentiment-es-v2"
