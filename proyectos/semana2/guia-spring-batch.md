# Spring Batch - Guia paso a paso

---

## Que es Spring Batch?

Spring Batch es un framework para **procesamiento por lotes** (batch processing). Sirve para procesar grandes volumenes de datos de forma automatica, sin interaccion del usuario.

### Cuando se usa?

Imagina que trabajas en un banco y cada fin de mes necesitas:
- Leer 500,000 movimientos bancarios de un archivo
- Calcular comisiones e impuestos de cada movimiento
- Guardar los resultados en la base de datos

No vas a hacer eso manualmente. Tampoco vas a exponer un endpoint REST para eso. Necesitas un **proceso automatico** que lea, transforme y escriba miles de registros de forma eficiente y confiable. Para eso existe Spring Batch.

### Por que no simplemente un `for` con INSERTs?

Podrias leer un CSV con `BufferedReader`, recorrerlo con un `for` y hacer un INSERT por cada linea. Funcionaria para 10 registros. Pero con 500,000 registros necesitas:

- **Procesamiento por chunks** — no cargar todo en memoria, sino procesar de 50 en 50 o de 1000 en 1000
- **Tolerancia a fallos** — si falla en el registro 300,000, poder retomar desde ahi sin reprocesar los primeros 299,999
- **Historial** — saber cuando se ejecuto, cuanto tardo, cuantos registros proceso, si fallo o no

Spring Batch resuelve todo eso. Tu solo defines QUE leer, COMO transformar y DONDE escribir. El framework se encarga del resto.

---

## La analogia: una linea de produccion

Piensa en Spring Batch como una **fabrica con una linea de produccion**:

```
ALMACEN DE          LINEA DE              ALMACEN DE
MATERIA PRIMA  -->  PRODUCCION  -->       PRODUCTO TERMINADO
(CSV, BD, API)      (transformar)         (BD, CSV, PDF)
      |                  |                       |
   Reader            Processor               Writer
```

| Fabrica | Spring Batch | En nuestro proyecto |
|---------|-------------|-------------------|
| El gerente de planta que dice "arranquen" | **JobLauncher** | Spring Boot lo hace automaticamente |
| La orden de produccion completa | **Job** | `procesarEmpleadosJob` |
| Una estacion de trabajo en la linea | **Step** | `paso1` |
| El operario que trae la materia prima | **ItemReader** | Lee `empleados.csv` |
| El operario que transforma la pieza | **ItemProcessor** | Calcula bono y pone nombre en mayusculas |
| El operario que empaca el producto final | **ItemWriter** | Inserta en tabla MySQL |
| La bitacora donde anotan todo | **JobRepository** | Tablas `BATCH_*` en MySQL |

---

## Arquitectura de Spring Batch

Este es el diagrama que vimos en sesion:

```
                                          ItemReader       (lee datos de entrada)
                                        /
JobLauncher --> Job --> Step(s) --> ItemProcessor    (transforma cada registro)
                                        \
                                          ItemWriter       (escribe resultado)

                JobRepository  (guarda historial de ejecuciones en BD)
```

**Un Job tiene uno o mas Steps.** Cada Step tiene exactamente un Reader, un Processor (opcional) y un Writer.

**El JobRepository** no es codigo que tu escribas. Es un componente interno de Spring Batch que automaticamente guarda en la base de datos: cuando se ejecuto el Job, cuanto tardo, cuantos registros leyo, cuantos escribio, si fallo o tuvo exito. Esto permite retomar un Job fallido desde donde se quedo.

---

## Que vamos a construir

Una aplicacion que:
1. **Lee** un archivo CSV con 10 empleados
2. **Transforma** cada empleado: nombre en mayusculas + calculo de bono (10% del salario)
3. **Escribe** los resultados en una tabla MySQL

```
empleados.csv          EmpleadoProcessor          tabla empleados_procesados
+----------------+     +------------------+       +-------------------------+
| Juan Perez     | --> | JUAN PEREZ       |  -->  | JUAN PEREZ | 25000 | 2500 |
| Ventas         |     | Ventas           |       +-------------------------+
| 25000          |     | 25000            |
+----------------+     | bono: 2500       |
                       +------------------+
```

---

## Prerequisitos

