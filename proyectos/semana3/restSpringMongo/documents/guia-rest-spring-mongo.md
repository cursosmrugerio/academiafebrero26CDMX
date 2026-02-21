# REST con Spring Boot y MongoDB - Guia de repaso

En la semana 1 construimos un CRUD REST de alumnos con Spring Boot y **MySQL**. Esta semana construimos el mismo CRUD pero con **MongoDB**. La arquitectura (Controller → Service → Repository) es identica. Lo que cambia es como Spring se conecta a la base de datos y como representa los datos.

Esta guia se enfoca unicamente en **lo que cambia** al usar MongoDB. Si necesitas repasar la arquitectura REST, los endpoints o las anotaciones de Spring Web (`@RestController`, `@GetMapping`, etc.), consulta la guia de semana 1.

---

## Que cambia y que NO cambia

### Lo que NO cambia (identico a MySQL)

- La arquitectura de 3 capas: Controller → Service → Repository
- Las anotaciones de Spring Web: `@RestController`, `@GetMapping`, `@PostMapping`, etc.
- La inyeccion de dependencias por constructor
- Los codigos HTTP de respuesta (200, 201, 204, 404)
- La clase main con `@SpringBootApplication`
- El flujo de una peticion: llega al Controller, baja al Service, llega al Repository

### Lo que SI cambia

| Aspecto | MySQL (semana 1) | MongoDB (semana 3) |
|---------|-------------------|---------------------|
| Dependencia Maven | `spring-boot-starter-data-jpa` + `mysql-connector-j` | `spring-boot-starter-data-mongodb` |
| Configuracion | `spring.datasource.*` + `spring.jpa.*` | `spring.data.mongodb.uri` |
| Anotacion de la entidad | `@Entity` + `@Table` | `@Document(collection = "...")` |
| Tipo del ID | `Integer` (autoincremental) | `String` (ObjectId de 24 caracteres) |
| Generacion del ID | `@GeneratedValue(IDENTITY)` — MySQL lo genera | MongoDB lo genera automaticamente, sin anotacion |
| Anotaciones de columnas | `@Column(nullable, length, name)` | No se necesitan |
| Repository | `JpaRepository<Alumno, Integer>` | `MongoRepository<Alumno, String>` |
| Puerto | 8080 | 8081 (para no chocar con MySQL) |

---

## Paso 1: pom.xml — una sola dependencia en lugar de dos

Con MySQL necesitabamos **dos** dependencias para la base de datos:

```xml
<!-- MySQL: DOS dependencias -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <scope>runtime</scope>
</dependency>
```

Con MongoDB necesitamos solo **una**:

```xml
<!-- MongoDB: UNA dependencia -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

**Por que?** Con MySQL, JPA es el framework de acceso a datos y el connector es el driver JDBC. Son dos cosas separadas. Con MongoDB, el starter de Spring Data MongoDB ya incluye todo: el driver de MongoDB y el framework de acceso a datos.

---

## Paso 2: application.properties — una URI en lugar de cuatro propiedades

Con MySQL necesitabamos configurar URL, usuario, password, driver y propiedades de JPA:

```properties
# MySQL: 6 lineas de configuracion
spring.datasource.url=jdbc:mysql://localhost:3306/academia
spring.datasource.username=root
spring.datasource.password=root123
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

Con MongoDB solo necesitamos **una linea** de conexion:

```properties
# MongoDB: 1 linea de configuracion
spring.data.mongodb.uri=mongodb://root:root123@localhost:27017/academia?authSource=admin
```

### Anatomia de la URI de MongoDB

```
mongodb://root:root123@localhost:27017/academia?authSource=admin
         ─────┬─────  ─────────┬────  ───┬───  ────────┬───────
          usuario:       host:puerto    base de    parametro de
          password                      datos      autenticacion
```

| Parte | Valor | Explicacion |
|-------|-------|-------------|
| `mongodb://` | Protocolo | Equivalente a `jdbc:mysql://` |
| `root:root123` | Credenciales | Usuario y password del contenedor Docker |
| `localhost:27017` | Host y puerto | Puerto default de MongoDB |
| `academia` | Base de datos | Donde se guardan las colecciones |
| `authSource=admin` | Parametro | Le dice a MongoDB que valide las credenciales contra la BD `admin` |

