import re

def limpiar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"http\S+|www\S+", "", texto)
    texto = re.sub(r"@\w+|#\w+", "", texto)
    texto = re.sub(r"[^a-záéíóúüñ\s]", "", texto)
    return " ".join(texto.split())