- Docker Desktop corriendo con el contenedor `mysql-academia` iniciado
- Java 17 o superior instalado
- Maven instalado
- Eclipse (o IntelliJ / VS Code)
- DBeaver (o cualquier cliente MySQL)

Verificar que el contenedor MySQL esta corriendo:

```bash
docker ps
```

Debes ver `mysql-academia` con estado `Up`. Si no esta corriendo:

```bash
docker start mysql-academia
```

---

## Paso 1: Preparar la base de datos

Antes de escribir codigo, necesitamos crear la tabla donde Spring Batch va a escribir los resultados.

### 1.1 Dar permisos al usuario alumno

Abre DBeaver, conectate como **root** (`root` / `root123`) y ejecuta:

```sql
GRANT ALL PRIVILEGES ON academia.* TO 'alumno'@'%';
FLUSH PRIVILEGES;
```

> **Por que?** El usuario `alumno` necesita permisos para crear tablas y hacer INSERT/SELECT sobre la base de datos `academia`. Sin esto, la aplicacion falla con "Access denied".

### 1.2 Crear la tabla destino

Ahora conectate como **alumno** (`alumno` / `alumno123`, base de datos `academia`) y ejecuta:

```sql
USE academia;

CREATE TABLE empleados_procesados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    bono DECIMAL(10,2) NOT NULL
);
```

Verificar que se creo:

```sql
SHOW TABLES;
```

Debes ver `empleados_procesados` en la lista.

> **Nota:** Spring Batch tambien va a crear sus propias tablas (`BATCH_JOB_INSTANCE`, `BATCH_JOB_EXECUTION`, etc.) automaticamente cuando ejecutes la aplicacion. No necesitas crearlas tu.

---

## Paso 2: Crear el proyecto en Eclipse

### 2.1 Nuevo proyecto Maven

1. **File** > **New** > **Maven Project**
2. Marca la casilla **Create a simple project (skip archetype selection)**
3. Llena los campos:
   - **Group Id:** `com.academia`
   - **Artifact Id:** `spring-batch`
   - **Version:** `1.0.0`
   - **Packaging:** `jar`
4. Clic en **Finish**

### 2.2 Crear la estructura de paquetes

Clic derecho en `src/main/java` > **New** > **Package** y crea estos 3 paquetes:

```
com.academia.batch
com.academia.batch.model
com.academia.batch.processor
com.academia.batch.config
```

### 2.3 Crear la carpeta de recursos

Clic derecho en `src/main/resources` (ya debe existir). Aqui van el archivo de configuracion y el CSV.

### 2.4 Estructura final

```
spring-batch/
├── pom.xml
└── src/main/
    ├── java/com/academia/batch/
    │   ├── SpringBatchApplication.java
    │   ├── config/
    │   │   └── BatchConfig.java
    │   ├── model/
    │   │   └── Empleado.java
    │   └── processor/
    │       └── EmpleadoProcessor.java
    └── resources/
        ├── application.properties
        └── empleados.csv
```

---

## Paso 3: pom.xml (dependencias)

Abre el archivo `pom.xml` que Eclipse genero y **reemplaza todo su contenido** con esto:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.2</version>
        <relativePath/>
    </parent>

    <groupId>com.academia</groupId>
    <artifactId>spring-batch</artifactId>
    <version>1.0.0</version>
    <name>spring-batch</name>
    <description>Procesamiento por lotes con Spring Batch y MySQL</description>

    <properties>
        <java.version>17</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-batch</artifactId>
        </dependency>
        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <scope>runtime</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

**Que hay aqui:**

| Seccion | Que hace |
|---------|---------|
| `<parent>` | Hereda la configuracion base de Spring Boot 3.2.2 |
| `spring-boot-starter-batch` | Incluye todo lo necesario para Spring Batch (el framework, transacciones, JDBC) |
| `mysql-connector-j` | El driver JDBC para que Java se conecte a MySQL |
| `spring-boot-maven-plugin` | Permite ejecutar la app con `mvn spring-boot:run` |

Despues de pegar el contenido: clic derecho en el proyecto > **Maven** > **Update Project** (o `Alt+F5`).

---

## Paso 4: application.properties (configuracion)

Crea el archivo `application.properties` en `src/main/resources/`:

