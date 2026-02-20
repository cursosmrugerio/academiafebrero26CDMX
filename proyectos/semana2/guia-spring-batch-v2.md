# Spring Batch v2 - Job con dos Steps

## Que hay de nuevo en esta version?

En la v1 creamos un Job con un solo Step que leia un CSV y escribia en MySQL. En esta v2 agregamos un **segundo Step** que lee de MySQL y genera un CSV de reporte.

### Flujo completo

```
Step 1:  empleados.csv  →  procesar (bono + mayusculas)  →  tabla MySQL
Step 2:  tabla MySQL     →  calcular salario total        →  reporte-empleados.csv
```

### Que se aprende de nuevo

| Concepto | Donde se ve |
|----------|------------|
| Un Job puede tener **multiples Steps** | `.start(paso1).next(paso2)` en el Job |
| Los Steps se ejecutan **en orden** | paso1 primero, paso2 despues |
| La salida de un Step puede ser la **entrada del siguiente** | paso1 llena la tabla, paso2 la lee |
| **Diferentes tipos de Reader** | `FlatFileItemReader` (CSV) vs `JdbcCursorItemReader` (MySQL) |
| **Diferentes tipos de Writer** | `JdbcBatchItemWriter` (MySQL) vs `FlatFileItemWriter` (CSV) |
| El Processor puede tener **tipos diferentes** de entrada y salida | `ItemProcessor<Empleado, EmpleadoReporte>` |

### Analogia con la fabrica

En la v1 teniamos una sola estacion de trabajo. Ahora tenemos **dos estaciones en serie**:

```
Estacion 1 (Step 1)                    Estacion 2 (Step 2)
+----------------------------+         +----------------------------+
| Materia prima: CSV         |         | Materia prima: tabla MySQL |
| Operacion: bono+mayusculas |  --->   | Operacion: salario total   |
| Producto: tabla MySQL      |         | Producto: CSV de reporte   |
+----------------------------+         +----------------------------+
```

La estacion 2 no puede arrancar hasta que la estacion 1 termine. Spring Batch se encarga de este orden automaticamente.

---

## Prerequisitos

- Docker Desktop corriendo con el contenedor `mysql-academia` iniciado
- Java 17 o superior instalado
- Maven instalado
- Eclipse (o IntelliJ / VS Code)
- La tabla `empleados_procesados` creada (si seguiste la guia v1 ya la tienes)

Verificar que el contenedor MySQL esta corriendo:

```bash
docker ps
```

Si no esta corriendo:

```bash
docker start mysql-academia
```

> **Importante:** Si ya ejecutaste la v1 y la tabla tiene datos, limpia los datos antes de empezar. Ejecuta en DBeaver conectado como **alumno**:
> ```sql
> DELETE FROM empleados_procesados;
> ```

Si no tienes la tabla `empleados_procesados`, creala:

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

---

## Que cambia respecto a la v1?

Solo hay **3 archivos nuevos o modificados**. Todo lo demas es identico a la v1:

| Archivo | Cambio |
|---------|--------|
| `EmpleadoReporte.java` | **Nuevo** — modelo con campo `salarioTotal` para el reporte |
| `ReporteProcessor.java` | **Nuevo** — convierte `Empleado` a `EmpleadoReporte` |
| `BatchConfig.java` | **Modificado** — agrega Reader, Processor, Writer y Step del paso 2 |

---

## Estructura del proyecto

```
springBatchV2/
├── pom.xml                                          (igual que v1)
└── src/main/
    ├── java/com/academia/batch/
    │   ├── SpringBatchApplication.java              (igual que v1)
    │   ├── config/
    │   │   └── BatchConfig.java                     ★ MODIFICADO
    │   ├── model/
    │   │   ├── Empleado.java                        (igual que v1)
    │   │   └── EmpleadoReporte.java                 ★ NUEVO
    │   └── processor/
    │       ├── EmpleadoProcessor.java               (igual que v1)
    │       └── ReporteProcessor.java                ★ NUEVO
    └── resources/
        ├── application.properties                   (igual que v1)
        └── empleados.csv                            (igual que v1)
```

---

## Paso 1: Crear el proyecto en Eclipse

1. **File** > **New** > **Maven Project**
2. Marca la casilla **Create a simple project (skip archetype selection)**
3. Llena los campos:
   - **Group Id:** `com.academia`
   - **Artifact Id:** `spring-batch-v2`
   - **Version:** `1.0.0`
   - **Packaging:** `jar`
