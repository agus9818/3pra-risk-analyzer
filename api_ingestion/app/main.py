from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models                             # <-- CORRECCIÓN 1: Importación relativa para models
from .models import VulnerabilityCreate          # <-- CORRECCIÓN 2: Asegurar la importación relativa para el Schema
from .utils import calcular_prioridad_ticket
import uvicorn
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="3PRA - Ingestión API",
    description="API para recibir y priorizar hallazgos de vulnerabilidades de terceros."
)

# ENDPOINT: Ingesta y priorización de vulnerabilidades
@app.post("/api/vulnerabilities/", status_code=201, response_model=VulnerabilityCreate)
def create_vulnerability(finding: VulnerabilityCreate, db: Session = Depends(get_db)):
    """Recibe un hallazgo de vulnerabilidad, calcula su prioridad y lo guarda en la DB"""
    # Aplica la lógica de priorización
    prioridad, criticidad = calcular_prioridad_ticket(
        severidad_scanner=finding.severidad_scanner,
        activo_nombre=finding.activo_afectado
    )

    # Crear el objeto ORM para DB
    db_finding = models.Vulnerability(
        activo_afectado=finding.activo_afectado,
        severidad_scanner=finding.severidad_scanner,
        vulnerabilidad=finding.vulnerabilidad,
        url=finding.url,

        # Campos calculados por el sistema
        criticidad_activo=criticidad,
        prioridad_ticket=prioridad,
        corregido=False
    )

    try:
        db.add(db_finding)
        db.commit()
        db.refresh(db_finding)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al guardar el hallazgo en la base de datos.")
    
    # Devuelve el objeto que fue guardado
    return db_finding

# ENDPOINT de prueba
@app.get("/api/health")
def health_check():
    """Verifica si la API está funcionando correctamente."""
    return {"status": "ok", "service": "3PRA Ingestión API"}