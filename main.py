from datetime import datetime

from fastapi import FastAPI, HTTPException

from models import (
    BEBIDAS_DISPONIBLES,
    SERVICIOS_DISPONIBLES,
    Cliente,
    ClienteCreate,
    ClienteUpdate,
)

app = FastAPI(title="Estética de Uñas API")

clientes: list[Cliente] = []
next_id = 1


@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido a la API de la Estética de Uñas"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/servicios")
def listar_servicios():
    return SERVICIOS_DISPONIBLES


@app.get("/bebidas")
def listar_bebidas():
    return BEBIDAS_DISPONIBLES


@app.post("/clientes", response_model=Cliente)
def crear_cliente(cliente: ClienteCreate):
    global next_id

    if cliente.servicio not in SERVICIOS_DISPONIBLES:
        raise HTTPException(status_code=400, detail="Servicio no válido")
    if cliente.bebida_preferida not in BEBIDAS_DISPONIBLES:
        raise HTTPException(status_code=400, detail="Bebida no válida")

    nuevo_cliente = Cliente(
        id=next_id,
        nombre=cliente.nombre,
        telefono=cliente.telefono,
        servicio=cliente.servicio,
        bebida_preferida=cliente.bebida_preferida,
        notas=cliente.notas,
        fecha_registro=datetime.now(),
    )
    clientes.append(nuevo_cliente)
    next_id += 1
    return nuevo_cliente


@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return clientes


@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, datos: ClienteUpdate):
    for cliente in clientes:
        if cliente.id == cliente_id:
            if datos.servicio is not None and datos.servicio not in SERVICIOS_DISPONIBLES:
                raise HTTPException(status_code=400, detail="Servicio no válido")
            if datos.bebida_preferida is not None and datos.bebida_preferida not in BEBIDAS_DISPONIBLES:
                raise HTTPException(status_code=400, detail="Bebida no válida")

            actualizaciones = datos.model_dump(exclude_unset=True)
            for campo, valor in actualizaciones.items():
                setattr(cliente, campo, valor)
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    for i, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            clientes.pop(i)
            return {"mensaje": "Cliente eliminado"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")