4. Clic en **Finish**

Crea los 4 paquetes en `src/main/java` (clic derecho > **New** > **Package**):

```
com.academia.batch
com.academia.batch.model
com.academia.batch.processor
com.academia.batch.config
```

---

## Paso 2: pom.xml

Abre el `pom.xml` que Eclipse genero y **reemplaza todo su contenido** con:

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
    <artifactId>spring-batch-v2</artifactId>
    <version>1.0.0</version>
    <name>spring-batch-v2</name>
    <description>Spring Batch con dos Steps: CSV a MySQL y MySQL a CSV</description>

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

Despues de pegar: clic derecho en el proyecto > **Maven** > **Update Project** (o `Alt+F5`).

---

## Paso 3: application.properties

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

---

## Paso 4: empleados.csv

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

---

## Paso 5: Empleado.java

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

Mismo modelo que la v1. Se usa en el Step 1 y como entrada del Step 2.

---

## Paso 6: EmpleadoReporte.java (NUEVO en v2)

Crea la clase `EmpleadoReporte.java` en el paquete `com.academia.batch.model`:

```java
package com.academia.batch.model;

// Modelo usado en el Step 2: agrega el campo salarioTotal para el reporte CSV
public class EmpleadoReporte {

    private String nombre;
    private String departamento;
    private double salario;
    private double bono;
    private double salarioTotal;

    public EmpleadoReporte() {
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

    public double getSalarioTotal() {
        return salarioTotal;
    }

    public void setSalarioTotal(double salarioTotal) {
        this.salarioTotal = salarioTotal;
    }

    @Override
    public String toString() {
        return nombre + " | " + departamento + " | Salario: " + salario
             + " | Bono: " + bono + " | Total: " + salarioTotal;
    }
}
```

**Por que un modelo nuevo?** El Step 2 genera un campo que no existe en `Empleado`: `salarioTotal` (la suma de salario + bono). En lugar de modificar el modelo original, creamos uno nuevo especifico para el reporte. Esto tambien demuestra que el **Processor puede recibir un tipo y devolver otro diferente**.

---

## Paso 7: EmpleadoProcessor.java

Crea la clase `EmpleadoProcessor.java` en el paquete `com.academia.batch.processor`:

```java
package com.academia.batch.processor;

import com.academia.batch.model.Empleado;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.batch.item.ItemProcessor;

// Step 1 - Processor: transforma el empleado leido del CSV
public class EmpleadoProcessor implements ItemProcessor<Empleado, Empleado> {

    private static final Logger log = LoggerFactory.getLogger(EmpleadoProcessor.class);

    @Override
    public Empleado process(Empleado empleado) {
        empleado.setNombre(empleado.getNombre().toUpperCase());
        empleado.setBono(empleado.getSalario() * 0.10);

        log.info("Step 1 - Procesando: {}", empleado);
        return empleado;
    }
}
```

Mismo processor que la v1. La unica diferencia es que el log dice `"Step 1 - "` para distinguirlo del Step 2 en la consola.

---

## Paso 8: ReporteProcessor.java (NUEVO en v2)

Crea la clase `ReporteProcessor.java` en el paquete `com.academia.batch.processor`:

```java
package com.academia.batch.processor;

import com.academia.batch.model.Empleado;
import com.academia.batch.model.EmpleadoReporte;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.batch.item.ItemProcessor;

// Step 2 - Processor: convierte Empleado a EmpleadoReporte calculando el salario total
// Nota: el tipo de entrada (Empleado) es diferente al tipo de salida (EmpleadoReporte)
public class ReporteProcessor implements ItemProcessor<Empleado, EmpleadoReporte> {

    private static final Logger log = LoggerFactory.getLogger(ReporteProcessor.class);

    @Override
    public EmpleadoReporte process(Empleado empleado) {
        EmpleadoReporte reporte = new EmpleadoReporte();
        reporte.setNombre(empleado.getNombre());
        reporte.setDepartamento(empleado.getDepartamento());
        reporte.setSalario(empleado.getSalario());
        reporte.setBono(empleado.getBono());
        reporte.setSalarioTotal(empleado.getSalario() + empleado.getBono());

        log.info("Step 2 - Reporte: {}", reporte);
        return reporte;
    }
}
```

