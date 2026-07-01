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

## Fase 8: Eliminar clientes — COMPLETADA (2026-06-30)

- Añadida ruta `DELETE /clientes/{cliente_id}` en `main.py` que elimina el cliente de `clientes_db` y responde con `204 No Content`.
- Responde con `404` y mensaje "Cliente no encontrado" si el ID no existe.
- Verificado con `TestClient`: eliminación de un cliente existente (204, luego 404 al consultarlo) y eliminación de un ID inexistente (404).

### Próxima fase
Fase 9: Consultar catálogo de servicios (ruta `GET /servicios`).

## Fase 9: Consultar catálogo de servicios — COMPLETADA (2026-06-30)

- Añadida en `main.py` la lista fija `servicios_db: list[Servicio]` con los 4 servicios iniciales del catálogo (gelish, esmalte con calcio, decoración de uñas, remoción de esmalte).
- Añadida ruta `GET /servicios` que devuelve el catálogo completo.
- Verificado con `TestClient` que la ruta responde `200` con los 4 servicios.

### Próxima fase
Fase 10: Consultar catálogo de bebidas (ruta `GET /bebidas`).

## Fase 10: Consultar catálogo de bebidas — COMPLETADA (2026-06-30)

- Añadida en `main.py` la lista fija `bebidas_db: list[str]` con las 4 bebidas iniciales (Café, Té, Refresco, Agua).
- Añadida ruta `GET /bebidas` que devuelve el catálogo completo.
- Verificado con `TestClient` que la ruta responde `200` con las 4 bebidas.

### Próxima fase
Fase 11: Validaciones básicas (nombre/teléfono no vacíos, servicio y bebida dentro del catálogo).

## Fase 11: Validaciones básicas — COMPLETADA (2026-06-30)

- Añadidas en `models.py` las constantes `SERVICIOS_VALIDOS` y `BEBIDAS_VALIDAS` como fuente única de verdad del catálogo.
- Añadidos `field_validator` en `ClienteBase` y `ClienteUpdate` para: nombre no vacío, teléfono no vacío, servicio dentro del catálogo, bebida dentro del catálogo.
- `main.py` actualizado para reutilizar `BEBIDAS_VALIDAS` en `bebidas_db`.
- Verificado con `TestClient`: nombre vacío devuelve `422`, servicio fuera de catálogo devuelve `422`, registro válido devuelve `201`.

### Próxima fase
Fase 12: Documentación automática con Swagger (rutas `/docs` y `/redoc`, ya generadas automáticamente por FastAPI; verificar que funcionan).

## Fase 12: Documentación automática con Swagger — COMPLETADA (2026-06-30)

- No se requirió código adicional: FastAPI genera automáticamente `/docs` (Swagger UI), `/redoc` (ReDoc) y `/openapi.json`.
- Verificado con `TestClient` que las tres rutas responden `200`.

### Próxima fase
Fase 13: Preparar archivos para Render (verificar `requirements.txt` y `render.yaml`, y el comando de inicio `uvicorn main:app --host 0.0.0.0 --port $PORT`).

## Fase 13: Preparar archivos para Render — COMPLETADA (2026-06-30)

- Verificado `requirements.txt` con las dependencias `fastapi` y `uvicorn`.
- Verificado `render.yaml` con `env: python`, `buildCommand: pip install -r requirements.txt` y `startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT`.
- Verificado que `main.py` importa correctamente (`python -c "import main"`).
- `README.md` ya incluye instrucciones de ejecución local.

### Próxima fase
Fase 14: Subir proyecto a GitHub (confirmar que `main.py`, `requirements.txt`, `render.yaml`, `README.md` y `PROJECT_PLAN.md` estén incluidos en el repositorio).

## Fase 14: Subir proyecto a GitHub — PARCIAL (2026-06-30)

- Confirmado que el repositorio ya tiene remoto configurado: `origin` → `https://github.com/LRubioH1/nail-salon-app.git`, rama `main` sincronizada con `origin/main`.
- Confirmado que `main.py`, `requirements.txt`, `render.yaml`, `README.md`, `models.py`, `docs/PROGRESS.md` y `docs/PROJECT_PLAN_uñas.md` están en el repositorio.
- Creado el commit local `18aed94` con los cambios de las Fases 2-13.
- **Pendiente**: el `git push origin main` falló porque no hay credenciales de GitHub configuradas en este entorno (no hay `/dev/tty` disponible ni `gh` CLI instalado). El usuario debe ejecutar `git push origin main` manualmente desde una terminal con sus credenciales configuradas.

### Próxima fase
Completar el push manual de la Fase 14 (pendiente de credenciales) y luego continuar con la Fase 15: Desplegar en Render.