**`authSource=admin`** es necesario porque el usuario `root` se creo en la base de datos `admin` (que es la BD administrativa de MongoDB). Sin este parametro, MongoDB intenta autenticar en `academia` y falla.

### No hay `ddl-auto` ni `show-sql`

En MySQL, `hibernate.ddl-auto=update` le decia a JPA que creara o modificara las tablas automaticamente. En MongoDB **no existe este concepto**: las colecciones se crean automaticamente la primera vez que insertas un documento. No necesitas definir estructura.

---

## Paso 3: Entity — @Document en lugar de @Entity

Este es el cambio mas importante. En MySQL mapeabamos una **tabla relacional** con columnas fijas. En MongoDB mapeamos un **documento** en una coleccion.

### Version MySQL (semana 1)

```java
import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "alumnos")
public class Alumno {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(nullable = false, length = 100)
    private String nombre;

    @Column(nullable = false, length = 100)
    private String apellido;

    @Column(length = 150)
    private String email;

    @Column(name = "fecha_registro")
    private LocalDate fechaRegistro;

    // constructor, getters, setters...
}
```

### Version MongoDB (semana 3)

```java
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.time.LocalDate;

@Document(collection = "alumnos")
public class Alumno {

    @Id
    private String id;

    private String nombre;

    private String apellido;

    private String email;

    private LocalDate fechaRegistro;

    // constructor, getters, setters...
}
```

### Que cambio y por que

| Cambio | MySQL | MongoDB | Razon |
|--------|-------|---------|-------|
| Anotacion de clase | `@Entity` + `@Table(name)` | `@Document(collection)` | Diferente framework: JPA vs Spring Data MongoDB |
| Paquete de `@Id` | `jakarta.persistence.Id` | `org.springframework.data.annotation.Id` | Son anotaciones de frameworks diferentes |
| Tipo del ID | `Integer` | `String` | MongoDB usa ObjectId (24 caracteres hex), no enteros |
| Generacion del ID | `@GeneratedValue(IDENTITY)` | *(nada)* | MongoDB genera el ObjectId automaticamente sin necesidad de anotacion |
| Anotaciones de campo | `@Column(nullable, length, name)` | *(nada)* | MongoDB no tiene esquema fijo, no hay restricciones de columna |

### Sobre el ObjectId

En MySQL el ID era un numero autoincremental: `1`, `2`, `3`, `4`...

En MongoDB el ID es un **ObjectId** de 24 caracteres hexadecimales, por ejemplo:

```
6999f1f166bdc060715a3ad0
```

Este ObjectId lo genera MongoDB automaticamente al insertar un documento. Contiene informacion codificada:

```
6999f1f1  66bdc0  6071  5a3ad0
────┬───  ──┬──  ──┬─  ──┬───
timestamp  random  counter  random
(segundos)
```

**No necesitas generar ni asignar el ID manualmente.** Si el campo `id` es `null` cuando haces `save()`, MongoDB lo genera. Por eso no necesitamos `@GeneratedValue`.

### Sobre las anotaciones de campo

Con JPA (MySQL), las anotaciones `@Column` servian para:
- Definir restricciones: `nullable = false`, `length = 100`
- Mapear nombres diferentes: `@Column(name = "fecha_registro")` para el campo `fechaRegistro`

Con MongoDB **nada de esto aplica**:
- No hay esquema fijo, asi que no hay restricciones de columna en la BD
- Spring Data MongoDB usa directamente el nombre del atributo Java como nombre del campo en el documento
- `fechaRegistro` en Java se guarda como `fechaRegistro` en MongoDB (sin conversion a snake_case)

---

## Paso 4: Repository — MongoRepository en lugar de JpaRepository

### Version MySQL

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface AlumnoRepository extends JpaRepository<Alumno, Integer> {
}
```

### Version MongoDB

```java
import org.springframework.data.mongodb.repository.MongoRepository;