**Diferencia clave con EmpleadoProcessor:**

| | EmpleadoProcessor (Step 1) | ReporteProcessor (Step 2) |
|---|---|---|
| Tipo | `ItemProcessor<Empleado, Empleado>` | `ItemProcessor<Empleado, EmpleadoReporte>` |
| Entrada y salida | Mismo tipo | **Tipos diferentes** |
| Logica | Modifica el mismo objeto que recibio | Crea un **objeto nuevo** de otro tipo |

En la v1 el Processor recibia un `Empleado` y devolvia el mismo `Empleado` modificado. Aqui el Processor recibe un `Empleado` pero devuelve un `EmpleadoReporte` — un objeto completamente nuevo con un campo extra (`salarioTotal`).

---

## Paso 9: BatchConfig.java (MODIFICADO en v2)

Crea la clase `BatchConfig.java` en el paquete `com.academia.batch.config`.

**Esta es la clase con mas cambios.** Ahora define componentes para ambos Steps y conecta los dos en el Job.

```java
package com.academia.batch.config;

import com.academia.batch.model.Empleado;
import com.academia.batch.model.EmpleadoReporte;
import com.academia.batch.processor.EmpleadoProcessor;
import com.academia.batch.processor.ReporteProcessor;
import org.springframework.batch.core.Job;
import org.springframework.batch.core.Step;
import org.springframework.batch.core.job.builder.JobBuilder;
import org.springframework.batch.core.launch.support.RunIdIncrementer;
import org.springframework.batch.core.repository.JobRepository;
import org.springframework.batch.core.step.builder.StepBuilder;
import org.springframework.batch.item.database.JdbcBatchItemWriter;
import org.springframework.batch.item.database.JdbcCursorItemReader;
import org.springframework.batch.item.database.builder.JdbcBatchItemWriterBuilder;
import org.springframework.batch.item.database.builder.JdbcCursorItemReaderBuilder;
import org.springframework.batch.item.file.FlatFileItemReader;
import org.springframework.batch.item.file.FlatFileItemWriter;
import org.springframework.batch.item.file.builder.FlatFileItemReaderBuilder;
import org.springframework.batch.item.file.builder.FlatFileItemWriterBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.FileSystemResource;
import org.springframework.transaction.PlatformTransactionManager;

import javax.sql.DataSource;

@Configuration
public class BatchConfig {

    // =====================================================================
    //  STEP 1: Lee CSV → procesa (bono + mayusculas) → escribe en MySQL
    //  (identico a la v1)
    // =====================================================================

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

    @Bean
    public EmpleadoProcessor procesarEmpleado() {
        return new EmpleadoProcessor();
    }

    @Bean
    public JdbcBatchItemWriter<Empleado> escribirEnBd(DataSource dataSource) {
        return new JdbcBatchItemWriterBuilder<Empleado>()
                .sql("INSERT INTO empleados_procesados (nombre, departamento, salario, bono) "
                   + "VALUES (:nombre, :departamento, :salario, :bono)")
                .dataSource(dataSource)
                .beanMapped()
                .build();
    }

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

    // =====================================================================
    //  STEP 2: Lee MySQL → calcula salario total → escribe CSV de reporte
    //  (NUEVO en v2)
    // =====================================================================

    @Bean
    public JdbcCursorItemReader<Empleado> leerDeBd(DataSource dataSource) {
        return new JdbcCursorItemReaderBuilder<Empleado>()
                .name("empleadoDbReader")
                .dataSource(dataSource)
                .sql("SELECT nombre, departamento, salario, bono FROM empleados_procesados")
                .rowMapper((rs, rowNum) -> {
                    Empleado empleado = new Empleado();
                    empleado.setNombre(rs.getString("nombre"));
                    empleado.setDepartamento(rs.getString("departamento"));
                    empleado.setSalario(rs.getDouble("salario"));
                    empleado.setBono(rs.getDouble("bono"));
                    return empleado;
                })
                .build();
    }

    @Bean
    public ReporteProcessor procesarReporte() {
        return new ReporteProcessor();
    }

    @Bean
    public FlatFileItemWriter<EmpleadoReporte> escribirCsv() {
        return new FlatFileItemWriterBuilder<EmpleadoReporte>()
                .name("reporteWriter")
                .resource(new FileSystemResource("reporte-empleados.csv"))
                .headerCallback(writer -> writer.write("nombre,departamento,salario,bono,salario_total"))
                .delimited()
                .names("nombre", "departamento", "salario", "bono", "salarioTotal")
                .build();
    }

    @Bean
    public Step paso2(JobRepository jobRepository,
                      PlatformTransactionManager transactionManager,
                      JdbcCursorItemReader<Empleado> leerDeBd,
                      ReporteProcessor procesarReporte,
                      FlatFileItemWriter<EmpleadoReporte> escribirCsv) {

        return new StepBuilder("paso2", jobRepository)
                .<Empleado, EmpleadoReporte>chunk(3, transactionManager)
                .reader(leerDeBd)
                .processor(procesarReporte)
                .writer(escribirCsv)
                .build();
    }

    // =====================================================================
    //  JOB: ejecuta paso1 y luego paso2
    // =====================================================================

    @Bean
    public Job procesarEmpleadosJob(JobRepository jobRepository, Step paso1, Step paso2) {
        return new JobBuilder("procesarEmpleadosJob", jobRepository)
                .incrementer(new RunIdIncrementer()) // run.id auto-incremental para permitir re-ejecuciones
                .start(paso1)
                .next(paso2)    // despues de paso1, ejecuta paso2
                .build();
    }
}
```

