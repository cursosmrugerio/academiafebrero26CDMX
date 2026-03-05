# Guia de Scrum - Aprendiendo mientras desarrollamos TechShop

## Que es Scrum?

Scrum es un marco de trabajo agil para desarrollar software de forma incremental.
En lugar de intentar construir todo de una vez, divides el trabajo en ciclos cortos
llamados **sprints**, y al final de cada uno entregas algo funcional.

---

## Conceptos aprendidos

### Epic

Un **Epic** es un objetivo grande que NO puedes completar en un solo sprint.
Funciona como un "tema" o "categoria de trabajo" que agrupa varias historias de usuario.

Ejemplo en TechShop:
- TECH-1: "Sprint 1 - Los cimientos y el catalogo" (Epic)
- TECH-2: "Sprint 2 - La experiencia de compra" (Epic)
- TECH-3: "Sprint 3 - Batch, testing y calidad" (Epic)

### Historia de Usuario

Un pedazo de trabajo concreto que SI puedes completar en un sprint.
Se escribe desde la perspectiva de quien la necesita:

> *"Como **[quien]**, quiero **[que]** para **[por que]**"*

Ejemplos en TechShop:
- TECH-5: "Como admin, quiero gestionar categorias para organizar los productos"
- TECH-7: "Como cliente, quiero ver el catalogo de productos"

Nota: A veces hay historias tecnicas que no siguen el formato clasico,
como TECH-4: "Estructura del proyecto Spring Boot". Son trabajo necesario
pero no representan funcionalidad directa para un usuario.

### Epic vs Historia de Usuario

```
Epic (grande, no cabe en un sprint)
├── Historia de Usuario (mediana, cabe en un sprint)
├── Historia de Usuario
└── Historia de Usuario
```

La jerarquia en nuestro proyecto:

```
TECH-1 (Epic: "Catalogo")
├── TECH-4  Estructura Spring Boot
├── TECH-5  Gestionar categorias
├── TECH-6  CRUD productos
├── TECH-7  Ver catalogo
└── TECH-8  Configurar Swagger

TECH-2 (Epic: "Compra")
├── TECH-9  Registro de usuarios
├── TECH-10 Carrito de compras
├── TECH-11 Realizar pedido
├── TECH-12 Consultar ordenes
└── TECH-13 Swagger Sprint 2

TECH-3 (Epic: "Batch + Calidad")
├── TECH-14 Carga masiva CSV
├── TECH-15 Tests unitarios
├── TECH-16 Swagger final
└── TECH-17 Demo final
```

### Sprint

Periodo fijo de trabajo (tipicamente 1 a 4 semanas) donde el equipo se compromete
a entregar un conjunto de historias terminadas. Al final del sprint se hace una **demo**
para mostrar lo que funciona.

En TechShop tenemos 3 sprints:
- Sprint 1: Catalogo (MongoDB, productos, categorias)
- Sprint 2: Compra (usuarios, carrito, ordenes con MySQL)
- Sprint 3: Batch + Calidad (Spring Batch, testing, Swagger completo)

### Product Backlog

Lista **priorizada** de TODO el trabajo pendiente del proyecto. Lo mantiene
el Product Owner y contiene todas las historias de usuario ordenadas por prioridad.

En TechShop: las 14 historias (TECH-4 a TECH-17).

### Sprint Backlog

Subconjunto del Product Backlog que el equipo elige para trabajar en UN sprint especifico.

Ejemplo: el Sprint Backlog del Sprint 1 son TECH-4, TECH-5, TECH-6, TECH-7 y TECH-8.

### Estado de una Historia

Cada historia pasa por estos estados en Jira:

```
Tareas por hacer  -->  En progreso  -->  Listo
```

- **Tareas por hacer**: Aun no se empieza
- **En progreso**: Alguien esta trabajando en ella
- **Listo**: Completada y funcionando

### Demo

Sesion al final de cada sprint donde se muestra el software funcionando.
No es una presentacion de PowerPoint, es una demostracion en vivo.

Ejemplo Sprint 1: abrir Swagger, crear categorias, crear productos, listar por categoria.

### Incremento

El **Incremento** es el resultado tangible de un sprint: software funcionando que se
puede entregar al usuario. No es codigo a medias ni "falta solo el deploy" — es algo
que alguien puede ejecutar y probar.

Cada incremento se construye sobre el anterior:

```
Sprint 1 → Incremento v1.0.0 (catalogo funcionando)
Sprint 2 → Incremento v2.0.0 (catalogo + compra funcionando)
Sprint 3 → Incremento v3.0.0 (todo el ecommerce funcionando)
```

En TechShop, el incremento se entrega como un Docker Compose completo.
El evaluador ejecuta `docker compose up -d`, abre Swagger, y prueba todo lo
que se construyo hasta ese sprint. No necesita instalar Java, Maven ni bases de datos.

Esto se alinea con el principio de Scrum: *"El software funcionando es la medida
principal de progreso"*.

### Definition of Done (DoD)

Lista de criterios que una historia de usuario debe cumplir para considerarse **terminada**.
No basta con que "el codigo funcione" — debe cumplir un estandar de calidad.

En TechShop, nuestra Definition of Done es:

1. **Codigo implementado** — la funcionalidad que pide la historia esta completa
2. **Tests unitarios** — el servicio tiene tests con Mockito
3. **Tests de integracion** — el controlador tiene tests con MockMvc
4. **Coverage >= 80%** — medido con JaCoCo; si baja de 80%, el build falla
5. **Sin errores de compilacion** — `mvn clean verify` pasa correctamente
6. **Historia movida a "Listo"** en Jira

Por que importa el DoD? Porque evita el clasico "ya esta, solo falta testearlo"
que en realidad significa "no esta terminado". Si no tiene tests, no esta listo.

---

## Flujo de trabajo que seguimos

```
1. Tomar una historia       -->  Moverla a "En progreso" en Jira
2. Desarrollar el codigo    -->  Implementar lo que pide la historia
3. Completar                -->  Moverla a "Listo" en Jira
4. Siguiente historia       -->  Repetir
5. Al terminar el sprint    -->  Demo de lo construido
```

---

## Diario de aprendizaje

| Fecha | Concepto | Contexto |
|---|---|---|
| 2026-03-05 | Epic, Historia de Usuario, Sprint, Backlog, Estado, Demo | Antes de iniciar TECH-4 |
| 2026-03-05 | Definition of Done (DoD) | Decidimos estrategia de testing desde Sprint 1 |
| 2026-03-05 | Incremento | Decidimos Dockerizar la app para entregas incrementales por sprint |

