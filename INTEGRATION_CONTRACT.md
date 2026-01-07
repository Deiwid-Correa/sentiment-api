# Integration Contract — Sentiment Analysis API

## Purpose

This document defines how external systems (such as a Java backend)
should consume the Sentiment Analysis API.

---

## Base URL

Local (Docker):
http://localhost:8000

---

## Endpoint

POST /v2/analyze

---

## Request

Headers:
- Content-Type: application/json
- Accept: application/json

Body example:

{
  "text": "Excelente servicio y muy rápido"
}

---

## Successful Response (200 OK)

{
  "texto": "Excelente servicio y muy rápido",
  "sentimiento": "positivo",
  "probabilidad": 0.67,
  "modelo": "sentiment-es-v2",
  "trace_id": "94ac7cd1"
}

---

## Error Response (Model Failure)

{
  "error_code": "MODEL_FAILURE",
  "message": "Internal model error",
  "trace_id": "a1b2c3"
}

---

## Notes for Backend Team

- Use endpoint /v2/analyze
- Response is always HTTP 200
- Errors are returned inside the JSON
- Use trace_id for logs
- No authentication required