### Lo nuevo del Step 2, explicado en detalle

A continuacion se explican los 3 componentes nuevos del Step 2.

---

### Reader del Step 2: `JdbcCursorItemReader` (leer de base de datos)

En la v1 usamos `FlatFileItemReader` para leer un CSV. Ahora usamos `JdbcCursorItemReader` para leer directamente de MySQL.

```java
.sql("SELECT nombre, departamento, salario, bono FROM empleados_procesados")
```

Ejecuta este SELECT y recorre los resultados fila por fila.

```java
.rowMapper((rs, rowNum) -> {
    Empleado empleado = new Empleado();
    empleado.setNombre(rs.getString("nombre"));
    empleado.setDepartamento(rs.getString("departamento"));
    empleado.setSalario(rs.getDouble("salario"));
    empleado.setBono(rs.getDouble("bono"));
    return empleado;
})
```

El **`rowMapper`** es una funcion que convierte cada fila de la consulta SQL en un objeto Java. Los dos parametros son:

- **`rs`** (ResultSet) — representa una fila del resultado de la consulta. Con `rs.getString("nombre")` obtienes el valor de la columna `nombre` de esa fila. Es lo mismo que usarias con JDBC puro
- **`rowNum`** — el numero de fila actual (0, 1, 2...). No lo usamos aqui, pero Spring lo requiere

El Reader ejecuta el SELECT una sola vez y luego le entrega al Processor de a una fila a la vez (igual que el `FlatFileItemReader` entrega una linea del CSV a la vez).

**Comparacion de Readers:**

| | v1: FlatFileItemReader | v2: JdbcCursorItemReader |
|---|---|---|
| Lee de | Archivo CSV | Base de datos (SELECT) |
| Mapeo | Automatico con `targetType()` | Manual con `rowMapper()` |
| Cuando usarlo | Archivos planos (CSV, TXT) | Tablas de base de datos |

---

### Writer del Step 2: `FlatFileItemWriter` (escribir a CSV)

En la v1 usamos `JdbcBatchItemWriter` para escribir en MySQL. Ahora usamos `FlatFileItemWriter` para generar un archivo CSV.

```java
.resource(new FileSystemResource("reporte-empleados.csv"))
```

**`FileSystemResource` vs `ClassPathResource` — cual es la diferencia?**

| | ClassPathResource | FileSystemResource |
|---|---|---|
| Que es | Busca archivos **dentro** del proyecto (`src/main/resources/`) | Escribe archivos **en el sistema de archivos** de tu computadora |
| Para que sirve | **Leer** recursos empaquetados en la app | **Escribir** archivos de salida |
| Ejemplo | El CSV de entrada que ya esta en el proyecto | El CSV de reporte que la app **genera** |

No podemos usar `ClassPathResource` para escribir porque los archivos dentro de `src/main/resources/` son de solo lectura una vez que la app esta compilada. Para generar archivos nuevos usamos `FileSystemResource`.

```java
.headerCallback(writer -> writer.write("nombre,departamento,salario,bono,salario_total"))
```

Escribe la linea de encabezados al inicio del archivo CSV generado.

