# MySQL - Crear usuario, base de datos y tabla

Prerequisito: estar conectado a MySQL desde DBeaver con el usuario root.

Abrir SQL Editor: clic derecho en la conexion > **SQL Editor** > **Open SQL Script**

---

## 1. Crear la base de datos

```sql
CREATE DATABASE academia;
```

## 2. Crear un usuario

```sql
CREATE USER 'alumno'@'%' IDENTIFIED BY 'alumno123';
GRANT ALL PRIVILEGES ON academia.* TO 'alumno'@'%';
FLUSH PRIVILEGES;
```

- `'alumno'@'%'` — el `%` permite conectarse desde cualquier IP (necesario porque MySQL corre dentro de un contenedor Docker)
- `GRANT ALL PRIVILEGES ON academia.*` — le da permisos completos solo sobre la base de datos `academia`
- `FLUSH PRIVILEGES` — aplica los cambios de permisos inmediatamente

## 3. Crear la tabla alumnos

```sql
USE academia;

CREATE TABLE alumnos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    fecha_registro DATE DEFAULT (CURRENT_DATE)
);
```

## 4. Insertar datos de prueba

```sql
INSERT INTO alumnos (nombre, apellido, email) VALUES
('Juan', 'Lopez', 'juan@mail.com'),
('Maria', 'Garcia', 'maria@mail.com'),
('Carlos', 'Hernandez', 'carlos@mail.com');

SELECT * FROM alumnos;
```

Para ejecutar cada bloque en DBeaver: selecciona las lineas y presiona **Ctrl + Enter**.

---

## Conexion con el nuevo usuario

Puedes crear una segunda conexion en DBeaver usando el usuario que acabas de crear:

```
Host:     localhost
Puerto:   3306
Usuario:  alumno
Password: alumno123
Database: academia
```