public interface AlumnoRepository extends MongoRepository<Alumno, String> {
}
```

### Que cambio

| Cambio | MySQL | MongoDB |
|--------|-------|---------|
| Interfaz padre | `JpaRepository` | `MongoRepository` |
| Tipo del ID | `Integer` | `String` |
| Paquete | `org.springframework.data.jpa.repository` | `org.springframework.data.mongodb.repository` |

### Los metodos son los mismos

Ambas interfaces heredan de `CrudRepository`, asi que los metodos CRUD son identicos:

| Metodo | Que hace | Equivalente MongoDB |
|--------|----------|---------------------|
| `findAll()` | Listar todos | `db.alumnos.find()` |
| `findById(id)` | Buscar por ID | `db.alumnos.find({_id: ObjectId("...")})` |
| `save(alumno)` | Insertar o actualizar | `db.alumnos.insertOne(...)` o `db.alumnos.replaceOne(...)` |
| `deleteById(id)` | Eliminar por ID | `db.alumnos.deleteOne({_id: ObjectId("...")})` |
| `existsById(id)` | Verificar si existe | `db.alumnos.countDocuments({_id: ObjectId("...")})` |

**Punto clave:** gracias a que Spring Data abstrae el acceso a datos, el Service y el Controller no saben (ni les importa) si la base de datos es MySQL o MongoDB. Usan los mismos metodos.

---

## Paso 5: Service y Controller — casi identicos

El Service y el Controller son practicamente iguales al proyecto MySQL. El unico cambio es el **tipo del ID**: donde antes decias `Integer`, ahora dices `String`.

### En el Service

```java
// MySQL:   public Optional<Alumno> buscarPorId(Integer id)
// MongoDB: public Optional<Alumno> buscarPorId(String id)

// MySQL:   public Optional<Alumno> actualizar(Integer id, Alumno datos)
// MongoDB: public Optional<Alumno> actualizar(String id, Alumno datos)

// MySQL:   public boolean eliminar(Integer id)
// MongoDB: public boolean eliminar(String id)
```

### En el Controller

```java
// MySQL:   public ResponseEntity<Alumno> buscarPorId(@PathVariable Integer id)
// MongoDB: public ResponseEntity<Alumno> buscarPorId(@PathVariable String id)
```

La logica interna no cambia nada. El `repository.findById()`, `repository.save()`, `repository.deleteById()` funcionan igual.

---

## Paso 6: Probar con Postman o curl

La app corre en **puerto 8081** (no 8080, para no chocar con el proyecto MySQL).

### Crear un alumno (POST)

```
POST http://localhost:8081/api/alumnos
Content-Type: application/json

{
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juan@correo.com"
}
```

Respuesta (201 Created):

```json
{
    "id": "6999f1f166bdc060715a3ad0",
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juan@correo.com",
    "fechaRegistro": "2026-02-21"
}
```

**Nota la diferencia:** el `id` ya no es `1` sino un ObjectId como `"6999f1f166bdc060715a3ad0"`.

### Buscar por ID (GET)

```
GET http://localhost:8081/api/alumnos/6999f1f166bdc060715a3ad0
```

Ahora el ID en la URL es un string de 24 caracteres, no un numero.

### Listar todos (GET)

```
GET http://localhost:8081/api/alumnos
```

### Actualizar (PUT)

```
PUT http://localhost:8081/api/alumnos/6999f1f166bdc060715a3ad0
Content-Type: application/json

{
    "nombre": "Juan Carlos",
    "apellido": "Perez Garcia",
    "email": "juancarlos@correo.com"
}
```

### Eliminar (DELETE)

```
DELETE http://localhost:8081/api/alumnos/6999f1f166bdc060715a3ad0
```

Respuesta: **204 No Content** (igual que MySQL).

---

## Verificar en MongoDB directamente

Puedes conectarte al contenedor de MongoDB para ver los documentos desde la shell:

```bash
docker exec -it mongo-academia mongosh -u root -p root123
```

Dentro de la shell de MongoDB:

```javascript
// Seleccionar la base de datos
use academia

// Ver todos los alumnos
db.alumnos.find()

// Ver alumnos con formato legible
db.alumnos.find().pretty()

// Contar documentos
db.alumnos.countDocuments()

