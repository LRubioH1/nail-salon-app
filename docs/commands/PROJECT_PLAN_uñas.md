# PROJECT_PLAN.md

# Proyecto: Aplicación sencilla para estética de uñas

## 1. Objetivo general

Construir una aplicación web sencilla para una estética de uñas que permita registrar clientes, asociarles servicios realizados o solicitados, guardar detalles adicionales como preferencia de bebida y consultar el historial básico de atención.

La aplicación se desarrollará con **Python** y **FastAPI**, y se desplegará en **Render**. En esta primera versión no se utilizará base de datos; los datos se manejarán temporalmente en memoria mientras la aplicación esté activa.

---

## 2. Alcance inicial del proyecto

La aplicación permitirá:

- Registrar clientes.
- Consultar la lista de clientes registrados.
- Consultar el detalle de un cliente específico.
- Registrar servicios para cada cliente.
- Manejar servicios disponibles de la estética.
- Guardar detalles adicionales del cliente.
- Registrar la preferencia de bebida del cliente.
- Preparar la estructura del proyecto para que más adelante pueda conectarse a una base de datos.
- Desplegar la aplicación en Render.

---

## 3. Tecnologías propuestas

- **Python 3.11 o superior**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Render** para despliegue
- **GitHub** para control de versiones y conexión con Render

---

## 4. Servicios disponibles

La aplicación manejará inicialmente los siguientes servicios:

- Aplicación de gelish
- Esmalte con calcio
- Decoración de uñas
- Remoción de esmalte

Estos servicios podrán manejarse como una lista fija dentro del código en la primera versión.

---

## 5. Preferencias de bebida

Cada cliente podrá tener registrada una preferencia de bebida. Las opciones iniciales serán:

- Café
- Té
- Refresco
- Agua

---

## 6. Datos principales del cliente

Cada cliente podrá tener los siguientes datos:

- ID del cliente
- Nombre completo
- Teléfono
- Servicio solicitado
- Preferencia de bebida
- Fecha de registro
- Notas adicionales

Ejemplos de notas adicionales:

- Color favorito
- Tipo de uñas preferido
- Alergias conocidas
- Si prefiere diseño discreto o llamativo
- Comentarios sobre citas anteriores

---

# Fases de construcción

---

## Fase 1: Preparación del proyecto

### Objetivo
Crear la estructura inicial del proyecto en Python usando FastAPI.

### Actividades

1. Crear una carpeta principal del proyecto.
2. Crear un entorno virtual de Python.
3. Instalar las dependencias necesarias.
4. Crear el archivo principal de la aplicación.
5. Crear el archivo de dependencias `requirements.txt`.
6. Crear el archivo de configuración para Render.

### Estructura inicial sugerida

```text
nail_salon_app/
│
├── main.py
├── requirements.txt
├── render.yaml
├── README.md
└── PROJECT_PLAN.md
```

### Resultado esperado

El proyecto tendrá una estructura básica lista para iniciar el desarrollo.

---

## Fase 2: Crear la aplicación base en FastAPI

### Objetivo
Crear una aplicación mínima que confirme que FastAPI funciona correctamente.

### Actividades

1. Importar FastAPI.
2. Crear la instancia principal de la aplicación.
3. Crear una ruta inicial `/`.
4. Crear una ruta de prueba `/health`.

### Rutas iniciales

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Mensaje de bienvenida |
| GET | `/health` | Verifica que la aplicación funciona |

### Resultado esperado

La aplicación responderá correctamente en el navegador o desde Swagger UI.

---

## Fase 3: Definir modelos de datos

### Objetivo
Crear los modelos principales usando Pydantic.

### Modelos sugeridos

#### Cliente

Campos sugeridos:

- `id`
- `nombre`
- `telefono`
- `servicio`
- `bebida_preferida`
- `notas`
- `fecha_registro`

#### Servicio

Campos sugeridos:

- `id`
- `nombre_servicio`
- `descripcion`

### Resultado esperado

La aplicación tendrá modelos claros para recibir y validar información.

---

## Fase 4: Crear almacenamiento temporal en memoria

### Objetivo
Guardar los clientes temporalmente sin usar base de datos.

### Actividades

1. Crear una lista vacía para almacenar clientes.
2. Crear un contador para generar IDs automáticos.
3. Guardar los registros mientras la aplicación esté encendida.

### Consideración importante

Como no se usará base de datos, los datos se perderán cuando la aplicación se reinicie o cuando Render reinicie el servicio.

### Resultado esperado

La aplicación podrá guardar clientes de forma temporal durante la ejecución.

---

## Fase 5: Registrar clientes

### Objetivo
Crear una ruta para registrar nuevos clientes.

### Ruta propuesta

| Método | Ruta | Descripción |
|---|---|---|
| POST | `/clientes` | Registra un nuevo cliente |

### Datos requeridos

- Nombre del cliente
- Teléfono
- Servicio solicitado
- Preferencia de bebida

### Datos opcionales

- Notas adicionales

### Resultado esperado

El sistema permitirá registrar clientes y devolverá la información del cliente creado con su ID.

---

## Fase 6: Consultar clientes

### Objetivo
Permitir la consulta de los clientes registrados.

