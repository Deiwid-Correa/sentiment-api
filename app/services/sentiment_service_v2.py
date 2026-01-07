import uuid
import time
import logging
import concurrent.futures

from app.model_loader import get_model
from app.services.text_utils import limpiar_texto

TIMEOUT_SECONDS = 2
MODELO_NOMBRE = "sentiment-es-v2"


def _generate_trace_id() -> str:
    return uuid.uuid4().hex[:8]


def _inferir(texto: str):
    model = get_model()

    texto_limpio = limpiar_texto(texto)
    vector = model.vectorizador.transform([texto_limpio])

    probs = model.predict_proba(vector)[0]
    idx = probs.argmax()

    return model.classes_[idx], float(probs[idx])


def analizar_v2(texto: str) -> dict:
    trace_id = _generate_trace_id()
    start_time = time.time()

    if not texto or len(texto.strip()) < 3:
        return {
            "texto": texto,
            "sentimiento": "Indefinido",
            "probabilidad": 0.0,
            "modelo": MODELO_NOMBRE,
            "trace_id": trace_id
        }

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    try:
        future = executor.submit(_inferir, texto)
        sentimiento, prob = future.result(timeout=TIMEOUT_SECONDS)

        latency_ms = round((time.time() - start_time) * 1000, 2)

        logging.info(
            f"INFERENCE_OK | trace_id={trace_id} | "
            f"sentimiento={sentimiento} | prob={round(prob, 2)} | "
            f"latency_ms={latency_ms}"
        )

        return {
            "texto": texto,
            "sentimiento": sentimiento,
            "probabilidad": round(prob, 2),
            "modelo": MODELO_NOMBRE,
            "trace_id": trace_id
        }

    except concurrent.futures.TimeoutError:
        latency_ms = round((time.time() - start_time) * 1000, 2)

        logging.error(
            f"MODEL_TIMEOUT | trace_id={trace_id} | latency_ms={latency_ms}"
        )

        return {
            "texto": texto,
            "sentimiento": "error",
            "probabilidad": 0.0,
            "modelo": MODELO_NOMBRE,
            "trace_id": trace_id
        }

    except Exception as e:
        latency_ms = round((time.time() - start_time) * 1000, 2)

        logging.error(
            f"MODEL_FAILURE | trace_id={trace_id} | latency_ms={latency_ms} | error={str(e)}"
        )

        return {
            "error_code": "MODEL_FAILURE",
            "message": "Error interno del modelo",
            "trace_id": trace_id
        }

    finally:
        executor.shutdown(wait=False)