// Buscar por nombre
db.alumnos.find({ nombre: "Juan" })
```

Tambien puedes ver los documentos desde **MongoDB Compass** conectandote con:

```
mongodb://root:root123@localhost:27017
```

---

## Como se guarda un alumno en MySQL vs MongoDB

### En MySQL (tabla con filas y columnas)

```
+----+--------+----------+-------------------+----------------+
| id | nombre | apellido | email             | fecha_registro |
+----+--------+----------+-------------------+----------------+
|  1 | Juan   | Perez    | juan@correo.com   | 2026-02-21     |
|  2 | Maria  | Lopez    | maria@correo.com  | 2026-02-21     |
+----+--------+----------+-------------------+----------------+
```

Todos los registros tienen exactamente las mismas columnas.

### En MongoDB (coleccion con documentos JSON)

```json
{
    "_id": ObjectId("6999f1f166bdc060715a3ad0"),
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juan@correo.com",
    "fechaRegistro": ISODate("2026-02-21"),
    "_class": "com.academia.rest.entity.Alumno"
}
```

**Notas:**
- `_id` es el nombre interno que MongoDB usa para el campo que mapeamos como `id` en Java
- `_class` es un campo que Spring Data MongoDB agrega automaticamente para saber que clase Java corresponde al documento. No lo defines tu, Spring lo agrega solo
- Los tipos de datos son nativos de MongoDB: `ObjectId` para IDs, `ISODate` para fechas

---

## Resumen: que hay que cambiar para migrar de MySQL a MongoDB

Si ya tienes un proyecto REST con MySQL y quieres crear la version con MongoDB, estos son los unicos cambios:

### 1. pom.xml
Reemplaza `spring-boot-starter-data-jpa` + `mysql-connector-j` por `spring-boot-starter-data-mongodb`.

### 2. application.properties
Reemplaza las propiedades `spring.datasource.*` y `spring.jpa.*` por una sola linea `spring.data.mongodb.uri`.

### 3. Entity
Cambia `@Entity` + `@Table` por `@Document(collection = "...")`. Cambia el ID de `Integer` a `String`. Quita `@GeneratedValue` y todas las `@Column`.

### 4. Repository
Cambia `JpaRepository<Alumno, Integer>` por `MongoRepository<Alumno, String>`.

### 5. Service y Controller
Cambia `Integer` por `String` en los parametros de ID. Nada mas.

**Todo lo demas queda igual.** La arquitectura REST, las anotaciones web, los codigos HTTP, la inyeccion de dependencias — nada de eso depende de la base de datos.

---

## Ejecucion desde linea de comando

### Prerequisitos

```bash
# Verificar que MongoDB esta corriendo en Docker
docker ps --filter name=mongo-academia

# Si no esta corriendo:
docker start mongo-academia
```

### Compilar y ejecutar

```bash
# Desde la carpeta del proyecto
cd proyectos/semana3/restSpringMongo

# Compilar
mvn clean package

# Ejecutar (opcion A: con Maven)
mvn spring-boot:run

# Ejecutar (opcion B: con el JAR)
java -jar target/rest-spring-mongo-1.0.0.jar
```

### Probar los endpoints con curl

```bash
# Crear un alumno
curl -X POST http://localhost:8081/api/alumnos \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Juan","apellido":"Perez","email":"juan@correo.com"}'

# Listar todos
curl http://localhost:8081/api/alumnos

# Buscar por ID (reemplaza el ObjectId con uno real)
curl http://localhost:8081/api/alumnos/6999f1f166bdc060715a3ad0

# Actualizar
curl -X PUT http://localhost:8081/api/alumnos/6999f1f166bdc060715a3ad0 \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Juan Carlos","apellido":"Perez","email":"juan@correo.com"}'

# Eliminar
curl -X DELETE http://localhost:8081/api/alumnos/6999f1f166bdc060715a3ad0
```

---

## Problemas comunes

### "Authentication failed" al arrancar la app

La URI de conexion esta mal o falta `?authSource=admin`. Verifica que sea exactamente:

```
mongodb://root:root123@localhost:27017/academia?authSource=admin
```

### "Connection refused" al arrancar la app

El contenedor de MongoDB no esta corriendo:

```bash
docker start mongo-academia
```

### El ID llega como `null` en el JSON de respuesta

Verifica que tu campo `id` tenga la anotacion `@Id` del paquete correcto: `org.springframework.data.annotation.Id` (no `jakarta.persistence.Id` que es de JPA).

### Al hacer POST, el campo `_class` aparece en MongoDB pero no en el JSON

Es normal. Spring Data MongoDB guarda `_class` internamente para saber el tipo Java del documento. No aparece en las respuestas REST porque tu clase `Alumno` no tiene un atributo `_class`.
