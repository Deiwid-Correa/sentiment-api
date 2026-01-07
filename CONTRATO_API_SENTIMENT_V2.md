

# CONTRATO TÉCNICO – API DE ANÁLISIS DE SENTIMIENTO (V2)

## 1. Propósito

Este documento define el **contrato técnico oficial** para la integración entre el **servicio de Análisis de Sentimiento (Data Science – Python)** y el **Back-End (Java / Spring Boot)**.

El servicio se expone como un **microservicio independiente**, accesible vía HTTP, y debe ser consumido como un **cliente REST**.
El equipo de Back-End **no debe cargar modelos ni librerías de Machine Learning**.

---

## 2. Información general del servicio

* **Nombre del servicio:** Sentiment Analysis API
* **Versión estable:** v2
* **Protocolo:** HTTP / JSON
* **Arquitectura:** Microservicio independiente
* **Responsabilidad:** Clasificación de sentimiento de textos en español

---

## 3. Endpoint oficial

### POST `/v2/analyze`

Clasifica el sentimiento de un texto y devuelve la etiqueta junto con la probabilidad.

---

## 4. Request

### Headers

```http
Content-Type: application/json
```

### Body (JSON)

```json
{
  "text": "Excelente servicio y muy rápido"
}
```

### Reglas de validación

* El campo `text` es obligatorio
* Longitud mínima: 3 caracteres
* Idioma esperado: español
* Texto vacío o inválido devuelve respuesta controlada

---

## 5. Response – Éxito

### Código HTTP

```http
200 OK
```

### Body (JSON)

```json
{
  "texto": "Excelente servicio y muy rápido",
  "sentimiento": "positivo",
  "probabilidad": 0.67,
  "modelo": "sentiment-es-v2",
  "trace_id": "94ac7cd1"
}
```

### Campos

| Campo        | Tipo   | Descripción                                                     |
| ------------ | ------ | --------------------------------------------------------------- |
| texto        | string | Texto original enviado                                          |
| sentimiento  | string | Clasificación del modelo (`positivo`, `negativo`, `indefinido`) |
| probabilidad | float  | Confianza del modelo (0.0 – 1.0)                                |
| modelo       | string | Identificador del modelo utilizado                              |
| trace_id     | string | Identificador único para trazabilidad                           |

---

## 6. Response – Error controlado (fallo del modelo)

Este escenario ocurre cuando el modelo falla internamente, pero la API **mantiene estabilidad y responde correctamente**.

### Código HTTP

```http
200 OK
```

### Body (JSON)

```json
{
  "error_code": "MODEL_FAILURE",
  "message": "Error interno del modelo",
  "trace_id": "cf486222"
}
```

### Notas importantes

* El endpoint **nunca expone errores internos**
* El contrato se mantiene estable incluso ante fallos
* El campo `trace_id` permite correlacionar logs

---

## 7. Timeout y resiliencia

* El servicio implementa **protección por timeout**
* Si la inferencia supera el tiempo máximo permitido:

  * Se devuelve una respuesta controlada
  * No se bloquea el servicio
* El consumidor (Java) **no necesita implementar reintentos agresivos**

---

## 8. Versionado y compatibilidad

* `/v1` → versión legacy (no usar para nuevas integraciones)
* `/v2` → versión estable y recomendada
* Cambios futuros se publicarán como `/v3` sin romper `/v2`

---

## 9. Extensibilidad futura (no implementado aún)

El contrato está preparado para soportar en el futuro:

* `/v2/stats` → métricas agregadas
* `/v2/batch` → procesamiento de múltiples textos
* Ajuste de umbral de confianza

Estos endpoints **no forman parte del MVP actual** y no deben asumirse como disponibles.

---

## 10. Responsabilidades por equipo

### Data Science / API (Python)

* Entrenamiento del modelo
* Serialización y carga del modelo
* Exposición del endpoint
* Logs, trazabilidad y manejo de errores

### Back-End (Java / Spring Boot)

* Consumir el endpoint vía HTTP
* Manejar respuestas de éxito y error
* Integrar el resultado en su lógica de negocio
* No manipular ni cargar modelos de ML

---

## 11. Prueba mínima de integración

Ejemplo de prueba desde cualquier cliente HTTP:

```bash
curl -X POST http://localhost:8000/v2/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"Excelente servicio"}'
```

Si esta llamada responde correctamente, la integración está lista.

---

## 12. Estado del contrato

* **Estado:** Estable
* **Uso recomendado:** Producción / Demo / Hackathon
* **Cambios:** Solo mediante nueva versión del endpoint

---

### Autoría técnica

Este contrato y la implementación del servicio fueron diseñados y desarrollados por:

**Deiwid Correa**
Arquitectura, Data Science, API, Seguridad, Versionado y Pruebas