### Rutas propuestas

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/clientes` | Lista todos los clientes |
| GET | `/clientes/{cliente_id}` | Consulta un cliente específico |

### Resultado esperado

La aplicación permitirá consultar todos los clientes o buscar uno por su ID.

---

## Fase 7: Actualizar información del cliente

### Objetivo
Permitir modificar los datos de un cliente registrado.

### Ruta propuesta

| Método | Ruta | Descripción |
|---|---|---|
| PUT | `/clientes/{cliente_id}` | Actualiza los datos de un cliente |

### Datos que podrían actualizarse

- Nombre
- Teléfono
- Servicio
- Bebida preferida
- Notas adicionales

### Resultado esperado

La aplicación permitirá corregir o actualizar información de los clientes.

---

## Fase 8: Eliminar clientes

### Objetivo
Permitir eliminar un cliente registrado.

### Ruta propuesta

| Método | Ruta | Descripción |
|---|---|---|
| DELETE | `/clientes/{cliente_id}` | Elimina un cliente |

### Resultado esperado

La aplicación permitirá borrar clientes cuando sea necesario.

---

## Fase 9: Consultar catálogo de servicios

### Objetivo
Crear una ruta para consultar los servicios disponibles de la estética.

### Ruta propuesta

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/servicios` | Lista los servicios disponibles |

### Servicios iniciales

- Aplicación de gelish
- Esmalte con calcio
- Decoración de uñas
- Remoción de esmalte

### Resultado esperado

La aplicación mostrará los servicios disponibles para que puedan asignarse a los clientes.

---

## Fase 10: Consultar catálogo de bebidas

### Objetivo
Crear una ruta para consultar las bebidas disponibles para los clientes.

### Ruta propuesta

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/bebidas` | Lista las bebidas disponibles |

### Bebidas iniciales

- Café
- Té
- Refresco
- Agua

### Resultado esperado

La aplicación mostrará las opciones de bebida que se pueden registrar como preferencia del cliente.

---

## Fase 11: Validaciones básicas

### Objetivo
Evitar registros incompletos o incorrectos.

### Validaciones sugeridas

- El nombre del cliente no debe estar vacío.
- El teléfono no debe estar vacío.
- El servicio debe pertenecer al catálogo definido.
- La bebida debe pertenecer al catálogo definido.
- Las notas adicionales pueden ser opcionales.

### Resultado esperado

La aplicación rechazará información inválida y mostrará mensajes de error claros.

---

## Fase 12: Documentación automática con Swagger

### Objetivo
Aprovechar la documentación automática que genera FastAPI.

### Rutas útiles

| Ruta | Descripción |
|---|---|
| `/docs` | Documentación interactiva Swagger UI |
| `/redoc` | Documentación alternativa ReDoc |

### Resultado esperado

El proyecto tendrá documentación visual para probar las rutas sin necesidad de crear una interfaz todavía.

---

## Fase 13: Preparar archivos para Render

### Objetivo
Crear los archivos necesarios para desplegar la aplicación en Render.

### Archivo `requirements.txt`

Dependencias iniciales:

```text
fastapi
uvicorn
```

### Comando de inicio para Render

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Archivo opcional `render.yaml`

Este archivo puede ayudar a configurar el servicio automáticamente en Render.

### Resultado esperado

El proyecto estará listo para subirse a GitHub y conectarse con Render.

---

## Fase 14: Subir proyecto a GitHub

### Objetivo
Guardar el proyecto en un repositorio para conectarlo con Render.

### Actividades

1. Crear un repositorio en GitHub.
2. Subir los archivos del proyecto.
3. Verificar que estén incluidos:
   - `main.py`
   - `requirements.txt`
   - `render.yaml`, si se decide usar
   - `README.md`
   - `PROJECT_PLAN.md`

### Resultado esperado

El código estará disponible en GitHub para poder desplegarse.

---

## Fase 15: Desplegar en Render

### Objetivo
Publicar la aplicación en internet usando Render.

### Actividades

1. Entrar a Render.
2. Crear un nuevo Web Service.
3. Conectar el repositorio de GitHub.
4. Seleccionar Python como entorno.
5. Configurar el comando de instalación.
6. Configurar el comando de inicio.
7. Desplegar la aplicación.
8. Probar las rutas `/`, `/health` y `/docs`.

### Resultado esperado

La aplicación estará publicada y accesible desde una URL de Render.

---

# Rutas finales sugeridas

| Método | Ruta | Función |
|---|---|---|
| GET | `/` | Inicio de la aplicación |
| GET | `/health` | Verificación de funcionamiento |
| POST | `/clientes` | Crear cliente |
| GET | `/clientes` | Consultar clientes |
| GET | `/clientes/{cliente_id}` | Consultar cliente por ID |
| PUT | `/clientes/{cliente_id}` | Actualizar cliente |
| DELETE | `/clientes/{cliente_id}` | Eliminar cliente |
| GET | `/servicios` | Consultar servicios disponibles |
| GET | `/bebidas` | Consultar bebidas disponibles |

---

# Ejemplo de registro de cliente

```json
{
  "nombre": "María López",
  "telefono": "5551234567",
  "servicio": "Aplicación de gelish",
  "bebida_preferida": "Café",
  "notas": "Prefiere tonos claros y decoración sencilla."
}
```

---

# Mejoras futuras

Una vez terminada la primera versión, se podrán agregar las siguientes mejoras:

1. Conexión a base de datos.
2. Login para administradores.
3. Registro de citas.
4. Calendario de servicios.
5. Historial de visitas por cliente.
6. Control de pagos.
7. Estados de cita, como pendiente, en proceso, terminada o cancelada.
8. Interfaz web sencilla.
9. Reportes de servicios más solicitados.
10. Recordatorios por WhatsApp o correo electrónico.

---

# Nota final

Esta primera versión será una aplicación mínima funcional. Permitirá registrar clientes y servicios sin base de datos, ideal para probar el flujo general antes de construir una versión más completa.
