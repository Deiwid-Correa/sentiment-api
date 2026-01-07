import uuid
import logging
from app.model_loader import get_model
from app.services.text_utils import limpiar_texto

MODELO_NOMBRE = "sentiment-es-v1"
UMBRAL_CONFIANZA = 0.6


def _generate_trace_id() -> str:
    return uuid.uuid4().hex[:8]


def analizar(texto: str) -> dict:
    trace_id = _generate_trace_id()

    try:
        if not texto or len(texto.strip()) < 3:
            return {
                "texto": texto,
                "sentimiento": "Indefinido",
                "probabilidad": 0.0,
                "modelo": MODELO_NOMBRE
            }

        model = get_model()
        texto_limpio = limpiar_texto(texto)

        X = model.vectorizador.transform([texto_limpio])
        probs = model.predict_proba(X)[0]

        pred_idx = probs.argmax()
        prob = float(probs[pred_idx])
        etiqueta = model.classes_[pred_idx]

        if prob < UMBRAL_CONFIANZA:
            etiqueta = "Indefinido"

        return {
            "texto": texto,
            "sentimiento": etiqueta,
            "probabilidad": round(prob, 2),
            "modelo": MODELO_NOMBRE
        }

    except Exception as e:
         logging.error(
        f"MODEL_FAILURE | trace_id={trace_id} | error={str(e)}"
    )

    return {
        "texto": texto,
        "sentimiento": "error",   # 👈 EXACTO como lo pide el test
        "probabilidad": 0.0,
        "modelo": MODELO_NOMBRE
    }
