# MongoDB - Crear coleccion alumnos y ventajas de NoSQL

Prerequisito: estar conectado a MongoDB desde Compass con el connection string:
```
mongodb://root:root123@localhost:27017
```

En Compass, crea una base de datos `academia` con una coleccion `alumnos` (boton Create Database).

Luego abre la coleccion y usa el boton **Open MongoDB Shell** (parte superior) para ejecutar los comandos.

### Antes de ejecutar cualquier comando, selecciona la base de datos:

```javascript
use academia
```

Esto le indica a MongoDB en que base de datos vas a trabajar. Despues ya puedes usar `db.alumnos.find()`, `db.alumnos.insertOne(...)`, etc.

---

## En SQL todos los registros DEBEN tener la misma estructura

En MySQL, la tabla alumnos tiene columnas fijas:

```sql
CREATE TABLE alumnos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    email VARCHAR(150)
);
```

Si quieres que UN alumno tenga telefono y otro no, necesitas agregar la columna a TODOS:

```sql
ALTER TABLE alumnos ADD COLUMN telefono VARCHAR(20);
-- Ahora TODOS los alumnos tienen telefono (con valor NULL en la mayoria)
```

---

## En MongoDB cada documento puede tener estructura diferente

### Insert basico (equivalente al SQL)

```javascript
db.alumnos.insertOne({
    nombre: "Juan",
    apellido: "Lopez",
    email: "juan@mail.com"
})
```

### Un alumno con telefono y otro sin telefono - sin problema

```javascript
db.alumnos.insertMany([
    {
        nombre: "Maria",
        apellido: "Garcia",
        email: "maria@mail.com",
        telefono: "55-1234-5678"
    },
    {
        nombre: "Carlos",
        apellido: "Hernandez",
        email: "carlos@mail.com"
    }
])
```

Maria tiene telefono, Carlos no. No se necesito modificar ninguna estructura.

### Un alumno con multiples direcciones

En SQL necesitarias crear otra tabla `direcciones` con llaves foraneas. En MongoDB:

```javascript
db.alumnos.insertOne({
    nombre: "Ana",
    apellido: "Martinez",
    email: "ana@mail.com",
    direcciones: [
        { tipo: "casa", calle: "Reforma 100", ciudad: "CDMX" },
        { tipo: "trabajo", calle: "Insurgentes 500", ciudad: "CDMX" }
    ]
})
```

Todo en un solo documento. Sin JOINs.

### Un alumno con cursos y calificaciones

En SQL necesitarias minimo 3 tablas (`alumnos`, `cursos`, `inscripciones`). En MongoDB:

```javascript
db.alumnos.insertOne({
    nombre: "Roberto",
    apellido: "Diaz",
    email: "roberto@mail.com",
    cursos: [
        { nombre: "Java Basico", calificacion: 95, completado: true },
        { nombre: "Spring Boot", calificacion: null, completado: false },
        { nombre: "Docker", calificacion: 88, completado: true }
    ]
})
```

### Un alumno con datos completamente diferentes a los demas

```javascript
db.alumnos.insertOne({
    nombre: "Laura",
    apellido: "Sanchez",
    empresa: "Tech Corp",
    puesto: "Developer",
    experiencia_anios: 3,
    tecnologias: ["Java", "Python", "Docker", "AWS"],
    linkedin: "linkedin.com/in/laura-sanchez"
})
```

Este documento no tiene email ni cursos, pero tiene empresa, puesto y tecnologias. En la misma coleccion, sin errores.

---

## Consultas

### Ver todos los alumnos

```javascript
db.alumnos.find()
```

### Buscar por nombre

```javascript
db.alumnos.find({ nombre: "Ana" })
```

### Buscar alumnos que tengan telefono

```javascript
db.alumnos.find({ telefono: { $exists: true } })
```

### Buscar alumnos que sepan Java

```javascript
db.alumnos.find({ tecnologias: "Java" })
```

### Buscar alumnos con cursos completados con calificacion mayor a 90

```javascript
db.alumnos.find({ "cursos.calificacion": { $gt: 90 }, "cursos.completado": true })
```

---

## Resumen: SQL vs NoSQL

| Aspecto | SQL (MySQL) | NoSQL (MongoDB) |
|---------|-------------|-----------------|
| Estructura | Fija, definida por la tabla | Flexible, cada documento puede ser diferente |
| Agregar un campo | ALTER TABLE (afecta toda la tabla) | Solo agregalo al documento que lo necesite |
| Datos anidados | Requiere tablas extra + JOINs | Se guardan directamente en el documento |
| Listas/Arrays | Requiere tabla intermedia | Campo tipo array nativo |
| Esquema | Obligatorio antes de insertar | Opcional |
