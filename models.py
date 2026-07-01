from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ServicioBase(BaseModel):
    nombre_servicio: str
    descripcion: Optional[str] = None


class Servicio(ServicioBase):
    id: int


class ClienteBase(BaseModel):
    nombre: str
    telefono: str
    servicio: str
    bebida_preferida: str
    notas: Optional[str] = None


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    servicio: Optional[str] = None
    bebida_preferida: Optional[str] = None
    notas: Optional[str] = None


class Cliente(ClienteBase):
    id: int
    fecha_registro: datetime = Field(default_factory=datetime.now)
