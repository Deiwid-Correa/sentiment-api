# Contrato Técnico de Integración  
## Sentiment Analysis API — Consumo desde Java / Spring Boot

---

## Objetivo del documento

Este documento define el contrato técnico oficial para integrar un Back-end
desarrollado en Java (Spring Boot u otro framework) con el microservicio
de análisis de sentimiento implementado en Python.

El objetivo es permitir que el equipo de Back-end consuma la predicción
del modelo de Machine Learning **sin necesidad de conocer Python,
Data Science ni cargar modelos localmente**.

---

## Descripción del servicio

El microservicio expone una API REST que recibe texto en español y devuelve
la clasificación de sentimiento junto con su probabilidad asociada.

El modelo de Machine Learning está completamente encapsulado dentro
del servicio y **NO debe ser replicado ni exportado al Back-end Java**.

---

## Información general del servicio

- Protocolo: HTTP
- Formato: JSON
- Puerto: 8000
- Base URL:

http://localhost:8000

- Documentación Swagger:

http://localhost:8000/docs


