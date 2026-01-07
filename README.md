# Sentiment Analysis API (Español)

## Descripción general

Este proyecto implementa una API REST para análisis de sentimiento en textos en español.
La API recibe comentarios, reseñas u opiniones de clientes y clasifica el sentimiento
como positivo o negativo, devolviendo la predicción junto con su probabilidad.

La solución está diseñada como un microservicio listo para producción, pensado para
ser consumido por aplicaciones Back-end (por ejemplo, Java con Spring Boot), sin exponer
ni compartir el modelo de Machine Learning.

---

## Contexto de negocio

Empresas de atención al cliente, marketing y operaciones reciben grandes volúmenes
de comentarios de usuarios (reseñas, encuestas, redes sociales).

Esta API permite:
- Identificar automáticamente comentarios positivos o negativos
- Priorizar la atención a comentarios negativos
- Medir la satisfacción del cliente a lo largo del tiempo
- Apoyar la toma de decisiones operativas y de marketing

Incluso con un modelo simple, la clasificación de sentimiento aporta valor real
a pequeñas y medianas empresas que no cuentan con equipos dedicados de análisis.

---

## Arquitectura de la solución

### Data Science
- Limpieza y normalización del texto
- Vectorización con TF-IDF
- Entrenamiento de modelo supervisado (Logistic Regression)
- Evaluación de métricas
- Serialización del modelo entrenado

### API
- Implementada en Python con FastAPI
- Versionado de endpoints (v1 y v2)
- Manejo de errores controlado
- Protección contra timeouts del modelo
- Logging estructurado con trazabilidad (`trace_id`)

### Despliegue
- Contenerización con Docker
- Orquestación con Docker Compose

### Consumo
- Comunicación vía HTTP/JSON
- Pensada para ser consumida por Back-end en Java (Spring Boot)
- El Back-end no necesita Python ni librerías de Machine Learning

El modelo de ML está completamente encapsulado dentro del microservicio.

---

## Requisitos

- Docker
- Docker Compose

No se requiere Python local para ejecutar el servicio.

---

## Ejecución del proyecto con Docker

### Construir y levantar el servicio

```bash
docker-compose up --build



Documentación Swagger:

http://localhost:8000/docs
---

## Endpoints disponibles

### POST /v2/analyze

- Analiza el sentimiento de un texto en español.

#### Request (JSON)
```json
{
  "text": "El servicio fue rápido y muy profesional"
}

### Response exitosa

{
  "texto": "El servicio fue rápido y muy profesional",
  "sentimiento": "positivo",
  "probabilidad": 0.67,
  "modelo": "sentiment-es-v2",
  "trace_id": "94ac7cd1"
}


###Manejo de errores

- La API responde siempre con HTTP 200.
- Los errores se reportan dentro del cuerpo de la respuesta para facilitar la trazabilidad en los sistemas consumidores.

    Ejemplo de error

{
  "error_code": "MODEL_FAILURE",
  "message": "Error interno del modelo",
  "trace_id": "a1b2c3"
}

    Guía de integración para Back-end (Java / Spring Boot)

Esta API está pensada para ser consumida como un microservicio externo.

###Consideraciones técnicas

Endpoint: /v2/analyze

Método: POST

Content-Type: application/json

Autenticación: No requerida

Respuesta: JSON

### El Back-end no necesita cargar ni ejecutar el modelo de Machine Learning.

### Flujo recomendado en Java

1.Enviar una petición HTTP POST con el texto a analizar

2.Parsear la respuesta JSON

3.Utilizar los campos sentimiento y probabilidad dentro de la lógica de negocio

###Pruebas

El proyecto incluye:

-Pruebas unitarias

-Simulación de timeouts del modelo

-Simulación de fallos controlados del modelo

-Pruebas de regresión entre las versiones v1 y v2
    pytest --cov=app




###Autoría y responsabilidad técnica

Este proyecto fue diseñado, implementado y desplegado por:

Deiwid Correa

Responsabilidades cubiertas

-Limpieza y preparación del dataset

-Entrenamiento y serialización del modelo

-Diseño e implementación de la API

-Versionado de endpoints (v1 y v2)

-Manejo de errores, timeouts y logging

-Implementación de pruebas automatizadas y de regresión

-Dockerización y despliegue con Docker Compose

###Licencia

-Proyecto desarrollado con fines educativos y demostrativos.