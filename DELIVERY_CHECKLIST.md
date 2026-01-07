
# Checklist de Entrega – Sentiment Analysis API

Este checklist define los criterios mínimos para considerar la integración
con el backend Java como exitosa.

---

## 1. Entregables Incluidos

✔ API de análisis de sentimiento funcional (FastAPI)  
✔ Modelo de Machine Learning cargado desde archivo  
✔ Endpoint estable `/v2/analyze`  
✔ Manejo de errores y timeouts  
✔ Logs de inferencia y trazabilidad  
✔ Dockerfile  
✔ docker-compose.yml  
✔ Documentación técnica (README + contrato de API)

---

## 2. Cómo levantar el servicio (Backend)

### Opción recomendada: Docker Compose
```bash
docker-compose up
````

El servicio quedará disponible en:

```
http://localhost:8000
```

---

## 3. Prueba rápida de integración

### Request de prueba

```bash
curl -X POST http://localhost:8000/v2/analyze \
-H "Content-Type: application/json" \
-d '{"text":"Excelente servicio y muy rápido"}'
```

### Respuesta esperada

```json
{
  "texto": "Excelente servicio y muy rápido",
  "sentimiento": "positivo",
  "probabilidad": 0.67,
  "modelo": "sentiment-es-v2",
  "trace_id": "xxxxxxx"
}
```

---

## 4. Criterios de Integración Exitosa

✔ El backend Java puede consumir `/v2/analyze`
✔ La respuesta JSON coincide con el contrato
✔ Se manejan correctamente respuestas de error
✔ El servicio responde en menos de 2 segundos
✔ No se requieren cambios en el contrato

---

## 5. Responsabilidades

### Servicio de Sentimiento (Python)

* Disponibilidad del endpoint
* Estabilidad del contrato
* Versionado de la API
* Manejo de errores internos

### Backend Consumidor (Java)

* Consumo del endpoint vía HTTP
* Manejo de respuestas
* Persistencia o uso del resultado
* No asumir lógica interna del modelo

---

## 6. Estado de la Entrega

🟢 Servicio listo para integración
🟢 Contrato estable
🟢 Docker operativo
🟢 Pruebas básicas completadas

---

## 7. Contacto Técnico

Para dudas técnicas relacionadas con el servicio:

**Deiwid Correa**