```java
.delimited()
.names("nombre", "departamento", "salario", "bono", "salarioTotal")
```

Para cada `EmpleadoReporte`, llama a `getNombre()`, `getDepartamento()`, `getSalario()`, `getBono()`, `getSalarioTotal()` y los escribe separados por coma. El `.names()` funciona igual que `beanMapped()` del Writer de BD: mapea por nombre del campo al getter correspondiente.

**Comparacion de Writers:**

| | v1: JdbcBatchItemWriter | v2: FlatFileItemWriter |
|---|---|---|
| Escribe en | Base de datos (INSERT) | Archivo CSV |
| Mapeo | `beanMapped()` + `:campo` en SQL | `.names()` + getters |
| Cuando usarlo | Guardar en BD | Generar reportes/archivos |

---

### El Job ahora tiene dos Steps

Los cambios en la definicion del Job son agregar `.next(paso2)` y el `.incrementer(new RunIdIncrementer())`:

```java
// v1: un solo step
.start(paso1)
.build();

// v2: dos steps en secuencia
.incrementer(new RunIdIncrementer()) // permite re-ejecutar sin limpiar tablas BATCH_*
.start(paso1)
.next(paso2)    // se ejecuta despues de que paso1 termina exitosamente
.build();
```

Si `paso1` falla, `paso2` **no se ejecuta**. Spring Batch garantiza el orden y no avanza al siguiente Step si el anterior fallo.

**`RunIdIncrementer`** — cada vez que ejecutas la app, Spring Batch agrega automaticamente un parametro `run.id` con un valor incremental (1, 2, 3...). Esto hace que cada ejecucion sea unica y evita el error "A job instance already exists". Sin esto, tendrias que limpiar las tablas `BATCH_*` manualmente antes de cada re-ejecucion.

---

## Paso 10: SpringBatchApplication.java

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

Misma clase main que la v1. No necesita cambios.

---

## Paso 11: Ejecutar la aplicacion

### Desde Eclipse

Clic derecho en `SpringBatchApplication.java` > **Run As** > **Java Application**

### Desde la terminal

Desde la carpeta raiz del proyecto (`springBatchV2/`):

```bash
mvn spring-boot:run
```

### Resultado esperado en consola

Ahora veras **dos bloques** de logs, uno por cada Step. Primero todo el Step 1, luego todo el Step 2:

```
Job: [SimpleJob: [name=procesarEmpleadosJob]] launched with the following parameters: [{}]

Executing step: [paso1]
Step 1 - Procesando: JUAN PEREZ | Ventas | Salario: 25000.0 | Bono: 2500.0
Step 1 - Procesando: MARIA LOPEZ | TI | Salario: 35000.0 | Bono: 3500.0
Step 1 - Procesando: CARLOS GARCIA | RRHH | Salario: 28000.0 | Bono: 2800.0
Step 1 - Procesando: ANA MARTINEZ | Ventas | Salario: 27000.0 | Bono: 2700.0
Step 1 - Procesando: PEDRO SANCHEZ | TI | Salario: 32000.0 | Bono: 3200.0
Step 1 - Procesando: LAURA DIAZ | RRHH | Salario: 30000.0 | Bono: 3000.0
Step 1 - Procesando: ROBERTO FLORES | Ventas | Salario: 26000.0 | Bono: 2600.0
Step 1 - Procesando: SOFIA RAMIREZ | TI | Salario: 38000.0 | Bono: 3800.0
Step 1 - Procesando: DIEGO TORRES | RRHH | Salario: 29000.0 | Bono: 2900.0
Step 1 - Procesando: FERNANDA RIOS | Ventas | Salario: 31000.0 | Bono: 3100.0
Step: [paso1] executed in 36ms

Executing step: [paso2]
Step 2 - Reporte: JUAN PEREZ | Ventas | Salario: 25000.0 | Bono: 2500.0 | Total: 27500.0
Step 2 - Reporte: MARIA LOPEZ | TI | Salario: 35000.0 | Bono: 3500.0 | Total: 38500.0
Step 2 - Reporte: CARLOS GARCIA | RRHH | Salario: 28000.0 | Bono: 2800.0 | Total: 30800.0
Step 2 - Reporte: ANA MARTINEZ | Ventas | Salario: 27000.0 | Bono: 2700.0 | Total: 29700.0
Step 2 - Reporte: PEDRO SANCHEZ | TI | Salario: 32000.0 | Bono: 3200.0 | Total: 35200.0
Step 2 - Reporte: LAURA DIAZ | RRHH | Salario: 30000.0 | Bono: 3000.0 | Total: 33000.0
Step 2 - Reporte: ROBERTO FLORES | Ventas | Salario: 26000.0 | Bono: 2600.0 | Total: 28600.0
Step 2 - Reporte: SOFIA RAMIREZ | TI | Salario: 38000.0 | Bono: 3800.0 | Total: 41800.0
Step 2 - Reporte: DIEGO TORRES | RRHH | Salario: 29000.0 | Bono: 2900.0 | Total: 31900.0
Step 2 - Reporte: FERNANDA RIOS | Ventas | Salario: 31000.0 | Bono: 3100.0 | Total: 34100.0
Step: [paso2] executed in 27ms

Job: [SimpleJob: [name=procesarEmpleadosJob]] completed with the following parameters: [{}] and the following status: [COMPLETED]
```