```properties
# Conexion a MySQL (contenedor docker mysql-academia)
spring.datasource.url=jdbc:mysql://localhost:3306/academia
spring.datasource.username=alumno
spring.datasource.password=alumno123
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# Spring Batch crea automaticamente las tablas BATCH_* en MySQL
spring.batch.jdbc.initialize-schema=always

# Ejecutar el Job automaticamente al iniciar la aplicacion
spring.batch.job.enabled=true
```

**Que hace cada propiedad:**

| Propiedad | Explicacion |
|-----------|-------------|
| `spring.datasource.url` | URL de conexion: protocolo `jdbc:mysql`, host `localhost`, puerto `3306`, base de datos `academia` |
| `spring.datasource.username` | Usuario de MySQL |
| `spring.datasource.password` | Contraseña de MySQL |
| `spring.datasource.driver-class-name` | Clase del driver JDBC de MySQL |
| `spring.batch.jdbc.initialize-schema=always` | Le dice a Spring Batch que cree sus tablas de metadata (`BATCH_*`) automaticamente al arrancar |
| `spring.batch.job.enabled=true` | Ejecuta el Job automaticamente cuando la app inicia, sin necesidad de llamarlo manualmente |

> **Importante:** Spring Boot lee este archivo al arrancar y crea automaticamente un objeto `DataSource` (conexion a la BD) que estara disponible para cualquier clase que lo necesite. No tienes que crear la conexion manualmente.

---

## Paso 5: empleados.csv (datos de entrada)

Crea el archivo `empleados.csv` en `src/main/resources/`:

```csv
nombre,departamento,salario
Juan Perez,Ventas,25000
Maria Lopez,TI,35000
Carlos Garcia,RRHH,28000
Ana Martinez,Ventas,27000
Pedro Sanchez,TI,32000
Laura Diaz,RRHH,30000
Roberto Flores,Ventas,26000
Sofia Ramirez,TI,38000
Diego Torres,RRHH,29000
Fernanda Rios,Ventas,31000
```

La primera linea (`nombre,departamento,salario`) son los **encabezados**. Spring Batch los usa para saber que columna corresponde a que campo del objeto Java. Por eso el Reader tiene `.linesToSkip(1)` — para saltar esta linea y no procesarla como dato.

---

## Paso 6: Empleado.java (el modelo)

Crea la clase `Empleado.java` en el paquete `com.academia.batch.model`:

```java
package com.academia.batch.model;

public class Empleado {

    private String nombre;
    private String departamento;
    private double salario;
    private double bono;

    public Empleado() {
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDepartamento() {
        return departamento;
    }

    public void setDepartamento(String departamento) {
        this.departamento = departamento;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public double getBono() {
        return bono;
    }

    public void setBono(double bono) {
        this.bono = bono;
    }

    @Override
    public String toString() {
        return nombre + " | " + departamento + " | Salario: " + salario + " | Bono: " + bono;
    }
}
```

**Puntos importantes:**

- Es un **POJO** (Plain Old Java Object): una clase simple con atributos, constructor vacio, getters y setters
- El **constructor vacio es obligatorio**: Spring Batch crea la instancia con `new Empleado()` y luego llena los campos con los setters
- Los nombres de los campos (`nombre`, `departamento`, `salario`) deben **coincidir exactamente** con los encabezados del CSV. Asi Spring Batch sabe que `setNombre()` se llena con la columna `nombre` del CSV
- El campo `bono` **no existe en el CSV**. Se calcula en el Processor y se asigna con `setBono()`. En el CSV empieza en `0.0` (valor default de `double`)

---

## Paso 7: EmpleadoProcessor.java (la transformacion)

Crea la clase `EmpleadoProcessor.java` en el paquete `com.academia.batch.processor`:

```java
package com.academia.batch.processor;

import com.academia.batch.model.Empleado;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.batch.item.ItemProcessor;

public class EmpleadoProcessor implements ItemProcessor<Empleado, Empleado> {

    private static final Logger log = LoggerFactory.getLogger(EmpleadoProcessor.class);

    @Override
    public Empleado process(Empleado empleado) {
        // Regla de negocio: nombre en mayusculas y bono del 10%
        empleado.setNombre(empleado.getNombre().toUpperCase());
        empleado.setBono(empleado.getSalario() * 0.10);

        log.info("Procesando: {}", empleado);
        return empleado;
    }
}
```

