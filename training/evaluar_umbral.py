from app.model_loader import modelo, vectorizador
from app.services.sentiment_service import limpiar_texto

textos_prueba = [
    "Excelente servicio, me encantó",
    "Muy buena atención y rapidez",
    "El servicio fue normal",
    "No estuvo mal pero pudo ser mejor",
    "Pésima experiencia, horrible atención",
    "Nunca volvería, muy mal servicio"
]

umbrales = [0.45, 0.5, 0.55, 0.6, 0.65]

for UMBRAL in umbrales:
    print(f"\n🔎 Evaluando UMBRAL = {UMBRAL}")
    print("-" * 50)

    for texto in textos_prueba:
        limpio = limpiar_texto(texto)
        vector = vectorizador.transform([limpio])

        pred = modelo.predict(vector)[0]
        prob = max(modelo.predict_proba(vector)[0])

        if prob < UMBRAL:
            resultado = "Indefinido"
        else:
            resultado = pred

        print(f"Texto: {texto}")
        print(f"Resultado: {resultado} | Confianza: {round(prob, 2)}")
        print("-" * 50)
