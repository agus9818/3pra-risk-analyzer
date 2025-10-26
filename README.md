DevSecOps 3rd Party Risk Analyzer (3PRA)

Implementación de microservicios con FastAPI y PostgreSQL para la ingesta, priorización automatizada y visualización del riesgo de vulnerabilidades de plataformas de terceros. Preparado para Docker/K8s y CI/CD.

##  Instrucciones de Levantamiento (Fase 1: Backend + DB)

Este proyecto utiliza Docker Compose para orquestar la API de ingesta y la base de datos.

1.  **Construir e iniciar los contenedores:**
    ```bash
    docker-compose up -d --build
    ```
2.  **Verificar el estado:**
    ```bash
    docker ps
    ```
3.  **Acceder a la API de Ingesta (Backend):**
    Una vez levantado, el servicio FastAPI está disponible en: `http://localhost:8000`