Observa:
- `paso1` termina completamente antes de que `paso2` inicie
- El Step 2 muestra el campo `Total` que no existia en el Step 1
- El Job termina con status `COMPLETED` indicando que ambos Steps fueron exitosos

---

## Paso 12: Verificar los resultados

### 12.1 En MySQL (resultado del Step 1)

Abre DBeaver conectado como **alumno** y ejecuta:

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

### 12.2 El archivo CSV generado (resultado del Step 2)

El archivo `reporte-empleados.csv` se crea en la **carpeta raiz del proyecto** (`springBatchV2/`).

**En Eclipse:** para verlo en el Package Explorer necesitas hacer clic derecho en el proyecto > **Refresh** (o presionar `F5`). El archivo aparecera en la raiz del proyecto.

**Desde la terminal:** puedes abrirlo directamente con cualquier editor o con Excel.

El contenido del archivo debe ser:

```csv
nombre,departamento,salario,bono,salario_total
JUAN PEREZ,Ventas,25000.0,2500.0,27500.0
MARIA LOPEZ,TI,35000.0,3500.0,38500.0
CARLOS GARCIA,RRHH,28000.0,2800.0,30800.0
ANA MARTINEZ,Ventas,27000.0,2700.0,29700.0
PEDRO SANCHEZ,TI,32000.0,3200.0,35200.0
LAURA DIAZ,RRHH,30000.0,3000.0,33000.0
ROBERTO FLORES,Ventas,26000.0,2600.0,28600.0
SOFIA RAMIREZ,TI,38000.0,3800.0,41800.0
DIEGO TORRES,RRHH,29000.0,2900.0,31900.0
FERNANDA RIOS,Ventas,31000.0,3100.0,34100.0
```

La columna `salario_total` es la suma de `salario + bono`, calculada por el `ReporteProcessor`.

### 12.3 Estadisticas de ambos Steps en el JobRepository

```sql
SELECT STEP_NAME, READ_COUNT, WRITE_COUNT, COMMIT_COUNT, STATUS
FROM BATCH_STEP_EXECUTION;
```

| STEP_NAME | READ_COUNT | WRITE_COUNT | COMMIT_COUNT | STATUS |
|-----------|-----------|-------------|-------------|--------|
| paso1 | 10 | 10 | 4 | COMPLETED |
| paso2 | 10 | 10 | 4 | COMPLETED |

Ambos Steps leyeron 10 registros, escribieron 10 registros, hicieron 4 commits (chunks de 3+3+3+1) y terminaron exitosamente.

---

## Resumen comparativo v1 vs v2

| | v1 | v2 |
|---|---|---|
| Steps | 1 | **2** |
| Readers | FlatFileItemReader (CSV) | FlatFileItemReader (CSV) + **JdbcCursorItemReader (MySQL)** |
| Processors | EmpleadoProcessor | EmpleadoProcessor + **ReporteProcessor** |
| Writers | JdbcBatchItemWriter (MySQL) | JdbcBatchItemWriter (MySQL) + **FlatFileItemWriter (CSV)** |
| Modelos | Empleado | Empleado + **EmpleadoReporte** |
| Flujo | CSV → MySQL | CSV → MySQL → **CSV** |
| Job | `.start(paso1)` | `.start(paso1).next(paso2)` |

---

## Para re-ejecutar

