from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# URL de la Base de Datos
# Lee la variable de entorno que definimos en docker-compose.yml
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./test.db")

# Creación del motor
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creación de la sesión
# SessionLocal será la clase que se instancie para obtener la conexión a la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa
# Base es la clase de la que se heredarán los modelos ORM
Base = declarative_base()

# Función de utilidad para obtener una sesión de DB
# FastAPI usa esto para inyectar la dependencia de la DB en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

