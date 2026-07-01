from fastapi import FastAPI, HTTPException, status

from models import Cliente, ClienteCreate, ClienteUpdate

app = FastAPI(title="Estética de Uñas API")

clientes_db: list[Cliente] = []
siguiente_id: int = 1


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


@app.put("/clientes/{cliente_id}", response_model=Cliente)
def actualizar_cliente(cliente_id: int, datos: ClienteUpdate):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            actualizacion = datos.model_dump(exclude_unset=True)
            for campo, valor in actualizacion.items():
                setattr(cliente, campo, valor)
            return cliente
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
