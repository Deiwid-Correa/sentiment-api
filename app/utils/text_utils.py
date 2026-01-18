import re


def normalize_text(text: str) -> str:
    """
    Normaliza el texto para análisis de sentimiento.
    Compatible con Python 3.9.
    """
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\sáéíóúñ]", "", text)
    return text.strip()
