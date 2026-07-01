# Progreso del proyecto

## Fase 1: Preparación del proyecto — COMPLETADA (2026-06-30)

- Creado `main.py` con la instancia base de FastAPI.
- Creado `requirements.txt` con `fastapi` y `uvicorn`.
- Creado `render.yaml` con la configuración de despliegue en Render.
- Creado `README.md` con instrucciones básicas de ejecución.

Nota: el proyecto se reinició desde cero por decisión explícita del usuario, descartando una implementación previa (commit inicial) que ya cubría varias fases del plan.

## Fase 2: Crear la aplicación base en FastAPI — COMPLETADA (2026-06-30)

- Añadida ruta `GET /` con mensaje de bienvenida.
- Añadida ruta `GET /health` para verificar el funcionamiento de la aplicación.
- Verificado con `TestClient` que ambas rutas responden con código 200.

## Fase 3: Definir modelos de datos — COMPLETADA (2026-06-30)

- Creado `models.py` con modelos Pydantic.
- `Servicio`/`ServicioBase`: `id`, `nombre_servicio`, `descripcion` (opcional).
- `Cliente`/`ClienteBase`: `id`, `nombre`, `telefono`, `servicio`, `bebida_preferida`, `notas` (opcional), `fecha_registro` (autogenerada).
- `ClienteCreate` para el body de creación y `ClienteUpdate` con todos los campos opcionales para actualizaciones parciales.
- Verificado que el módulo importa correctamente.

## Fase 4: Crear almacenamiento temporal en memoria — COMPLETADA (2026-06-30)

- Añadida en `main.py` la lista `clientes_db: list[Cliente]` para almacenar clientes en memoria.
- Añadido el contador `siguiente_id` para generar IDs autoincrementales.
- Verificado que `main.py` importa correctamente y expone ambas variables.

### Próxima fase
Fase 5: Registrar clientes (ruta `POST /clientes`).

## Fase 5: Registrar clientes — COMPLETADA (2026-06-30)

- Añadida ruta `POST /clientes` en `main.py` que recibe un `ClienteCreate`, genera el `id` con `siguiente_id`, crea el `Cliente` y lo agrega a `clientes_db`.
- Responde con código `201` y el cliente creado (incluyendo `id` y `fecha_registro` autogenerados).
- Verificado con `TestClient` que el registro funciona correctamente.

### Próxima fase
Fase 6: Consultar clientes (rutas `GET /clientes` y `GET /clientes/{cliente_id}`).

## Fase 6: Consultar clientes — COMPLETADA (2026-06-30)

- Añadida ruta `GET /clientes` que devuelve la lista completa de `clientes_db`.
- Añadida ruta `GET /clientes/{cliente_id}` que busca el cliente por ID y devuelve `404` con mensaje "Cliente no encontrado" si no existe.
- Verificado con `TestClient`: listar clientes, consultar por ID existente y por ID inexistente (404).

### Próxima fase
Fase 7: Actualizar información del cliente (ruta `PUT /clientes/{cliente_id}`).

## Fase 7: Actualizar información del cliente — COMPLETADA (2026-06-30)

- Añadida ruta `PUT /clientes/{cliente_id}` en `main.py` que recibe un `ClienteUpdate` (todos los campos opcionales) y actualiza únicamente los campos enviados (`exclude_unset=True`).
- Responde con `404` y mensaje "Cliente no encontrado" si el ID no existe.
- Verificado con `TestClient`: actualización parcial de un cliente existente y actualización de un ID inexistente (404).

### Próxima fase
Fase 8: Eliminar clientes (ruta `DELETE /clientes/{cliente_id}`).
