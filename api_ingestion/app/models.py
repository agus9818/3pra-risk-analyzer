from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Literal
from .database import Base


# Modelo ORM: Estructura de la tabla en PostgreSQL

class Vulnerability(Base):
    __tablename__ = 'vulnerabilities'

    # Campos primarios
    id = Column(Integer, primary_key=True, index=True)
    activo_afectado = Column(String, index=True)
    severidad_scanner = Column(String)
    vulnerabilidad = Column(String)
    url = Column(String)

    # Campos de gestión (Añadidos por el sistema)
    criticidad_activo = Column(String) # Alta, Media, Baja
    prioridad_ticket = Column(String, index=True) # P0-Bloqueador, P1-Urgente, etc.

    # Campos de Estado
    corregido = Column(String, default=False)
    fecha_deteccion = Column(DateTime, default=func.now())
    fecha_ultima_actualizacion = Column(DateTime, default=func.now(), onupdate=func.now())

# Modelos SCHEMA: La validación para la API

# El modelo que se espera recibir en el endpoint de la API
class VulnerabilityCreate(BaseModel):
    activo_afectado: str
    severidad_scanner: Literal["Crítico", "Alto", "Medio", "Bajo"]
    vulnerabilidad: str
    url: str

    # Configuración de Pydantic
    class Config:
        from_attributes = True # Requerido para la compatibilidad con SQLAlchemy
        