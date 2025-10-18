from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    embedding = Column(JSON, nullable=False)  # asegurarse de importar JSON