**Que esta pasando aqui:**

- La clase implementa `ItemProcessor<Empleado, Empleado>`
  - El **primer** `Empleado` es el tipo de entrada (lo que llega del Reader)
  - El **segundo** `Empleado` es el tipo de salida (lo que se envia al Writer)
  - Podrian ser tipos diferentes. Por ejemplo, leer un `EmpleadoCrudo` y devolver un `EmpleadoProcesado`. En nuestro caso usamos el mismo tipo
- El metodo `process()` se ejecuta **una vez por cada registro** del CSV (10 veces en nuestro caso)
- Si `process()` retorna `null`, ese registro se **descarta** y no llega al Writer. Esto es util para filtrar registros que no cumplan cierta condicion
- `log.info()` imprime en consola lo que esta pasando. Usamos SLF4J que es la libreria de logging que incluye Spring Boot

---

## Paso 8: BatchConfig.java (donde se conecta todo)

Crea la clase `BatchConfig.java` en el paquete `com.academia.batch.config`.

**Esta es la clase mas importante del proyecto.** Aqui defines los 5 componentes de Spring Batch y los conectas entre si.

```java
package com.academia.batch.config;

import com.academia.batch.model.Empleado;
import com.academia.batch.processor.EmpleadoProcessor;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.job.builder.JobBuilder;
import org.springframework.batch.core.repository.JobRepository;
import org.springframework.batch.core.step.builder.StepBuilder;
import org.springframework.batch.item.database.JdbcBatchItemWriter;
import org.springframework.batch.item.database.builder.JdbcBatchItemWriterBuilder;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.builder.FlatFileItemReaderBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.transaction.PlatformTransactionManager;

import javax.sql.DataSource;

@Configuration
public class BatchConfig {

    // ==================== READER ====================
    // Lee el archivo CSV linea por linea y convierte cada linea en un objeto Empleado
    @Bean
    public FlatFileItemReader<Empleado> leerCsv() {
        return new FlatFileItemReaderBuilder<Empleado>()
                .name("empleadoReader")
                .resource(new ClassPathResource("empleados.csv"))
                .delimited()
                .names("nombre", "departamento", "salario")
                .targetType(Empleado.class)
                .linesToSkip(1)
                .build();
    }

    // ==================== PROCESSOR ====================
    // Transforma cada Empleado: nombre en mayusculas y calcula el bono
    @Bean
    public EmpleadoProcessor procesarEmpleado() {
        return new EmpleadoProcessor();
    }

    // ==================== WRITER ====================
    // Inserta cada Empleado procesado en la tabla empleados_procesados de MySQL
    @Bean
    public JdbcBatchItemWriter<Empleado> escribirEnBd(DataSource dataSource) {
        return new JdbcBatchItemWriterBuilder<Empleado>()
                .sql("INSERT INTO empleados_procesados (nombre, departamento, salario, bono) "
                   + "VALUES (:nombre, :departamento, :salario, :bono)")
                .dataSource(dataSource)
                .beanMapped()
                .build();
    }

    // ==================== STEP ====================
    // Un Step = Reader + Processor + Writer, procesando en chunks de 3
    @Bean
    public Step paso1(JobRepository jobRepository,
                      PlatformTransactionManager transactionManager,
                      FlatFileItemReader<Empleado> leerCsv,
                      EmpleadoProcessor procesarEmpleado,
                      JdbcBatchItemWriter<Empleado> escribirEnBd) {

        return new StepBuilder("paso1", jobRepository)
                .<Empleado, Empleado>chunk(3, transactionManager)
                .reader(leerCsv)
                .processor(procesarEmpleado)
                .writer(escribirEnBd)
                .build();
    }

    // ==================== JOB ====================
    // El Job completo. En este caso solo tiene un Step.
    @Bean
    public Job procesarEmpleadosJob(JobRepository jobRepository, Step paso1) {
        return new JobBuilder("procesarEmpleadosJob", jobRepository)
                .start(paso1)
                .build();
    }
}
```

### Explicacion detallada

Esta clase tiene muchos conceptos nuevos. Vamos uno por uno.

---

### Que es `@Configuration`?

