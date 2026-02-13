# Instalacion de DBeaver Community

DBeaver es un cliente gratuito de bases de datos. Con una sola herramienta puedes conectarte a MySQL, MongoDB, PostgreSQL y muchas mas.

---

## Instalacion en Windows

1. Ve a [https://dbeaver.io/download/](https://dbeaver.io/download/)
2. Descarga **Windows (installer)**
3. Ejecuta el `.exe` y sigue el wizard con Next hasta finalizar

---

## Conectar a MySQL (Docker)

Prerequisito: el contenedor `mysql-academia` debe estar corriendo (`docker ps`).

1. Abre DBeaver
2. Clic en **Nueva Conexion** (icono de enchufe con +)
3. Selecciona **MySQL**
4. Llena los datos:

```
Host:     localhost
Puerto:   3306
Usuario:  root
Password: root123
```

5. Clic en **Test Connection** para verificar
6. Si pide descargar el driver, acepta
7. Clic en **Finalizar**

---

## Conectar a MongoDB (Docker)

Prerequisito: el contenedor `mongo-academia` debe estar corriendo (`docker ps`).

1. Clic en **Nueva Conexion**
2. Selecciona **MongoDB**
3. Llena los datos:

```
Host:     localhost
Puerto:   27017
Usuario:  root
Password: root123
```

4. En la pestaña **Authentication**, selecciona **SCRAM-SHA-256**
5. Clic en **Test Connection**
6. Si pide descargar el driver, acepta
7. Clic en **Finalizar**

---

## Uso basico

- **Ver tablas/colecciones**: Expande la conexion en el panel izquierdo > esquema/base de datos > tablas
- **Ejecutar queries**: Clic derecho en la conexion > SQL Editor > Open SQL Script
- **Ver datos de una tabla**: Doble clic sobre la tabla en el panel izquierdo
