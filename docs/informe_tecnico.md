# Informe Técnico: Pruebas y CI/CD - Semana 4

## 1. Pruebas Unitarias (Pytest)
- **Framework:** Pytest 9.1.1
- **Resultado:** 5/5 Pruebas Exitosas (`PASSED`).
- **Endpoints Validados:**
  - `GET /health` -> Respuesta 200 OK.
  - `POST /clasificar` -> Validación de motor, tipos devueltos y reglas del modelo eco.
  - `GET /inferencias` -> Persistencia y retorno del historial.

## 2. Integración Continua (CI/CD)
- **Plataforma:** GitHub Actions (`.github/workflows/ci.yml`).
- **Triggers:** Push y Pull Request sobre la rama `main`.
- **Acciones:** Configuración de Python 3.12, instalación de dependencias y ejecución automatizada de Pytest.

## 3. Pruebas de Carga (Locust)
- **Herramienta:** Locust 2.46.3
- **Escenario:** 10 usuarios concurrentes con Spawn Rate de 2 usuarios/seg.
- **Resultados de Rendimiento:**
  - **Tasa de Errores:** 0%
  - **Latencia Promedio Global:** ~6 ms
  - **Comportamiento por Endpoint:**
    - `GET /health`: ~3.4 ms
    - `POST /clasificar`: ~6.3 ms
    - `GET /inferencias`: ~13.2 ms

## Conclusión
La API demuestra un rendimiento óptimo, alta confiabilidad con 0% de tasa de fallos bajo carga simulada y un pipeline de CI completamente integrado para entregas continuas.
