"""
Registro central de versiones del motor de sentimiento.
Cada versión apunta a la misma lógica base (motor único),
pero permite evolucionar contratos y respuestas.
"""

VERSIONS = {
    "v1": {
        "model": "sentiment-es-v1",
        "confidence": False,
        "explanation": False,
    },
    "v2": {
        "model": "sentiment-es-v2",
        "confidence": True,
        "explanation": False,
    },
    "v3": {
        "model": "sentiment-es-v3",
        "confidence": True,
        "explanation": True,
    },
}
