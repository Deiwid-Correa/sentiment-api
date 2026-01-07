
# Contrato Técnico – Sentiment Analysis API (v2)

## 1. Objetivo
Este documento define el contrato técnico oficial para la integración entre el
servicio de análisis de sentimiento (Python / FastAPI) y el backend consumidor
(Java / Spring Boot).

El contrato es estable y debe respetarse para garantizar compatibilidad futura.

---

## 2. Descripción del Servicio
La API recibe un texto en español y devuelve la clasificación de sentimiento
junto con la probabilidad asociada al resultado.

El modelo es de tipo supervisado (TF-IDF + Logistic Regression).

---

## 3. Base URL

### Entorno local / Docker
```

[http://localhost:8000](http://localhost:8000)

````

---

## 4. Endpoint Principal

### POST `/v2/analyze`

#### Request (JSON)
```json
{
  "text": "Excelente servicio y muy rápido"
}
````

---

#### Response Exitosa (200 OK)

```json
{
  "texto": "Excelente servicio y muy rápido",
  "sentimiento": "positivo",
  "probabilidad": 0.67,
  "modelo": "sentiment-es-v2",
  "trace_id": "a1b2c3d4"
}
```

---

### Campos de Respuesta

| Campo        | Tipo   | Descripción                      |
| ------------ | ------ | -------------------------------- |
| texto        | string | Texto original recibido          |
| sentimiento  | string | positivo / negativo / indefinido |
| probabilidad | float  | Valor entre 0 y 1                |
| modelo       | string | Versión del modelo               |
| trace_id     | string | Identificador de trazabilidad    |

---

## 5. Manejo de Errores

### Error Interno del Modelo (200 OK)

```json
{
  "error_code": "MODEL_FAILURE",
  "message": "Error interno del modelo",
  "trace_id": "e9f23a1b"
}
```

### Timeout de Inferencia (200 OK)

```json
{
  "texto": "Texto original",
  "sentimiento": "error",
  "probabilidad": 0.0,
  "modelo": "sentiment-es-v2"
}
```

> Nota: El servicio mantiene siempre una respuesta HTTP 200 para no romper
> integraciones del backend consumidor.

---

## 6. Validaciones

* El campo `text` es obligatorio
* Longitud mínima: 3 caracteres
* Textos inválidos retornan `sentimiento = "Indefinido"`

---

## 7. Reglas de Integración

* El backend Java debe consumir el servicio vía HTTP REST
* El contrato JSON no debe modificarse sin versionar (`/v3`)
* El backend no debe asumir latencias superiores a 2 segundos

---

## 8. Versionado

* `/v1` → Versión estable anterior
* `/v2` → Versión actual con trazabilidad y protección de ejecución

---

## 9. Autoría Técnica

Diseño, implementación y aseguramiento del servicio realizados por:

**Deiwid Correa**
Backend & Data Integration

