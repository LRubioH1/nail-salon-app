from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator

SERVICIOS_VALIDOS = [
    "Aplicación de gelish",
    "Esmalte con calcio",
    "Decoración de uñas",
    "Remoción de esmalte",
]

BEBIDAS_VALIDAS = ["Café", "Té", "Refresco", "Agua"]


class ServicioBase(BaseModel):
    nombre_servicio: str
    descripcion: Optional[str] = None

class Servicio(ServicioBase):
    id: int


def _validar_no_vacio(valor: Optional[str], campo: str) -> Optional[str]:
    if valor is not None and not valor.strip():
        raise ValueError(f"El {campo} no debe estar vacío")
    return valor


def _validar_servicio(valor: Optional[str]) -> Optional[str]:
    if valor is not None and valor not in SERVICIOS_VALIDOS:
        raise ValueError(f"El servicio debe ser uno de: {', '.join(SERVICIOS_VALIDOS)}")
    return valor


def _validar_bebida(valor: Optional[str]) -> Optional[str]:
    if valor is not None and valor not in BEBIDAS_VALIDAS:
        raise ValueError(f"La bebida debe ser una de: {', '.join(BEBIDAS_VALIDAS)}")
    return valor

class ClienteBase(BaseModel):
    nombre: str
    telefono: str
    servicio: str
    bebida_preferida: str
    notas: Optional[str] = None

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        return _validar_no_vacio(v, "nombre")

    @field_validator("telefono")
    @classmethod
    def telefono_no_vacio(cls, v):
        return _validar_no_vacio(v, "teléfono")

    @field_validator("servicio")
    @classmethod
    def servicio_valido(cls, v):
        return _validar_servicio(v)

    @field_validator("bebida_preferida")
    @classmethod
    def bebida_valida(cls, v):
        return _validar_bebida(v)


class ClienteCreate(ClienteBase):
    pass


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    servicio: Optional[str] = None
    bebida_preferida: Optional[str] = None
    notas: Optional[str] = None

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        return _validar_no_vacio(v, "nombre")

@field_validator("telefono")
@classmethod
def telefono_no_vacio(cls, v):
    return _validar_no_vacio(v, "teléfono")

@field_validator("servicio")
@classmethod
def servicio_valido(cls, v):
    return _validar_servicio(v)

@field_validator("bebida_preferida")
@classmethod
def bebida_valida(cls, v):
    return _validar_bebida(v)

class Cliente(ClienteBase):
    id: int
    fecha_registro: datetime = Field(default_factory=datetime.now)
