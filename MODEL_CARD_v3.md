# Model Card – Sentiment Analysis v3

## 1. Descripción general
El modelo **sentiment-es-v3** es un clasificador de sentimiento en español diseñado para analizar comentarios de usuarios y clasificarlos en tres categorías:
- Positivo
- Neutral
- Negativo

El modelo está orientado a textos cortos y medianos, típicos de reseñas, comentarios y feedback de usuarios en entornos reales.

---

## 2. Dataset utilizado
El modelo fue entrenado con un dataset balanceado compuesto por **150 comentarios en español**, distribuidos equitativamente:

- 50 positivos
- 50 neutrales
- 50 negativos

Los textos incluyen:
- Opiniones explícitas
- Comentarios mixtos
- Frases descriptivas sin carga emocional

El dataset fue construido manualmente con ejemplos realistas y revisados para evitar sesgos extremos.

---

## 3. Preprocesamiento
- Limpieza básica de texto
- Vectorización mediante **TF-IDF**
- Uso de unigramas y bigramas
- Sin eliminación forzada de stopwords para conservar matices semánticos

---

## 4. Modelo
- Algoritmo: **Logistic Regression**
- Vectorización: **TF-IDF (max_features=5000, ngram_range=(1,2))**
- Entrenamiento con división estratificada (80% entrenamiento / 20% prueba)
- Semilla fija para reproducibilidad

---

## 5. Métricas de evaluación

Resultados obtenidos sobre el conjunto de prueba:

- Accuracy global: **83%**
- Buen equilibrio entre clases
- Mejor desempeño en clase neutral
- Comportamiento coherente en frases mixtas

El modelo devuelve también una **probabilidad asociada** a cada predicción.

---

## 6. Manejo de ambigüedad
Las frases mixtas o ambiguas no son forzadas artificialmente a una categoría.
El modelo clasifica según el peso semántico dominante del texto.

Las decisiones de ajuste de umbrales o reglas adicionales se delegan a la capa de negocio.

---

## 7. Limitaciones conocidas
- No detecta sarcasmo
- No maneja contexto conversacional
- Puede variar su confianza en frases muy cortas

Estas limitaciones son comunes en modelos clásicos de NLP.

---

## 8. Uso previsto
- Análisis de sentimiento en tiempo real
- Integración con sistemas backend
- Visualización de feedback de usuarios

No está diseñado para decisiones críticas sin validación adicional.

---

## 9. Versionado
- v1: modelo inicial
- v2: mejoras en limpieza y estabilidad
- **v3: dataset balanceado y mejora en neutralidad**

---

## 10. Autoría
Modelo, dataset, API y proceso de entrenamiento desarrollados por:

**Deiwid Correa**  
Data & Backend Engineering