Le dice a Spring: "esta clase contiene definiciones de objetos que quiero que administres". Spring va a leer esta clase al arrancar y va a crear todos los objetos marcados con `@Bean`.

---

### Que es `@Bean`?

Cada metodo marcado con `@Bean` le dice a Spring: "ejecuta este metodo, toma el objeto que retorna, y guardalo para que cualquier otra clase lo pueda usar".

Es como un deposito. Tu defines como se construye cada pieza, y Spring las guarda en su contenedor para usarlas cuando se necesiten.

---

### De donde sale `DataSource`, `JobRepository` y `PlatformTransactionManager`?

Estos 3 objetos los crea **Spring Boot automaticamente** al arrancar la aplicacion:

| Objeto | De donde sale | Que es |
|--------|-------------|--------|
| `DataSource` | Spring Boot lo crea leyendo las propiedades `spring.datasource.*` del `application.properties` | La conexion a MySQL. Es como un pool de conexiones listas para usar |
| `JobRepository` | Spring Batch lo crea automaticamente usando el `DataSource` | El componente que guarda el historial de ejecuciones en las tablas `BATCH_*` |
| `PlatformTransactionManager` | Spring Boot lo crea automaticamente | Maneja las transacciones de BD (commit si todo sale bien, rollback si algo falla) |

**Tu no los creas.** Solo los recibes como parametros en tus metodos `@Bean` y Spring los inyecta automaticamente. A esto se le llama **inyeccion de dependencias**.

---

### Que hace cada metodo del Reader?

```java
.name("empleadoReader")                           // nombre interno para Spring Batch
.resource(new ClassPathResource("empleados.csv"))  // busca el archivo dentro de src/main/resources
.delimited()                                       // el archivo esta separado por comas (CSV)
.names("nombre", "departamento", "salario")        // nombres de las columnas, deben coincidir
                                                   // con los atributos del POJO Empleado
.targetType(Empleado.class)                        // convierte cada linea en un objeto Empleado
                                                   // usando los setters: setNombre(), setSalario()...
.linesToSkip(1)                                    // salta la primera linea (encabezados del CSV)
```

`ClassPathResource` significa "busca este archivo dentro de los recursos del proyecto" (la carpeta `src/main/resources`). Cuando Maven compila, copia todo lo de `resources/` al classpath.

---

### Que hace cada metodo del Writer?

```java
.sql("INSERT INTO empleados_procesados (...) VALUES (:nombre, :departamento, :salario, :bono)")
```

Los **`:nombre`**, **`:departamento`**, **`:salario`**, **`:bono`** son parametros con nombre. Spring Batch los reemplaza con los valores del objeto `Empleado`.

```java
.dataSource(dataSource)   // usa la conexion a MySQL que Spring creo automaticamente
.beanMapped()             // le dice a Spring Batch: "para llenar :nombre llama a getNombre(),
                          // para llenar :salario llama a getSalario()", etc.
                          // El mapeo es automatico por nombre: :campo → getCampo()
```

---

### Que es `chunk(3)`?

Spring Batch no procesa los 10 registros de golpe. Los procesa en **chunks** (pedazos):

```
Chunk 1:  lee 3 del CSV → procesa 3 → INSERT 3 en MySQL → COMMIT
Chunk 2:  lee 3 del CSV → procesa 3 → INSERT 3 en MySQL → COMMIT
Chunk 3:  lee 3 del CSV → procesa 3 → INSERT 3 en MySQL → COMMIT
Chunk 4:  lee 1 del CSV → procesa 1 → INSERT 1 en MySQL → COMMIT
```

**Por que chunks y no todo junto?**
- Si falla el chunk 3, los chunks 1 y 2 ya se guardaron. Solo se pierden 3 registros, no los 10
- Con 500,000 registros no quieres cargar todo en memoria. Con chunks de 1000, solo tienes 1000 en memoria a la vez

El numero 3 es para fines didacticos. En produccion se usan chunks de 100, 500 o 1000.

---

## Paso 9: SpringBatchApplication.java (clase main)

Crea la clase `SpringBatchApplication.java` en el paquete `com.academia.batch`:

```java
package com.academia.batch;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class SpringBatchApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringBatchApplication.class, args);
    }
}
```

