#!/usr/bin/env python3
"""
Genera el PDF de la Guia de Repaso del 20 de febrero de 2026.
Estilo visual consistente con los PDFs anteriores del curso.
"""
import weasyprint

HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  @page {
    size: letter;
    margin: 2.5cm 2.5cm 3cm 2.5cm;
    @bottom-center {
      content: "Pagina " counter(page) "/20";
      font-size: 10px;
      color: #999;
    }
    @top-left {
      content: "Curso de Java - Spring Batch";
      font-size: 9px;
      color: #999;
    }
    @top-right {
      content: "Semana 02 | 20 Feb 2026";
      font-size: 9px;
      color: #999;
    }
  }

  @page:first {
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: "Pagina 1/20"; font-size: 10px; color: #999; }
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #333;
  }

  /* --- PORTADA --- */
  .cover {
    text-align: center;
    padding-top: 80px;
    page-break-after: always;
  }
  .cover h1 {
    font-size: 36pt;
    color: #E8A838;
    font-style: italic;
    margin-bottom: 10px;
  }
  .cover h2 {
    font-size: 22pt;
    color: #5DADE2;
    font-weight: bold;
    margin-bottom: 30px;
  }
  .cover .separator {
    width: 60px;
    height: 4px;
    background: #E8A838;
    margin: 0 auto 30px;
  }
  .cover .info {
    font-size: 11pt;
    color: #666;
    margin-bottom: 5px;
  }
  .cover .temas-title {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 40px;
    margin-bottom: 15px;
  }
  .cover .temas {
    text-align: left;
    display: inline-block;
    font-size: 11pt;
    color: #444;
  }
  .cover .temas li {
    margin-bottom: 6px;
  }
  .cover .instructor {
    font-style: italic;
    color: #E8A838;
    font-size: 13pt;
    margin-top: 50px;
  }

  /* --- SECCIONES --- */
  h1.section {
    font-size: 22pt;
    color: #5DADE2;
    border-bottom: none;
    margin-top: 10px;
    margin-bottom: 5px;
    page-break-after: avoid;
  }
  h1.section::after {
    content: '';
    display: block;
    width: 50px;
    height: 4px;
    background: #E8A838;
    margin-top: 8px;
    margin-bottom: 15px;
  }

  h2 {
    font-size: 15pt;
    color: #333;
    margin-top: 25px;
    margin-bottom: 10px;
    page-break-after: avoid;
  }

  h3 {
    font-size: 12pt;
    color: #444;
    margin-top: 20px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }

  /* --- RESUMEN TITLE --- */
  h1.resumen {
    font-size: 22pt;
    color: #E8A838;
    margin-top: 10px;
    margin-bottom: 5px;
    page-break-after: avoid;
  }
  h1.resumen::after {
    content: '';
    display: block;
    width: 50px;
    height: 4px;
    background: #E8A838;
    margin-top: 8px;
    margin-bottom: 15px;
  }

  /* --- CODIGO --- */
  pre {
    background: #F7F9FB;
    border-left: 4px solid #5DADE2;
    padding: 12px 15px;
    font-size: 8.5pt;
    font-family: 'SF Mono', 'Menlo', 'Monaco', 'Consolas', monospace;
    line-height: 1.45;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    margin: 10px 0;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
  }

  code {
    font-family: 'SF Mono', 'Menlo', 'Monaco', 'Consolas', monospace;
    font-size: 9pt;
    background: #EBF0F5;
    padding: 1px 5px;
    border-radius: 3px;
  }

  pre code {
    background: none;
    padding: 0;
    font-size: 8.5pt;
  }

  /* --- CALLOUTS --- */
  .callout {
    padding: 12px 15px;
    margin: 12px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
  }
  .callout-clave {
    background: #E8F8E8;
    border-left: 4px solid #4CAF50;
  }
  .callout-problema {
    background: #FCE4E4;
    border-left: 4px solid #E74C3C;
  }
  .callout-nota {
    background: #FFF8E1;
    border-left: 4px solid #F5A623;
  }
  .callout-principio {
    background: #E3F2FD;
    border-left: 4px solid #2196F3;
  }
  .callout strong {
    color: inherit;
  }
  .callout-clave strong:first-child { color: #2E7D32; }
  .callout-problema strong:first-child { color: #C62828; }
  .callout-nota strong:first-child { color: #E65100; }
  .callout-principio strong:first-child { color: #1565C0; }

  /* --- TABLAS --- */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 10pt;
    page-break-inside: avoid;
  }
  table th {
    background: #5DADE2;
    color: white;
    padding: 8px 12px;
    text-align: left;
    font-weight: bold;
  }
  table td {
    padding: 7px 12px;
    border-bottom: 1px solid #E0E0E0;
  }
  table tr:nth-child(even) td {
    background: #F8FAFB;
  }

  p {
    margin: 8px 0;
  }

  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<!-- ==================== PORTADA ==================== -->
<div class="cover">
  <h1>Guia de Repaso</h1>
  <h2>Spring Batch:<br>Procesamiento por Lotes</h2>
  <div class="separator"></div>
  <p class="info">Semana 02 - Viernes 20 de Febrero de 2026</p>
  <p class="info">Academia Java - Ciudad de Mexico</p>

  <p class="temas-title">Temas del dia:</p>
  <div class="temas">
    <ol>
      <li>Que es Spring Batch: procesamiento por lotes</li>
      <li>Arquitectura: Job, Step, Reader-Processor-Writer</li>
      <li>Chunk-oriented processing: procesar en bloques</li>
      <li>Proyecto v1: CSV a MySQL (un Step)</li>
      <li>Proyecto v2: Dos Steps (CSV a MySQL a CSV)</li>
      <li>JobRepository: metadatos y control de ejecucion</li>
    </ol>
  </div>

  <p class="instructor">Instructor: Miguel Rugerio</p>
</div>

<!-- ==================== 1. QUE ES SPRING BATCH ==================== -->
<h1 class="section">1. Que es Spring Batch</h1>

<p>
  <strong>Spring Batch</strong> es un framework de Spring para <strong>procesamiento por lotes</strong>
  (batch processing). Procesa grandes cantidades de datos de forma automatizada, sin intervencion del usuario.
</p>

<h2>Analogia: la fabrica de empaquetado</h2>

<p>Imagina una fabrica que recibe cajas de productos (datos de entrada), los inspecciona y etiqueta
(procesamiento), y los coloca en un camion (datos de salida). La fabrica no procesa una caja a la vez,
sino <strong>grupos de cajas</strong> (chunks) para ser eficiente.</p>

<p>Spring Batch funciona igual:</p>

<pre><code>  CSV / BD / API          Tu logica            BD / CSV / API
  ┌──────────┐        ┌──────────┐         ┌──────────┐
  │  READER  │──────&gt; │PROCESSOR │───────&gt; │  WRITER  │
  │ (leer)   │        │(procesar)│         │(escribir)│
  └──────────┘        └──────────┘         └──────────┘</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Spring Batch se usa cuando necesitas procesar archivos grandes, migrar datos entre
  sistemas, generar reportes masivos, o cualquier tarea repetitiva sobre muchos registros.
</div>

<h2>Donde se usa en la industria</h2>

<table>
  <tr><th>Escenario</th><th>Reader</th><th>Writer</th></tr>
  <tr><td>Cargar empleados de un CSV a la base de datos</td><td>Archivo CSV</td><td>MySQL</td></tr>
  <tr><td>Generar reporte de ventas del mes</td><td>Base de datos</td><td>Archivo CSV</td></tr>
  <tr><td>Migrar datos entre sistemas</td><td>BD origen</td><td>BD destino</td></tr>
  <tr><td>Procesar archivos de un banco</td><td>Archivo plano</td><td>Base de datos</td></tr>
</table>

<!-- ==================== 2. ARQUITECTURA ==================== -->
<div class="page-break"></div>
<h1 class="section">2. Arquitectura de Spring Batch</h1>

<p>Spring Batch tiene 3 niveles jerarquicos: <strong>Job &gt; Step &gt; (Reader + Processor + Writer)</strong>.</p>

<pre><code> ┌─────────────────────────────────────────────┐
 │                    JOB                       │
 │  "procesarEmpleadosJob"                      │
 │                                              │
 │  ┌───────────────────────────────────────┐   │
 │  │              STEP 1                   │   │
 │  │  ┌────────┐ ┌──────────┐ ┌────────┐  │   │
 │  │  │ Reader │→│Processor │→│ Writer │  │   │
 │  │  │  CSV   │ │  logica  │ │ MySQL  │  │   │
 │  │  └────────┘ └──────────┘ └────────┘  │   │
 │  └───────────────────────────────────────┘   │
 │                    │                         │
 │                    ▼                         │
 │  ┌───────────────────────────────────────┐   │
 │  │              STEP 2                   │   │
 │  │  ┌────────┐ ┌──────────┐ ┌────────┐  │   │
 │  │  │ Reader │→│Processor │→│ Writer │  │   │
 │  │  │ MySQL  │ │  logica  │ │  CSV   │  │   │
 │  │  └────────┘ └──────────┘ └────────┘  │   │
 │  └───────────────────────────────────────┘   │
 │                                              │
 └─────────────────────────────────────────────┘
         │
         ▼
 ┌──────────────────┐
 │  JobRepository   │
 │  (tablas BATCH_*)│
 │  guarda estado   │
 └──────────────────┘</code></pre>

<h2>Los componentes</h2>

<table>
  <tr><th>Componente</th><th>Que hace</th><th>Analogia</th></tr>
  <tr><td><strong>Job</strong></td><td>El trabajo completo. Contiene uno o mas Steps</td><td>La orden de trabajo de la fabrica</td></tr>
  <tr><td><strong>Step</strong></td><td>Un paso del Job. Contiene Reader + Processor + Writer</td><td>Una estacion de la linea de ensamblaje</td></tr>
  <tr><td><strong>ItemReader</strong></td><td>Lee datos de una fuente (CSV, BD, API)</td><td>La banda que trae cajas</td></tr>
  <tr><td><strong>ItemProcessor</strong></td><td>Transforma cada registro</td><td>El operario que inspecciona y etiqueta</td></tr>
  <tr><td><strong>ItemWriter</strong></td><td>Escribe los resultados (BD, CSV, API)</td><td>El operario que pone cajas en el camion</td></tr>
  <tr><td><strong>JobRepository</strong></td><td>Guarda el estado de cada ejecucion</td><td>El registro de produccion de la fabrica</td></tr>
</table>

<div class="callout callout-nota">
  <strong>Nota:</strong> El Processor es <strong>opcional</strong>. Si solo necesitas copiar datos sin transformarlos,
  puedes tener solo Reader + Writer.
</div>

<!-- ==================== 3. CHUNK ==================== -->
<div class="page-break"></div>
<h1 class="section">3. Chunk-oriented Processing</h1>

<p>Spring Batch no procesa registro por registro. Procesa en <strong>chunks</strong> (bloques).</p>

<h2>Como funciona con chunk(3)</h2>

<p>Si tenemos 10 empleados y chunk size = 3:</p>

<pre><code>Registros: [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]

Chunk 1: Lee 1, Lee 2, Lee 3  → Procesa 1,2,3  → Escribe [1,2,3] en BD
Chunk 2: Lee 4, Lee 5, Lee 6  → Procesa 4,5,6  → Escribe [4,5,6] en BD
Chunk 3: Lee 7, Lee 8, Lee 9  → Procesa 7,8,9  → Escribe [7,8,9] en BD
Chunk 4: Lee 10               → Procesa 10     → Escribe [10] en BD</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Cada chunk es una <strong>transaccion</strong>. Si el chunk 3 falla, los chunks 1 y 2
  ya estan guardados en la base de datos. No se pierde todo el trabajo.
</div>

<h2>Por que no de 1 en 1?</h2>

<table>
  <tr><th>Estrategia</th><th>INSERTs para 10 registros</th><th>Eficiencia</th></tr>
  <tr><td>Uno por uno (chunk=1)</td><td>10 transacciones</td><td>Lento</td></tr>
  <tr><td><strong>Chunks de 3 (chunk=3)</strong></td><td><strong>4 transacciones</strong></td><td><strong>Equilibrado</strong></td></tr>
  <tr><td>Todo junto (chunk=10)</td><td>1 transaccion</td><td>Riesgo: si falla, se pierde todo</td></tr>
</table>

<p>En nuestros proyectos usamos <code>chunk(3)</code> para poder ver claramente en los logs como se procesan los bloques.</p>

<!-- ==================== 4. PROYECTO V1 ==================== -->
<div class="page-break"></div>
<h1 class="section">4. Proyecto v1: CSV a MySQL (un Step)</h1>

<p>El primer proyecto lee un archivo CSV de empleados, transforma los datos (nombre a mayusculas + calculo de bono), y los guarda en MySQL.</p>

<pre><code>empleados.csv ──→ EmpleadoProcessor ──→ MySQL (empleados_procesados)
                   - MAYUSCULAS          INSERT INTO ...
                   - bono = salario*10%</code></pre>

<h2>El archivo CSV de entrada</h2>

<pre><code>nombre,departamento,salario
Juan Perez,Ventas,25000
Maria Lopez,TI,35000
Carlos Garcia,RRHH,28000
Ana Martinez,Ventas,27000
Pedro Sanchez,TI,32000
Laura Diaz,RRHH,30000
Roberto Flores,Ventas,26000
Sofia Ramirez,TI,38000
Diego Torres,RRHH,29000
Fernanda Rios,Ventas,31000</code></pre>

<p>10 empleados con 3 campos: nombre, departamento, salario.</p>

<h2>El modelo: Empleado (POJO)</h2>

<pre><code>public class Empleado {

    private String nombre;
    private String departamento;
    private double salario;
    private double bono;

    public Empleado() {
    }

    // getters y setters para cada campo...

    @Override
    public String toString() {
        return nombre + " | " + departamento
             + " | Salario: " + salario + " | Bono: " + bono;
    }
}</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Spring Batch usa los <strong>setters</strong> para llenar el objeto al leer el CSV,
  y los <strong>getters</strong> para obtener los valores al escribir en la BD. Por eso necesita el constructor
  vacio y los getters/setters.
</div>

<!-- ==================== 5. READER ==================== -->
<div class="page-break"></div>
<h1 class="section">5. El Reader: leer el CSV</h1>

<p>El <code>FlatFileItemReader</code> lee archivos planos (CSV, TXT) linea por linea:</p>

<pre><code>@Bean
public FlatFileItemReader&lt;Empleado&gt; leerCsv() {
    return new FlatFileItemReaderBuilder&lt;Empleado&gt;()
            .name("empleadoReader")
            .resource(new ClassPathResource("empleados.csv"))
            .delimited()                          // separado por comas
            .names("nombre", "departamento", "salario") // columnas del CSV
            .targetType(Empleado.class)            // mapea a nuestro POJO
            .linesToSkip(1)                        // saltar encabezado
            .build();
}</code></pre>

<h2>Que hace cada linea</h2>

<table>
  <tr><th>Metodo</th><th>Que hace</th></tr>
  <tr><td><code>.name("empleadoReader")</code></td><td>Nombre interno para el reader</td></tr>
  <tr><td><code>.resource(new ClassPathResource(...))</code></td><td>Busca el archivo en <code>src/main/resources/</code></td></tr>
  <tr><td><code>.delimited()</code></td><td>Indica que el separador es coma (,)</td></tr>
  <tr><td><code>.names(...)</code></td><td>Mapea columnas del CSV a los setters del POJO</td></tr>
  <tr><td><code>.targetType(Empleado.class)</code></td><td>Tipo de objeto a crear por cada linea</td></tr>
  <tr><td><code>.linesToSkip(1)</code></td><td>Salta la primera linea (el encabezado)</td></tr>
</table>

<div class="callout callout-nota">
  <strong>Nota:</strong> <code>ClassPathResource</code> busca archivos dentro de <code>src/main/resources/</code>.
  Es donde Maven y Spring Boot esperan encontrar archivos estaticos del proyecto.
</div>

<!-- ==================== 6. PROCESSOR ==================== -->
<div class="page-break"></div>
<h1 class="section">6. El Processor: transformar los datos</h1>

<p>El <code>ItemProcessor</code> recibe un objeto, lo transforma, y lo devuelve:</p>

<pre><code>public class EmpleadoProcessor implements ItemProcessor&lt;Empleado, Empleado&gt; {

    private static final Logger log = LoggerFactory.getLogger(EmpleadoProcessor.class);

    @Override
    public Empleado process(Empleado empleado) {
        empleado.setNombre(empleado.getNombre().toUpperCase());
        empleado.setBono(empleado.getSalario() * 0.10);

        log.info("Step 1 - Procesando: {}", empleado);
        return empleado;
    }
}</code></pre>

<h2>Que hace</h2>

<p>1. <strong>Nombre a mayusculas:</strong> <code>"Juan Perez"</code> → <code>"JUAN PEREZ"</code></p>
<p>2. <strong>Calcula bono del 10%:</strong> salario 25000 → bono 2500.0</p>
<p>3. <strong>Log:</strong> imprime en consola cada empleado procesado</p>

<h2>La interfaz ItemProcessor&lt;I, O&gt;</h2>

<pre><code>ItemProcessor&lt;Empleado, Empleado&gt;
                 │          │
                 │          └── O = tipo de SALIDA (lo que devuelve)
                 └── I = tipo de ENTRADA (lo que recibe del Reader)</code></pre>

<p>En v1, la entrada y salida son el mismo tipo (<code>Empleado</code>). En v2 veremos que pueden ser diferentes.</p>

<div class="callout callout-clave">
  <strong>Clave:</strong> Si <code>process()</code> retorna <code>null</code>, el registro se <strong>descarta</strong>
  y no llega al Writer. Esto es util para filtrar datos.
</div>

<!-- ==================== 7. WRITER ==================== -->
<div class="page-break"></div>
<h1 class="section">7. El Writer: escribir en MySQL</h1>

<p>El <code>JdbcBatchItemWriter</code> inserta los registros procesados en la base de datos:</p>

<pre><code>@Bean
public JdbcBatchItemWriter&lt;Empleado&gt; escribirEnBd(DataSource dataSource) {
    return new JdbcBatchItemWriterBuilder&lt;Empleado&gt;()
            .sql("INSERT INTO empleados_procesados "
               + "(nombre, departamento, salario, bono) "
               + "VALUES (:nombre, :departamento, :salario, :bono)")
            .dataSource(dataSource)
            .beanMapped()
            .build();
}</code></pre>

<h2>Los parametros con nombre (:nombre, :salario)</h2>

<pre><code>VALUES (:nombre, :departamento, :salario, :bono)
        │          │              │         │
        ▼          ▼              ▼         ▼
  getNombre() getDepartamento() getSalario() getBono()</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>.beanMapped()</code> le dice a Spring Batch: "los parametros <code>:nombre</code>,
  <code>:salario</code>, etc. se obtienen llamando <code>getNombre()</code>, <code>getSalario()</code> del POJO".
  Por eso los nombres deben coincidir exactamente.
</div>

<h2>DataSource: la conexion a MySQL</h2>

<p><code>DataSource</code> es el objeto que contiene la conexion a la base de datos.
<strong>No lo creamos nosotros</strong> — Spring Boot lo crea automaticamente usando el <code>application.properties</code>:</p>

<pre><code>spring.datasource.url=jdbc:mysql://localhost:3306/academia
spring.datasource.username=alumno
spring.datasource.password=alumno123</code></pre>

<p>Spring Boot ve estas propiedades, crea un <code>DataSource</code>, y lo inyecta donde se necesite.
Esto es <strong>Inversion de Control</strong> en accion.</p>

<!-- ==================== 8. STEP Y JOB ==================== -->
<div class="page-break"></div>
<h1 class="section">8. El Step y el Job: ensamblando las piezas</h1>

<h2>El Step conecta Reader + Processor + Writer</h2>

<pre><code>@Bean
public Step paso1(JobRepository jobRepository,
                  PlatformTransactionManager transactionManager,
                  FlatFileItemReader&lt;Empleado&gt; leerCsv,
                  EmpleadoProcessor procesarEmpleado,
                  JdbcBatchItemWriter&lt;Empleado&gt; escribirEnBd) {

    return new StepBuilder("paso1", jobRepository)
            .&lt;Empleado, Empleado&gt;chunk(3, transactionManager)
            .reader(leerCsv)
            .processor(procesarEmpleado)
            .writer(escribirEnBd)
            .build();
}</code></pre>

<h2>Que es &lt;Empleado, Empleado&gt;chunk(3, transactionManager)?</h2>

<pre><code>.&lt;Empleado, Empleado&gt;chunk(3, transactionManager)
   │          │        │    │
   │          │        │    └── maneja las transacciones (commit/rollback)
   │          │        └── tamanio del chunk (procesa de 3 en 3)
   │          └── tipo de SALIDA del processor
   └── tipo de ENTRADA al processor</code></pre>

<h2>El Job ejecuta los Steps</h2>

<pre><code>@Bean
public Job procesarEmpleadosJob(JobRepository jobRepository, Step paso1) {
    return new JobBuilder("procesarEmpleadosJob", jobRepository)
            .start(paso1)   // inicia con el paso1
            .build();
}</code></pre>

<div class="callout callout-nota">
  <strong>Nota:</strong> <code>JobRepository</code>, <code>PlatformTransactionManager</code> y
  <code>DataSource</code> son <strong>inyectados automaticamente</strong> por Spring Boot. No necesitas
  crearlos manualmente — Spring Boot los configura usando las propiedades de
  <code>application.properties</code>.
</div>

<!-- ==================== 9. CONFIG Y BEAN ==================== -->
<div class="page-break"></div>
<h1 class="section">9. @Configuration y @Bean: la receta de la fabrica</h1>

<h2>@Configuration</h2>

<p>Marca una clase como <strong>fuente de configuracion</strong>. Le dice a Spring: "esta clase contiene la
receta para crear objetos":</p>

<pre><code>@Configuration
public class BatchConfig {
    // aqui van los @Bean
}</code></pre>

<h2>@Bean</h2>

<p>Cada metodo con <code>@Bean</code> le dice a Spring: "ejecuta este metodo y guarda el resultado para
cuando alguien lo necesite":</p>

<pre><code>@Bean
public FlatFileItemReader&lt;Empleado&gt; leerCsv() {
    // Spring ejecuta esto UNA vez y guarda el reader
    return new FlatFileItemReaderBuilder&lt;Empleado&gt;()
            // ...
            .build();
}

@Bean
public Step paso1(..., FlatFileItemReader&lt;Empleado&gt; leerCsv, ...) {
    // Spring inyecta el reader que creo arriba
    return new StepBuilder("paso1", jobRepository)
            .reader(leerCsv)  // &lt;-- usa el reader inyectado
            // ...
            .build();
}</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Los parametros de un metodo <code>@Bean</code> se resuelven por
  <strong>inyeccion de dependencias</strong>. Spring busca un bean del tipo correcto y lo pasa
  automaticamente. Por eso <code>paso1</code> recibe el <code>leerCsv</code> sin que nosotros
  llamemos <code>new</code>.
</div>

<h2>Relacion con IoC (sesion anterior)</h2>

<p>Ayer vimos IoC manual con <code>setPizza()</code> y luego un <code>Inyector</code> centralizado.
<strong>Spring Boot es el inyector real</strong>: busca los <code>@Bean</code> que definimos y los conecta
donde se necesiten, usando <code>@Configuration</code> como el mapa de instrucciones.</p>

<!-- ==================== 10. JOB REPOSITORY ==================== -->
<div class="page-break"></div>
<h1 class="section">10. JobRepository: el registro de produccion</h1>

<p>Spring Batch crea automaticamente <strong>9 tablas</strong> en MySQL con prefijo <code>BATCH_</code>:</p>

<pre><code>BATCH_JOB_INSTANCE        ← un Job unico (nombre + parametros)
BATCH_JOB_EXECUTION       ← cada ejecucion del Job (fecha, estado, duracion)
BATCH_JOB_EXECUTION_PARAMS ← parametros de cada ejecucion
BATCH_STEP_EXECUTION       ← cada ejecucion de cada Step (registros leidos, escritos)
...y 5 tablas mas de soporte</code></pre>

<h2>Para que sirven?</h2>

<pre><code>-- Ver las ejecuciones del Job
SELECT * FROM BATCH_JOB_EXECUTION;

-- Ver cuantos registros proceso cada Step
SELECT step_name, read_count, write_count, status
FROM BATCH_STEP_EXECUTION;</code></pre>

<table>
  <tr><th>Campo</th><th>Ejemplo</th><th>Significado</th></tr>
  <tr><td><code>status</code></td><td>COMPLETED</td><td>El Step termino correctamente</td></tr>
  <tr><td><code>read_count</code></td><td>10</td><td>Leyo 10 registros del CSV</td></tr>
  <tr><td><code>write_count</code></td><td>10</td><td>Escribio 10 registros en MySQL</td></tr>
  <tr><td><code>commit_count</code></td><td>4</td><td>Hizo 4 commits (10 registros / chunk 3 = 4 chunks)</td></tr>
</table>

<div class="callout callout-problema">
  <strong>Problema:</strong> Si ejecutas el Job dos veces con los mismos parametros, Spring Batch dice:
  "ya lo ejecute, no lo vuelvo a hacer". Si necesitas re-ejecutar, primero limpia las tablas BATCH_*
  y la tabla de datos.
</div>

<!-- ==================== 11. PROYECTO V2 ==================== -->
<div class="page-break"></div>
<h1 class="section">11. Proyecto v2: Dos Steps</h1>

<p>La version 2 agrega un segundo Step que lee los datos ya procesados de MySQL y genera un reporte CSV
con el salario total:</p>

<pre><code>  STEP 1                          STEP 2
  CSV ──→ Processor ──→ MySQL     MySQL ──→ Processor ──→ CSV
          - MAYUSCULAS                      - salarioTotal
          - bono 10%                        = salario + bono</code></pre>

<h2>El Job ejecuta los Steps en secuencia</h2>

<pre><code>@Bean
public Job procesarEmpleadosJob(JobRepository jobRepository,
                                Step paso1, Step paso2) {
    return new JobBuilder("procesarEmpleadosJob", jobRepository)
            .start(paso1)       // primero ejecuta paso1
            .next(paso2)        // despues ejecuta paso2
            .build();
}</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>.start(paso1).next(paso2)</code> define el orden. Si paso1 falla,
  paso2 <strong>no se ejecuta</strong>.
</div>

<!-- ==================== 12. STEP 2 MODELO Y PROCESSOR ==================== -->
<div class="page-break"></div>
<h1 class="section">12. Step 2: nuevo modelo y processor</h1>

<h2>EmpleadoReporte: un modelo diferente</h2>

<p>El Step 2 necesita un campo extra: <code>salarioTotal</code>. Creamos un nuevo POJO:</p>

<pre><code>public class EmpleadoReporte {

    private String nombre;
    private String departamento;
    private double salario;
    private double bono;
    private double salarioTotal;    // &lt;-- campo nuevo

    // constructor vacio + getters y setters para todos los campos
}</code></pre>

<h2>ReporteProcessor: tipos diferentes de entrada y salida</h2>

<pre><code>public class ReporteProcessor
        implements ItemProcessor&lt;Empleado, EmpleadoReporte&gt; {

    private static final Logger log =
        LoggerFactory.getLogger(ReporteProcessor.class);

    @Override
    public EmpleadoReporte process(Empleado empleado) {
        EmpleadoReporte reporte = new EmpleadoReporte();
        reporte.setNombre(empleado.getNombre());
        reporte.setDepartamento(empleado.getDepartamento());
        reporte.setSalario(empleado.getSalario());
        reporte.setBono(empleado.getBono());
        reporte.setSalarioTotal(
            empleado.getSalario() + empleado.getBono());

        log.info("Step 2 - Reporte: {}", reporte);
        return reporte;
    }
}</code></pre>

<h2>Tipos diferentes: Empleado entra, EmpleadoReporte sale</h2>

<pre><code>ItemProcessor&lt;Empleado, EmpleadoReporte&gt;
                 │              │
                 │              └── SALE un EmpleadoReporte (con salarioTotal)
                 └── ENTRA un Empleado (leido de MySQL)</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> En v1 el processor era <code>&lt;Empleado, Empleado&gt;</code> (mismo tipo).
  En v2 es <code>&lt;Empleado, EmpleadoReporte&gt;</code> (tipos diferentes). Esto demuestra que el
  processor puede <strong>transformar</strong> el tipo de dato, no solo modificarlo.
</div>

<!-- ==================== 13. STEP 2 READER BD ==================== -->
<div class="page-break"></div>
<h1 class="section">13. Step 2: Reader de base de datos</h1>

<h2>JdbcCursorItemReader: leer de MySQL</h2>

<pre><code>@Bean
public JdbcCursorItemReader&lt;Empleado&gt; leerDeBd(DataSource dataSource) {
    return new JdbcCursorItemReaderBuilder&lt;Empleado&gt;()
            .name("empleadoDbReader")
            .dataSource(dataSource)
            .sql("SELECT nombre, departamento, salario, bono "
               + "FROM empleados_procesados")
            .rowMapper((rs, rowNum) -&gt; {
                Empleado empleado = new Empleado();
                empleado.setNombre(rs.getString("nombre"));
                empleado.setDepartamento(rs.getString("departamento"));
                empleado.setSalario(rs.getDouble("salario"));
                empleado.setBono(rs.getDouble("bono"));
                return empleado;
            })
            .build();
}</code></pre>

<h2>El rowMapper: convertir filas SQL a objetos Java</h2>

<p>El <code>rowMapper</code> es una funcion que Spring llama <strong>por cada fila</strong> del resultado SQL:</p>

<pre><code>Fila SQL: | JUAN PEREZ | VENTAS | 25000.0 | 2500.0 |
                │            │         │         │
                ▼            ▼         ▼         ▼
      rs.getString   rs.getString  rs.getDouble  rs.getDouble
       ("nombre")  ("departamento") ("salario")    ("bono")
                │            │         │         │
                ▼            ▼         ▼         ▼
         setNombre()  setDepartamento() setSalario() setBono()
                │            │         │         │
                └────────────┴─────────┴─────────┘
                              │
                        Empleado completo</code></pre>

<div class="callout callout-nota">
  <strong>Nota:</strong> Usamos una <strong>lambda</strong> porque <code>RowMapper</code> es una interfaz
  funcional (tiene un solo metodo abstracto). Es lo mismo que vimos ayer con <code>Runnable</code>
  y los threads.
</div>

<!-- ==================== 14. STEP 2 WRITER CSV ==================== -->
<div class="page-break"></div>
<h1 class="section">14. Step 2: Writer a archivo CSV</h1>

<h2>FlatFileItemWriter: escribir un CSV de salida</h2>

<pre><code>@Bean
public FlatFileItemWriter&lt;EmpleadoReporte&gt; escribirCsv() {
    return new FlatFileItemWriterBuilder&lt;EmpleadoReporte&gt;()
            .name("reporteWriter")
            .resource(new FileSystemResource("reporte-empleados.csv"))
            .headerCallback(writer -&gt; writer.write(
                "nombre,departamento,salario,bono,salario_total"))
            .delimited()
            .names("nombre", "departamento", "salario",
                   "bono", "salarioTotal")
            .build();
}</code></pre>

<h2>ClassPathResource vs FileSystemResource</h2>

<table>
  <tr><th>Tipo</th><th>Donde busca</th><th>Uso tipico</th></tr>
  <tr><td><code>ClassPathResource</code></td><td>Dentro de <code>src/main/resources/</code></td><td>Archivos de <strong>entrada</strong> empaquetados en el proyecto</td></tr>
  <tr><td><code>FileSystemResource</code></td><td>En el <strong>disco duro</strong> (raiz del proyecto)</td><td>Archivos de <strong>salida</strong> generados por la aplicacion</td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> El CSV de entrada (<code>empleados.csv</code>) se lee con
  <code>ClassPathResource</code> porque es parte del proyecto. El CSV de salida
  (<code>reporte-empleados.csv</code>) se escribe con <code>FileSystemResource</code>
  porque es un archivo <strong>generado</strong> en tiempo de ejecucion.
</div>

<h2>El archivo generado</h2>

<pre><code>nombre,departamento,salario,bono,salario_total
JUAN PEREZ,VENTAS,25000.0,2500.0,27500.0
MARIA LOPEZ,TI,35000.0,3500.0,38500.0
CARLOS GARCIA,RRHH,28000.0,2800.0,30800.0
...</code></pre>

<div class="callout callout-nota">
  <strong>Nota en Eclipse:</strong> El archivo <code>reporte-empleados.csv</code> aparece en la raiz
  del proyecto. Si no lo ves, haz clic derecho en el proyecto → <strong>Refresh</strong> (o presiona <strong>F5</strong>).
</div>

<!-- ==================== 15. CONFIG COMPLETA V2 ==================== -->
<div class="page-break"></div>
<h1 class="section">15. La configuracion completa de v2</h1>

<h2>BatchConfig.java con los dos Steps</h2>

<pre><code>@Configuration
public class BatchConfig {

    // =============== STEP 1: CSV → MySQL ===============

    @Bean
    public FlatFileItemReader&lt;Empleado&gt; leerCsv() { ... }

    @Bean
    public EmpleadoProcessor procesarEmpleado() { ... }

    @Bean
    public JdbcBatchItemWriter&lt;Empleado&gt; escribirEnBd(DataSource ds) { ... }

    @Bean
    public Step paso1(...) {
        return new StepBuilder("paso1", jobRepository)
                .&lt;Empleado, Empleado&gt;chunk(3, tx)   // mismo tipo
                .reader(leerCsv)
                .processor(procesarEmpleado)
                .writer(escribirEnBd)
                .build();
    }

    // =============== STEP 2: MySQL → CSV ===============

    @Bean
    public JdbcCursorItemReader&lt;Empleado&gt; leerDeBd(DataSource ds) { ... }

    @Bean
    public ReporteProcessor procesarReporte() { ... }

    @Bean
    public FlatFileItemWriter&lt;EmpleadoReporte&gt; escribirCsv() { ... }

    @Bean
    public Step paso2(...) {
        return new StepBuilder("paso2", jobRepository)
                .&lt;Empleado, EmpleadoReporte&gt;chunk(3, tx)  // tipos diferentes!
                .reader(leerDeBd)
                .processor(procesarReporte)
                .writer(escribirCsv)
                .build();
    }

    // =============== JOB ===============

    @Bean
    public Job procesarEmpleadosJob(JobRepository repo,
                                    Step paso1, Step paso2) {
        return new JobBuilder("procesarEmpleadosJob", repo)
                .start(paso1)
                .next(paso2)
                .build();
    }
}</code></pre>

<!-- ==================== 16. COMPARACION V1 VS V2 ==================== -->
<div class="page-break"></div>
<h1 class="section">16. Comparacion: v1 vs v2</h1>

<h2>Componentes por proyecto</h2>

<table>
  <tr><th>Componente</th><th>v1</th><th>v2</th></tr>
  <tr><td>Steps</td><td>1</td><td>2</td></tr>
  <tr><td>Readers</td><td>FlatFileItemReader (CSV)</td><td>+ JdbcCursorItemReader (BD)</td></tr>
  <tr><td>Processors</td><td>EmpleadoProcessor</td><td>+ ReporteProcessor</td></tr>
  <tr><td>Writers</td><td>JdbcBatchItemWriter (BD)</td><td>+ FlatFileItemWriter (CSV)</td></tr>
  <tr><td>Modelos</td><td>Empleado</td><td>+ EmpleadoReporte</td></tr>
  <tr><td>Tipos del Processor</td><td><code>&lt;Empleado, Empleado&gt;</code></td><td>+ <code>&lt;Empleado, EmpleadoReporte&gt;</code></td></tr>
</table>

<h2>Flujo completo de v2</h2>

<pre><code>empleados.csv                              reporte-empleados.csv
 (10 registros)                             (10 registros)
      │                                           ▲
      ▼                                           │
 ┌─────────┐  ┌───────────────┐  ┌──────────┐    │
 │ Reader  │─→│  Processor    │─→│  Writer   │    │
 │ CSV     │  │  MAYUSCULAS   │  │  MySQL    │    │
 │         │  │  bono = 10%   │  │  INSERT   │    │
 └─────────┘  └───────────────┘  └──────────┘    │
                                      │           │
                STEP 1                │           │
 ─────────────────────────────────────┼───────────│──
                STEP 2                │           │
                                      ▼           │
             ┌──────────┐  ┌──────────────┐  ┌─────────┐
             │  Reader  │─→│  Processor   │─→│  Writer │
             │  MySQL   │  │  salarioTotal│  │  CSV    │
             │  SELECT  │  │  = sal + bono│  │  archivo│
             └──────────┘  └──────────────┘  └─────────┘</code></pre>

<!-- ==================== 17. APPLICATION PROPERTIES ==================== -->
<div class="page-break"></div>
<h1 class="section">17. application.properties explicado</h1>

<pre><code># Conexion a MySQL (contenedor docker mysql-academia)
spring.datasource.url=jdbc:mysql://localhost:3306/academia
spring.datasource.username=alumno
spring.datasource.password=alumno123
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# Spring Batch crea automaticamente las tablas BATCH_* en MySQL
spring.batch.jdbc.initialize-schema=always

# Ejecutar el Job automaticamente al iniciar la aplicacion
spring.batch.job.enabled=true</code></pre>

<h2>Que crea Spring Boot con estas propiedades</h2>

<table>
  <tr><th>Propiedad</th><th>Que hace Spring Boot</th></tr>
  <tr><td><code>spring.datasource.*</code></td><td>Crea un <code>DataSource</code> (conexion a MySQL) y lo inyecta donde se necesite</td></tr>
  <tr><td><code>spring.batch.jdbc.initialize-schema=always</code></td><td>Crea las 9 tablas <code>BATCH_*</code> automaticamente al iniciar</td></tr>
  <tr><td><code>spring.batch.job.enabled=true</code></td><td>Ejecuta el Job inmediatamente al arrancar la aplicacion</td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> Con solo 6 lineas de configuracion, Spring Boot crea automaticamente:
  el <code>DataSource</code>, el <code>JobRepository</code>, el <code>PlatformTransactionManager</code>,
  y las tablas de metadatos. Sin estas propiedades, tendriamos que crear todo manualmente.
</div>

<!-- ==================== 18. DEPENDENCIAS MAVEN ==================== -->
<div class="page-break"></div>
<h1 class="section">18. Dependencias Maven</h1>

<pre><code>&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-batch&lt;/artifactId&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;com.mysql&lt;/groupId&gt;
        &lt;artifactId&gt;mysql-connector-j&lt;/artifactId&gt;
        &lt;scope&gt;runtime&lt;/scope&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;</code></pre>

<p>Solo 2 dependencias:</p>

<table>
  <tr><th>Dependencia</th><th>Que incluye</th></tr>
  <tr><td><code>spring-boot-starter-batch</code></td><td>Spring Batch + Spring Boot + Spring JDBC + transacciones</td></tr>
  <tr><td><code>mysql-connector-j</code></td><td>Driver JDBC para conectarse a MySQL</td></tr>
</table>

<div class="callout callout-nota">
  <strong>Nota:</strong> <code>spring-boot-starter-batch</code> incluye todo lo que necesitamos. Spring Boot
  se encarga de versiones compatibles gracias al <code>&lt;parent&gt;</code> en el <code>pom.xml</code>.
  No necesitamos especificar versiones individuales.
</div>

<h2>La tabla SQL necesaria</h2>

<p>Antes de ejecutar, debes crear la tabla destino en MySQL:</p>

<pre><code>CREATE TABLE IF NOT EXISTS empleados_procesados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    departamento VARCHAR(50),
    salario DOUBLE,
    bono DOUBLE
);</code></pre>

<p>Las tablas <code>BATCH_*</code> las crea Spring Batch automaticamente gracias a la propiedad
<code>spring.batch.jdbc.initialize-schema=always</code>.</p>

<!-- ==================== 19. RESUMEN ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Resumen de conceptos clave</h1>

<table>
  <tr><th>Concepto</th><th>Descripcion</th></tr>
  <tr><td>Spring Batch</td><td>Framework para procesamiento por lotes (grandes volumenes de datos)</td></tr>
  <tr><td>Job</td><td>El trabajo completo. Contiene uno o mas Steps</td></tr>
  <tr><td>Step</td><td>Un paso: Reader + Processor + Writer</td></tr>
  <tr><td><code>ItemReader</code></td><td>Lee datos de una fuente (CSV, BD)</td></tr>
  <tr><td><code>ItemProcessor</code></td><td>Transforma cada registro. Puede cambiar el tipo de dato</td></tr>
  <tr><td><code>ItemWriter</code></td><td>Escribe los resultados (BD, CSV)</td></tr>
  <tr><td><code>chunk(N)</code></td><td>Procesa N registros por transaccion</td></tr>
  <tr><td><code>JobRepository</code></td><td>Tablas <code>BATCH_*</code> que guardan el estado de cada ejecucion</td></tr>
  <tr><td><code>@Configuration</code></td><td>Marca la clase como fuente de beans (recetas)</td></tr>
  <tr><td><code>@Bean</code></td><td>Marca un metodo cuyo resultado Spring guarda e inyecta</td></tr>
  <tr><td><code>ClassPathResource</code></td><td>Busca archivos dentro de <code>src/main/resources/</code></td></tr>
  <tr><td><code>FileSystemResource</code></td><td>Busca/crea archivos en el disco (fuera del jar)</td></tr>
  <tr><td><code>beanMapped()</code></td><td>Mapea <code>:parametros</code> SQL a los getters del POJO</td></tr>
  <tr><td><code>rowMapper</code></td><td>Funcion que convierte cada fila SQL en un objeto Java</td></tr>
  <tr><td><code>.start().next()</code></td><td>Define el orden de ejecucion de los Steps</td></tr>
</table>

<!-- ==================== 20. PROGRESION ==================== -->
<div class="page-break"></div>
<h2>Progresion de los ejercicios del dia</h2>

<table>
  <tr><th>Proyecto</th><th>Paquete</th><th>Version</th><th>Tema</th></tr>
  <tr><td>springBatch</td><td><code>com.academia.batch</code></td><td>v1</td><td>CSV → MySQL (1 Step)</td></tr>
  <tr><td>springBatch</td><td><code>com.academia.batch</code></td><td>v1</td><td><code>FlatFileItemReader</code> lee CSV</td></tr>
  <tr><td>springBatch</td><td><code>com.academia.batch</code></td><td>v1</td><td><code>EmpleadoProcessor</code> transforma datos</td></tr>
  <tr><td>springBatch</td><td><code>com.academia.batch</code></td><td>v1</td><td><code>JdbcBatchItemWriter</code> escribe en BD</td></tr>
  <tr><td>springBatch</td><td><code>com.academia.batch</code></td><td>v1</td><td><code>chunk(3)</code> procesamiento por bloques</td></tr>
  <tr><td>springBatchV2</td><td><code>com.academia.batch</code></td><td>v2</td><td>Dos Steps: <code>.start().next()</code></td></tr>
  <tr><td>springBatchV2</td><td><code>com.academia.batch</code></td><td>v2</td><td><code>JdbcCursorItemReader</code> lee de BD</td></tr>
  <tr><td>springBatchV2</td><td><code>com.academia.batch</code></td><td>v2</td><td><code>ReporteProcessor</code> tipos diferentes</td></tr>
  <tr><td>springBatchV2</td><td><code>com.academia.batch</code></td><td>v2</td><td><code>FlatFileItemWriter</code> genera CSV</td></tr>
  <tr><td>springBatchV2</td><td><code>com.academia.batch</code></td><td>v2</td><td><code>ClassPathResource</code> vs <code>FileSystemResource</code></td></tr>
</table>

</body>
</html>"""

if __name__ == "__main__":
    output_path = "/Users/mike/Desarrollo/academiafebrero26CDMX/documents/actividadXdia/200226.pdf"
    html = weasyprint.HTML(string=HTML_CONTENT)
    html.write_pdf(output_path)
    print(f"PDF generado: {output_path}")
