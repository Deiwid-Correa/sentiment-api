"""
Model Loader — Sentiment Analysis API

Autor técnico:
Deiwid Correa

Descripción:
Módulo responsable de la carga, cacheo y warm-up del modelo
de análisis de sentimiento desde disco.

Responsabilidades técnicas:
- Carga segura del modelo serializado
- Inicialización controlada (warm-up)
- Prevención de recargas innecesarias
- Manejo de errores durante la carga
- Registro de eventos de estado del modelo
"""


import joblib
import logging
from pathlib import Path
from threading import Lock

# 🔒 Lock para evitar cargas concurrentes
_model_lock = Lock()
_model_instance = None

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / "modelo_sentimiento_v2.pkl"
VECTORIZER_PATH = MODELS_DIR / "vectorizador_tfidf_v2.pkl"


class SentimentModel:
    def __init__(self, model, vectorizer):
        self.model = model
        self.vectorizador = vectorizer

    def predict_proba(self, X):
        return self.model.predict_proba(X)

    @property
    def classes_(self):
        return self.model.classes_


def _load_model() -> SentimentModel:
    logging.info("📦 Cargando modelo v2 desde disco...")

    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Modelo no encontrado: {MODEL_PATH}")

    if not VECTORIZER_PATH.exists():
        raise FileNotFoundError(f"Vectorizador no encontrado: {VECTORIZER_PATH}")

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    logging.info("✅ Modelo v2 cargado correctamente")
    return SentimentModel(model, vectorizer)


def get_model() -> SentimentModel:
    """
    Retorna el modelo en memoria.
    Se carga UNA sola vez (singleton).
    """
    global _model_instance

    if _model_instance is None:
        with _model_lock:
            if _model_instance is None:
                _model_instance = _load_model()

    return _model_instance


# 🔥 Warm-up automático al importar el módulo
try:
    get_model()
    logging.info("🔥 Warm-up del modelo completado")
except Exception as e:
    logging.error(f"❌ Falló el warm-up del modelo: {e}")
