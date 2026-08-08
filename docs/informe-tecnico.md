# Informe Técnico - Caracterización del Modelo Local

## Ficha de Caracterización del Modelo

| Dato | Cómo obtenerlo | Valor |
| :--- | :--- | :--- |
| **Perfil de hardware** | Sección 2 de la guía | Perfil C (4 GB) |
| **RAM total del equipo** | `free -h` | 4.0 GB (3.8 GiB) |
| **Modelo y etiqueta** | `ollama list` | gemma3:270m |
| **Tamaño en disco** | `ollama list` | 291 MB |
| **Latencia de 5 ejecuciones (ms)** | `time curl ...` cinco veces | ~800 ms a 1500 ms |
| **Latencia promedio** | Promedio de las cinco | ~1.1 s |
| **RAM usada durante la inferencia** | `free -h` mientras responde | ~2.3 GB |
| **Calidad percibida (1 a 5)** | Su criterio | 3/5 - Responde rápido a instrucciones simples, pero su tamaño limita análisis profundos. |
