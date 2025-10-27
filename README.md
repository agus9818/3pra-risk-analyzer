DevSecOps 3rd Party Risk Analyzer (3PRA)
Solución de Microservicios para la Ingesta, Priorización Automatizada y Persistencia de Hallazgos de Vulnerabilidades de Plataformas de Terceros.

El 3PRA aborda el desafío de gestionar la seguridad de la cadena de suministro de software (Software Supply Chain Security), permitiendo a las organizaciones aplicar la lógica de riesgo de negocio a los resultados brutos de escáneres dinámicos (DAST) o reportes de proveedores.


1. Arquitectura del Proyecto (Fase 1: MVP)El proyecto se basa en una arquitectura de microservicios contenerizada con Docker Compose.ServicioTecnologíaPropósitoPuertoapi_ingestionFastAPI (Python)Recibe los hallazgos de vulnerabilidades (JSON), aplica la lógica de priorización y escribe en la DB.8000dbPostgreSQLBase de datos persistente para almacenar todos los hallazgos y su prioridad calculada.5432 (Interno)

2. Lógica de Priorización de RiesgoEl corazón del 3PRA es la función de priorización, que convierte la Severidad del Escáner (técnica) en una Prioridad de Ticket (de negocio) cruzándola con la Criticidad del Activo.Fórmula: Prioridad_Ticket = f(Severidad_Scanner, Criticidad_Activo)Matriz de Decisión ImplementadaSeveridad EscánerCriticidad del ActivoPrioridad de TicketImplicación de NegocioCríticoALTA/MEDIA/BAJAP0 - BloqueadorRequiere acción inmediata.AltoALTAP1 - UrgenteDetener el pipeline o escalamiento.AltoMEDIA/BAJAP2 - ImportanteAgendado para la próxima sprint.MedioALTAP2 - ImportanteImpacto potencial alto.MedioMEDIA/BAJAP3 - BajoMonitoreo o corrección futura.BajoCualquieraP3 - BajoRiesgo tolerable.

4. Uso de la API (Ingesta)
El endpoint de la API utiliza el estándar OpenAPI de FastAPI.

Documentación Interactiva (Swagger UI): http://localhost:8000/docs

Health Check: http://localhost:8000/api/health

Endpoint de Ingesta
Utiliza este endpoint para simular el envío de un resultado de escáner.

Ruta: POST http://localhost:8000/api/vulnerabilities/

Cuerpo (Ejemplo JSON):

JSON

{
  "activo_afectado": "API_Pagos", 
  "severidad_scanner": "Alto",
  "vulnerabilidad": "Fallo de autenticación (Credenciales por defecto)",
  "url": "https://api.pagos.com/v1/auth"
}
NOTA: El sistema calculará la Prioridad de Ticket y la Criticidad del Activo automáticamente basándose en la data provista.