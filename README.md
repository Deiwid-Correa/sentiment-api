# Sentiment Analysis API (Español) – Hackathon Demo

## 📌 Descripción general

Este proyecto implementa una **API REST para análisis de sentimiento en textos en español**.
La API recibe comentarios, reseñas u opiniones de clientes y clasifica automáticamente el sentimiento como **positivo, negativo o neutro**, devolviendo además un **nivel de confianza** asociado a la predicción.

La solución está diseñada como un **microservicio desacoplado**, listo para ser consumido por aplicaciones Back-end (por ejemplo, Java con Spring Boot), **sin exponer ni compartir el modelo de Machine Learning**.

---

## 🏢 Contexto de negocio

Empresas de **atención al cliente, marketing y operaciones** reciben grandes volúmenes de comentarios provenientes de:

* reseñas de productos
* encuestas de satisfacción
* redes sociales

Esta API permite:

* Identificar automáticamente comentarios positivos, negativos o ambiguos
* Priorizar la atención a comentarios negativos
* Detectar casos dudosos (neutros) para revisión manual
* Medir la satisfacción del cliente a lo largo del tiempo

Incluso con un modelo simple, la clasificación de sentimiento aporta **valor real** a pequeñas y medianas empresas que no cuentan con equipos dedicados de análisis de datos.

---

## 🧠 Arquitectura de la solución

### Data Science

* Limpieza y normalización del texto
* Vectorización mediante **TF-IDF**
* Entrenamiento de modelo supervisado (Logistic Regression)
* Evaluación básica de métricas
* Serialización del modelo entrenado

### API

* Implementada en **Python con FastAPI**
* Versionado de endpoints
* Validación de entrada
* Respuesta estructurada y consistente en JSON
* Encapsulamiento total del modelo dentro del servicio

### Despliegue

* Contenerización con **Docker**
* Orquestación mediante **Docker Compose**

### Consumo

* Comunicación vía **HTTP / JSON**
* Pensada para ser consumida por Back-end en **Java (Spring Boot)**
* El Back-end **no necesita Python ni librerías de Machine Learning**

El modelo de ML permanece completamente encapsulado dentro del microservicio.

---

## ⚙️ Requisitos

* Docker
* Docker Compose

> No se requiere Python local para ejecutar el servicio.

---

## 🚀 Ejecución del proyecto con Docker

### Construir y levantar el servicio

```bash
docker-compose up --build
```

La API quedará disponible en:

```
http://localhost:8000
```

Documentación Swagger:

```
http://localhost:8000/docs
```

---

## 🔌 Endpoint disponible

### POST /v3/analyze

Analiza el sentimiento de un texto en español.

#### Request (JSON)

```json
{
  "text": "El servicio fue rápido y muy profesional"
}
```

#### Response exitosa

```json
{
  "sentimiento": "positivo",
  "confianza": 0.87
}
```

* **sentimiento**: positivo | negativo | neutro
* **confianza**: valor entre 0 y 1 que indica la seguridad de la predicción

---

## 🧪 Ejemplos de uso

* **Positivo**:
  “El servicio fue excelente, rápido y muy amable.”

* **Negativo**:
  “El lugar estaba sucio y la atención fue horrible.”

* **Ambiguo / Neutro**:
  “Fue sucio y feo, pero tal vez regrese más adelante.”

---

## 🔗 Guía de integración para Back-end (Java / Spring Boot)

Esta API está pensada para ser consumida como un **microservicio externo**.

### Consideraciones técnicas

* Endpoint: `/v3/analyze`
* Método: `POST`
* Content-Type: `application/json`
* Autenticación: No requerida
* Respuesta: JSON

### Flujo recomendado en Java

1. Enviar una petición HTTP POST con el texto a analizar
2. Parsear la respuesta JSON
3. Utilizar los campos `sentimiento` y `confianza` dentro de la lógica de negocio

> El Back-end **no necesita cargar ni ejecutar el modelo de Machine Learning**.

---

## 🎯 Alcance del proyecto (Hackathon)

* MVP funcional de análisis de sentimiento
* Integración clara entre **Data Science y Back-end**
* Enfoque en claridad, simplicidad y valor de negocio
* Preparado para demostración en entorno controlado

---

## 👤 Autoría y responsabilidad técnica

Este proyecto fue diseñado e implementado por:

**Deiwid Correa**

Responsabilidades cubiertas:

* Limpieza y preparación del dataset
* Entrenamiento y serialización del modelo
* Diseño e implementación de la API
* Versionado de endpoints
* Validación de entradas y estructura de respuestas
* Dockerización y despliegue con Docker Compose

---

## 📄 Licencia

Proyecto desarrollado con fines **educativos y demostrativos** (Hackathon).