Gracias al `RunIdIncrementer`, puedes ejecutar la app multiples veces sin limpiar las tablas `BATCH_*`. Cada ejecucion recibe un `run.id` unico (1, 2, 3...).

Solo necesitas limpiar la tabla de datos si quieres evitar duplicados:

```sql
DELETE FROM empleados_procesados;
```

El archivo `reporte-empleados.csv` se sobreescribe automaticamente al volver a ejecutar, no necesitas borrarlo manualmente.

> **Nota:** Si por alguna razon necesitas limpiar completamente el historial de Spring Batch:
> ```sql
> DELETE FROM BATCH_STEP_EXECUTION_CONTEXT;
> DELETE FROM BATCH_STEP_EXECUTION;
> DELETE FROM BATCH_JOB_EXECUTION_CONTEXT;
> DELETE FROM BATCH_JOB_EXECUTION_PARAMS;
> DELETE FROM BATCH_JOB_EXECUTION;
> DELETE FROM BATCH_JOB_INSTANCE;
> ```

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

Desde la carpeta raiz del proyecto (`springBatchV2/`):

```bash
# Compilar y empaquetar (genera el JAR en target/)
mvn clean package -DskipTests
```

Resultado esperado:

```
[INFO] BUILD SUCCESS
[INFO] -----------------------------------------------
```

Esto genera el archivo `target/spring-batch-v2-1.0.0.jar`.

### 4. Ejecutar la aplicacion

**Opcion A** — con Maven (no necesita compilar antes):

```bash
mvn spring-boot:run
```

**Opcion B** — ejecutando el JAR directamente (necesita haber compilado con `mvn clean package`):

```bash
java -jar target/spring-batch-v2-1.0.0.jar
```

Ambas opciones producen el mismo resultado. La opcion B es como se ejecutaria en un servidor de produccion.

### 5. Verificar resultados desde terminal

**MySQL (resultado del Step 1):**

```bash
docker exec -it mysql-academia mysql -u alumno -palumno123 academia -e "
SELECT * FROM empleados_procesados;
"
```

**Estadisticas de ambos Steps:**

```bash
docker exec -it mysql-academia mysql -u alumno -palumno123 academia -e "
SELECT STEP_NAME, READ_COUNT, WRITE_COUNT, COMMIT_COUNT, STATUS
FROM BATCH_STEP_EXECUTION;
"
```

**CSV generado (resultado del Step 2):**

El archivo `reporte-empleados.csv` se crea en la carpeta raiz del proyecto:

```bash
cat reporte-empleados.csv
```

Resultado esperado:

```
nombre,departamento,salario,bono,salario_total
JUAN PEREZ,Ventas,25000.0,2500.0,27500.0
MARIA LOPEZ,TI,35000.0,3500.0,38500.0
...
```

### 6. Limpiar datos para re-ejecutar

Gracias al `RunIdIncrementer`, no necesitas limpiar las tablas `BATCH_*`. Solo limpia la tabla de datos si quieres evitar duplicados:

```bash
docker exec -it mysql-academia mysql -u alumno -palumno123 academia -e "
DELETE FROM empleados_procesados;
"
```

Despues de limpiar, puedes volver a ejecutar con `mvn spring-boot:run` o `java -jar target/spring-batch-v2-1.0.0.jar`.

---

## Problemas comunes

### "Access denied for user 'alumno'"
El usuario no tiene permisos. Conectate como **root** y ejecuta:
```sql
GRANT ALL PRIVILEGES ON academia.* TO 'alumno'@'%';
FLUSH PRIVILEGES;
```

### "Table 'empleados_procesados' doesn't exist"
No creaste la tabla. Ejecuta el script de la seccion de Prerequisitos.

### "A job instance already exists"
Esto no deberia pasar con el `RunIdIncrementer` configurado. Si te pasa, verifica que tu `BatchConfig.java` tenga la linea `.incrementer(new RunIdIncrementer())` en la definicion del Job. Si no la tiene, sigue las instrucciones de la seccion "Para re-ejecutar" para limpiar manualmente.

### No veo el archivo reporte-empleados.csv en Eclipse
Clic derecho en el proyecto > **Refresh** (o `F5`). Eclipse no detecta automaticamente archivos creados por la app.

### "Communications link failure"
El contenedor MySQL no esta corriendo:
```bash
docker start mysql-academia
```
