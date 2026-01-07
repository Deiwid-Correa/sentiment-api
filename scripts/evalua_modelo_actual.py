import joblib
import os

# 📍 Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

modelo_path = os.path.join(BASE_DIR, "models", "modelo_sentimiento_v2.pkl")
vector_path = os.path.join(BASE_DIR, "models", "vectorizador_tfidf_v2.pkl")

print("📦 Cargando modelo y vectorizador...")

modelo = joblib.load(modelo_path)
vectorizador = joblib.load(vector_path)

tests = [
    "Excelente servicio, me encantó",
    "El servicio fue normal",
    "No estuvo mal pero tampoco fue bueno",
    "Horrible atención, pésimo todo",
    "Me gustó mucho la experiencia",
]

print("🧪 Ejecutando pruebas manuales...\n")

for texto in tests:
    X = vectorizador.transform([texto])
    pred = modelo.predict(X)[0]
    prob = modelo.predict_proba(X).max()

    print(f"Texto: {texto}")
    print(f"Predicción: {pred} | Confianza: {round(prob, 2)}")
    print("-" * 50)