Es la clase main estandar de Spring Boot. `@SpringBootApplication` hace 3 cosas:
1. Escanea todos los paquetes buscando clases con `@Configuration`, `@Bean`, `@Component`, etc.
2. Auto-configura Spring Boot (crea el `DataSource`, `JobRepository`, etc.)
3. Habilita la configuracion de Spring

Al ejecutar `main()`, Spring Boot:
1. Lee `application.properties`
2. Crea la conexion a MySQL (`DataSource`)
3. Encuentra `BatchConfig` y crea los beans (Reader, Processor, Writer, Step, Job)
4. Como `spring.batch.job.enabled=true`, el `JobLauncher` ejecuta el Job automaticamente

---

## Paso 10: Ejecutar la aplicacion

### Desde Eclipse

1. Clic derecho en `SpringBatchApplication.java`
2. **Run As** > **Java Application**

### Desde la terminal

Desde la carpeta raiz del proyecto:

```bash
mvn spring-boot:run
```

### Resultado esperado en consola

Entre todos los logs de Spring Boot, debes ver estas lineas:

```
Job: [SimpleJob: [name=procesarEmpleadosJob]] launched with the following parameters: [{}]
Executing step: [paso1]
Procesando: JUAN PEREZ | Ventas | Salario: 25000.0 | Bono: 2500.0
Procesando: MARIA LOPEZ | TI | Salario: 35000.0 | Bono: 3500.0
Procesando: CARLOS GARCIA | RRHH | Salario: 28000.0 | Bono: 2800.0
Procesando: ANA MARTINEZ | Ventas | Salario: 27000.0 | Bono: 2700.0
Procesando: PEDRO SANCHEZ | TI | Salario: 32000.0 | Bono: 3200.0
Procesando: LAURA DIAZ | RRHH | Salario: 30000.0 | Bono: 3000.0
Procesando: ROBERTO FLORES | Ventas | Salario: 26000.0 | Bono: 2600.0
Procesando: SOFIA RAMIREZ | TI | Salario: 38000.0 | Bono: 3800.0
Procesando: DIEGO TORRES | RRHH | Salario: 29000.0 | Bono: 2900.0
Procesando: FERNANDA RIOS | Ventas | Salario: 31000.0 | Bono: 3100.0
Step: [paso1] executed in 59ms
Job: [SimpleJob: [name=procesarEmpleadosJob]] completed with the following parameters: [{}] and the following status: [COMPLETED]
```

Si ves `COMPLETED` al final, todo funciono correctamente.

---

## Paso 11: Verificar los resultados en MySQL

Abre DBeaver conectado como **alumno** y ejecuta estas consultas:

### 11.1 Ver los empleados procesados

```sql
SELECT * FROM empleados_procesados;
```

Resultado esperado:

| id | nombre | departamento | salario | bono |
|----|--------|-------------|---------|------|
| 1 | JUAN PEREZ | Ventas | 25000.00 | 2500.00 |
| 2 | MARIA LOPEZ | TI | 35000.00 | 3500.00 |
| 3 | CARLOS GARCIA | RRHH | 28000.00 | 2800.00 |
| 4 | ANA MARTINEZ | Ventas | 27000.00 | 2700.00 |
| 5 | PEDRO SANCHEZ | TI | 32000.00 | 3200.00 |
| 6 | LAURA DIAZ | RRHH | 30000.00 | 3000.00 |
| 7 | ROBERTO FLORES | Ventas | 26000.00 | 2600.00 |
| 8 | SOFIA RAMIREZ | TI | 38000.00 | 3800.00 |
| 9 | DIEGO TORRES | RRHH | 29000.00 | 2900.00 |
| 10 | FERNANDA RIOS | Ventas | 31000.00 | 3100.00 |

Los nombres estan en mayusculas y cada bono es el 10% del salario. Esto confirma que el Processor funciono.

### 11.2 Ver las tablas que creo Spring Batch

```sql
SHOW TABLES LIKE 'BATCH%';
```

Estas tablas las creo Spring Batch automaticamente (por la propiedad `initialize-schema=always`):

