# Proyecto Final - Ecommerce

## Contexto
Proyecto final del curso de Java (academia BBVA). El objetivo es integrar todas las tecnologias
aprendidas en los modulos 5 y 6 en una aplicacion real: un ecommerce.

Autor: Miguel Rugerio (miguel.rugerio@outlook.com)
Fecha de inicio: 2026-03-04

---

## Decisiones Tomadas

### D001 - Stack tecnologico base
- **Fecha:** 2026-03-04
- **决:** Java 17 + Spring Boot 3.x + Maven
- **Razon:** Java 17 es LTS, compatible con Spring Boot 3.x, y es la version usada durante el curso.

### D002 - Bases de datos: MySQL + MongoDB
- **Fecha:** 2026-03-04
- **Decision:** Usar ambas bases de datos
  - **MySQL** → Datos transaccionales (usuarios, carrito, ordenes/pedidos)
  - **MongoDB** → Catalogo de productos (esquema flexible por categoria)
- **Razon:** Demostrar dominio de ambas tecnologias vistas en el curso. MongoDB permite que
  cada categoria de producto tenga atributos distintos sin alterar el esquema.

### D003 - Incluir Spring Batch
- **Fecha:** 2026-03-04
- **Decision:** Si, incluir un job de Spring Batch para carga masiva de productos desde CSV.
- **Razon:** Integrar Spring Batch en un caso de uso real del ecommerce.

### D004 - Documentacion con Swagger/OpenAPI
- **Fecha:** 2026-03-04
- **Decision:** Incluir Swagger para documentacion interactiva de la API REST.
- **Razon:** Ya se uso en ejercicios anteriores del curso. Facilita la prueba y demostracion de endpoints.

### D005 - Testing con JUnit 5 + Mockito
- **Fecha:** 2026-03-04
- **Decision:** Tests unitarios con Mockito para la capa de servicios.
- **Razon:** Tecnologias cubiertas en el modulo 5.

---

## Modulos del Ecommerce

| Modulo | BD | Descripcion |
|---|---|---|
| Usuarios | MySQL | Registro y autenticacion basica |
| Productos | MongoDB | CRUD completo con categorias |
| Carrito | MySQL | Agregar/quitar items, asociado a usuario |
| Ordenes | MySQL | Crear pedido desde carrito |
| Batch | - | Importar productos desde CSV |

## Endpoints REST planificados

| Metodo | Ruta | Descripcion |
|---|---|---|
| POST | /api/usuarios/registro | Registrar usuario |
| GET | /api/productos | Listar productos |
| GET | /api/productos/{id} | Detalle de producto |
| POST | /api/productos | Crear producto |
| PUT | /api/productos/{id} | Actualizar producto |
| DELETE | /api/productos/{id} | Eliminar producto |
| POST | /api/carrito/agregar | Agregar item al carrito |
| DELETE | /api/carrito/{itemId} | Quitar item del carrito |
| GET | /api/carrito/{usuarioId} | Ver carrito del usuario |
| POST | /api/ordenes | Crear orden desde carrito |
| GET | /api/ordenes/{id} | Consultar orden |

---

## Registro de Progreso

- [ ] Estructura inicial del proyecto (Maven, dependencias)
- [ ] Entidades y repositorios
- [ ] Servicios
- [ ] Controladores REST
- [ ] Spring Batch - job de carga de productos
- [ ] Tests unitarios
- [ ] Configuracion Swagger
- [ ] Pruebas de integracion
