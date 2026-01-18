def analyze_text(text: str) -> dict:
    text_lower = text.lower()

    if "bueno" in text_lower or "excelente" in text_lower:
        sentimiento = "positivo"
        confianza = 0.9
    elif "malo" in text_lower or "horrible" in text_lower:
        sentimiento = "negativo"
        confianza = 0.9
    else:
        sentimiento = "neutro"
        confianza = 0.6

    return {
        "texto": text,
        "sentimiento": sentimiento,
        "confianza": confianza,
        "version": "v3-ml-demo",
        "explicacion": "Texto con señales mixtas: palabras negativas y ausencia de intención clara."
        " Análisis ejecutado por motor-unico-v1"
        
        


    }