| Tabla | Que guarda |
|-------|-----------|
| `BATCH_JOB_INSTANCE` | Cada Job registrado (nombre unico) |
| `BATCH_JOB_EXECUTION` | Cada ejecucion de un Job (status, fecha inicio, fecha fin) |
| `BATCH_JOB_EXECUTION_PARAMS` | Los parametros con los que se ejecuto el Job |
| `BATCH_STEP_EXECUTION` | Cada ejecucion de cada Step (registros leidos, escritos, errores) |

### 11.3 Ver el historial de ejecucion del Job

```sql
SELECT JOB_INSTANCE_ID, STATUS, START_TIME, END_TIME
FROM BATCH_JOB_EXECUTION;
```

Aqui puedes ver que el Job se ejecuto y su status es `COMPLETED`.

### 11.4 Ver estadisticas del Step

```sql
SELECT STEP_NAME, READ_COUNT, WRITE_COUNT, COMMIT_COUNT, STATUS
FROM BATCH_STEP_EXECUTION;
```

| Campo | Valor | Significado |
|-------|-------|-------------|
| `READ_COUNT` | 10 | Leyo 10 registros del CSV |
| `WRITE_COUNT` | 10 | Escribio 10 registros en MySQL |
| `COMMIT_COUNT` | 4 | Hizo 4 commits (chunks de 3+3+3+1) |
| `STATUS` | COMPLETED | El Step termino exitosamente |

---

## Paso 12: Que pasa si ejecuto la app por segunda vez?

**Esto es importante.** Si ejecutas la aplicacion por segunda vez sin cambiar nada, vas a ver este error:

```
A job instance already exists and is complete for parameters={}
```

**Por que?** Spring Batch registra cada ejecucion en el `JobRepository`. Si un Job ya se ejecuto exitosamente con los mismos parametros (en nuestro caso, sin parametros `{}`), no lo vuelve a ejecutar. Esto es una **proteccion**: en produccion no quieres procesar el mismo archivo dos veces por accidente.

### Como re-ejecutar el Job

Para volver a ejecutar, necesitas limpiar los datos anteriores. Ejecuta estos scripts en DBeaver:

```sql
-- 1. Limpiar nuestros datos
DELETE FROM empleados_procesados;

-- 2. Limpiar el historial de Spring Batch (respetar el orden por las foreign keys)
DELETE FROM BATCH_STEP_EXECUTION_CONTEXT;
DELETE FROM BATCH_STEP_EXECUTION;
DELETE FROM BATCH_JOB_EXECUTION_CONTEXT;
DELETE FROM BATCH_JOB_EXECUTION_PARAMS;
DELETE FROM BATCH_JOB_EXECUTION;
DELETE FROM BATCH_JOB_INSTANCE;
```

Ahora puedes ejecutar la app de nuevo y procesara los 10 registros otra vez.

---

## Resumen: como se relaciona todo

```
application.properties
       |
       | (Spring Boot lee y crea automaticamente)
       v
   DataSource  ------>  JobRepository  ------>  tablas BATCH_* en MySQL
       |                     |
       |                     |
       v                     v
  BatchConfig (tu lo defines con @Bean)
       |
       |--- leerCsv()          = ItemReader       --> lee empleados.csv
       |--- procesarEmpleado() = ItemProcessor    --> transforma cada registro
       |--- escribirEnBd()     = ItemWriter       --> inserta en MySQL
       |--- paso1()            = Step             --> conecta Reader + Processor + Writer
       |--- procesarEmpleadosJob() = Job          --> contiene el Step
       |
       v
  JobLauncher (Spring Boot lo ejecuta automaticamente al arrancar)
```

| Componente | Clase/Config | Que hace |
|-----------|-------------|---------|
| **JobLauncher** | Auto-configurado por Spring Boot | Arranca el Job al iniciar la app |
| **Job** | `procesarEmpleadosJob` en BatchConfig | Define el trabajo completo |
| **Step** | `paso1` en BatchConfig | Un paso con Reader + Processor + Writer |
| **ItemReader** | `leerCsv()` — FlatFileItemReader | Lee empleados.csv linea por linea |
| **ItemProcessor** | `EmpleadoProcessor` | Nombre a mayusculas + calcula bono 10% |
| **ItemWriter** | `escribirEnBd()` — JdbcBatchItemWriter | Inserta en tabla empleados_procesados |
| **JobRepository** | Tablas BATCH_* en MySQL | Guarda historial de ejecuciones |

