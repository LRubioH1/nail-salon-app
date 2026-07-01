from fastapi import FastAPI, HTTPException, status

from models import BEBIDAS_VALIDAS, Cliente, ClienteCreate, ClienteUpdate, Servicio

app = FastAPI(title="Estética de Uñas API")

clientes_db: list[Cliente] = []
siguiente_id: int = 1

servicios_db: list[Servicio] = [
    Servicio(id=1, nombre_servicio="Aplicación de gelish"),
    Servicio(id=2, nombre_servicio="Esmalte con calcio"),
    Servicio(id=3, nombre_servicio="Decoración de uñas"),
    Servicio(id=4, nombre_servicio="Remoción de esmalte"),
]


@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de la Estética de Uñas"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/clientes", response_model=Cliente, status_code=status.HTTP_201_CREATED)
def registrar_cliente(cliente: ClienteCreate):
    global siguiente_id
    nuevo_cliente = Cliente(id=siguiente_id, **cliente.model_dump())
    clientes_db.append(nuevo_cliente)
    siguiente_id += 1
    return nuevo_cliente


@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return clientes_db


@app.get("/clientes/{cliente_id}", response_model=Cliente)
def consultar_cliente(cliente_id: int):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")


@app.delete("/clientes/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(cliente_id: int):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            clientes_db.remove(cliente)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")


@app.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, datos: ClienteUpdate):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            actualizacion = datos.model_dump(exclude_unset=True)
            for campo, valor in actualizacion.items():
                setattr(cliente, campo, valor)
            return cliente
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")


@app.get("/servicios", response_model=list[Servicio])
def listar_servicios():
    return servicios_db


bebidas_db: list[str] = BEBIDAS_VALIDAS


@app.get("/bebidas", response_model=list[str])
def listar_bebidas():
    return bebidas_db
