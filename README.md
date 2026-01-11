Sentiment Analysis API (Spanish) 

API REST para análisis de sentimiento en español, construida con FastAPI y Machine Learning clásico, enfocada en estabilidad, claridad y buenas prácticas de ingeniería.


🎯 Objetivo del proyecto

Proveer un servicio backend capaz de clasificar textos en español en tres categorías:

- Positivo  
- Neutral  
- Negativo  

El proyecto prioriza interpretabilidad del modelo, balance de datos y una arquitectura preparada para producción.


 🧠 Modelo de Machine Learning

- Algoritmo: Regresión Logística  
- Vectorización: TF-IDF con n-grams (1, 2)  
- Clases: Positivo, Neutral, Negativo  
- Dataset:
  - 150 frases en español
  - Balanceado (50 por clase)
  - Etiquetado manualmente

Métricas del modelo (dataset v3)

- Accuracy aproximado: 83%
- Clases balanceadas
- Predicción con probabilidad de confianza

---

 Tecnologías utilizadas

- Python 3.9
- FastAPI
- scikit-learn
- Pandas
- Uvicorn
- SlowAPI (rate limiting)
- Joblib
- Docker

---

sentiment-api/
│
├── app/
│ ├── main.py
│ └── api/
│ ├── v1/
│ └── v2/
│
├── training/
│ └── train_model.py
│
├── models/
│ ├── modelo_sentimiento_v3.pkl
│ └── vectorizador_tfidf_v3.pkl
│
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

Endpoints

 Healthcheck



GET /


Respuesta:
```json
{
  "message": "API funcionando correctamente"
}

Análisis de sentimiento (v2)
POST /v2/analyze


Request:

{
  "text": "El servicio fue rápido y profesional"
}


Response:

{
  "texto": "El servicio fue rápido y profesional",
  "sentimiento": "positivo",
  "probabilidad": 0.73,
  "modelo": "sentiment-es-v3",
  "trace_id": "abc123ef"
}

🛡️ Características del backend

Versionado de API

Rate limiting

Logging estructurado

Warm-up del modelo

Manejo de errores

Trazabilidad por request

Preparado para despliegue productivo

🧪 Entrenamiento del modelo

Ejecutar:

python training/train_model.py


Este proceso:

Carga el dataset

Entrena el modelo

Evalúa métricas

Guarda modelo y vectorizador

🐳 Ejecución con Docker
docker-compose up --build

📌 Estado del proyecto

MVP funcional

Modelo entrenado y evaluado

Documentación actualizada

API lista para integración

👤 Autor

Deiwid Correa
Backend & Machine Learning (Applied)