---

## Ejecucion completa desde linea de comando

Si prefieres trabajar sin Eclipse, puedes ejecutar todo el proyecto desde la terminal.

### 1. Verificar prerequisitos

```bash
# Java 17 o superior
java -version

# Maven
mvn -version

# Docker corriendo
docker ps
```

Si el contenedor MySQL no esta corriendo:

```bash
docker start mysql-academia
```

### 2. Preparar la base de datos desde terminal

Conectate a MySQL dentro del contenedor:

```bash
docker exec -it mysql-academia mysql -u root -proot123
```

Dentro de la consola de MySQL, ejecuta:

```sql
-- Dar permisos al usuario alumno (si no lo has hecho)
GRANT ALL PRIVILEGES ON academia.* TO 'alumno'@'%';
FLUSH PRIVILEGES;

-- Crear la tabla destino
USE academia;

CREATE TABLE IF NOT EXISTS empleados_procesados (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    departamento VARCHAR(50) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    bono DECIMAL(10,2) NOT NULL
);

exit;
```

### 3. Compilar el proyecto

Desde la carpeta raiz del proyecto (`springBatch/`):

```bash
# Compilar y empaquetar (genera el JAR en target/)
mvn clean package -DskipTests
```

Resultado esperado:

```
[INFO] BUILD SUCCESS
[INFO] -----------------------------------------------
```

Esto genera el archivo `target/spring-batch-1.0.0.jar`.

### 4. Ejecutar la aplicacion

**Opcion A** — con Maven (no necesita compilar antes):

```bash
mvn spring-boot:run
```

**Opcion B** — ejecutando el JAR directamente (necesita haber compilado con `mvn clean package`):

```bash
java -jar target/spring-batch-1.0.0.jar
```

Ambas opciones producen el mismo resultado. La opcion B es como se ejecutaria en un servidor de produccion.

### 5. Verificar resultados desde terminal

Conectate a MySQL como alumno:

```bash
docker exec -it mysql-academia mysql -u alumno -palumno123 academia
```

Dentro de la consola de MySQL:

```sql
-- Ver los empleados procesados
SELECT * FROM empleados_procesados;

-- Ver estadisticas del Step
SELECT STEP_NAME, READ_COUNT, WRITE_COUNT, COMMIT_COUNT, STATUS
FROM BATCH_STEP_EXECUTION;

exit;
```

### 6. Limpiar para re-ejecutar

```bash
docker exec -it mysql-academia mysql -u alumno -palumno123 academia -e "
DELETE FROM empleados_procesados;
DELETE FROM BATCH_STEP_EXECUTION_CONTEXT;
DELETE FROM BATCH_STEP_EXECUTION;
DELETE FROM BATCH_JOB_EXECUTION_CONTEXT;
DELETE FROM BATCH_JOB_EXECUTION_PARAMS;
DELETE FROM BATCH_JOB_EXECUTION;
DELETE FROM BATCH_JOB_INSTANCE;
"
```

Despues de limpiar, puedes volver a ejecutar con `mvn spring-boot:run` o `java -jar target/spring-batch-1.0.0.jar`.

---

## Problemas comunes

### "Access denied for user 'alumno'"
El usuario no tiene permisos. Conectate como **root** y ejecuta:
```sql
GRANT ALL PRIVILEGES ON academia.* TO 'alumno'@'%';
FLUSH PRIVILEGES;
```

### "Table 'empleados_procesados' doesn't exist"
No ejecutaste el script del Paso 1.2. Crea la tabla antes de ejecutar la app.

### "Communications link failure"
El contenedor MySQL no esta corriendo. Ejecuta:
```bash
docker start mysql-academia
```

### "A job instance already exists"
Ya ejecutaste el Job antes. Sigue las instrucciones del Paso 12 para limpiar y re-ejecutar.

### La app arranca pero no procesa nada
Verifica que `spring.batch.job.enabled=true` este en tu `application.properties`. Sin esta propiedad, el Job no se ejecuta automaticamente.

### "Could not resolve placeholder 'spring.datasource.url'"
El archivo `application.properties` no esta en la ruta correcta. Debe estar en `src/main/resources/`, no en otra carpeta.
