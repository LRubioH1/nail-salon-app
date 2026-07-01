from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

SERVICIOS_DISPONIBLES = [
    "Aplicación de gelish",
    "Esmalte con calcio",
    "Decoración de uñas",
    "Remoción de esmalte",
]

BEBIDAS_DISPONIBLES = [
    "Café",
    "Té",
    "Refresco",
    "Agua",
]


class ClienteCreate(BaseModel):
    nombre: str = Field(min_length=1)
    telefono: str = Field(min_length=1)
    servicio: str
    bebida_preferida: str
    notas: Optional[str] = None


class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    servicio: Optional[str] = None
    bebida_preferida: Optional[str] = None
    notas: Optional[str] = None


class Cliente(BaseModel):
    id: int
    nombre: str
    telefono: str
    servicio: str
    bebida_preferida: str
    notas: Optional[str] = None
    fecha_registro: datetime
