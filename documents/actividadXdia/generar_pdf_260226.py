#!/usr/bin/env python3
"""
Genera el PDF de la Guia de Repaso del 26 de febrero de 2026.
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
      content: "Pagina " counter(page) "/16";
      font-size: 10px;
      color: #999;
    }
    @top-left {
      content: "Curso de Java - Stream API Avanzado";
      font-size: 9px;
      color: #999;
    }
    @top-right {
      content: "Semana 03 | 26 Feb 2026";
      font-size: 9px;
      color: #999;
    }
  }

  @page:first {
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: "Pagina 1/16"; font-size: 10px; color: #999; }
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
  <h2>Optional y Stream API Avanzado</h2>
  <div class="separator"></div>
  <p class="info">Semana 03 - Jueves 26 de Febrero de 2026</p>
  <p class="info">Academia Java - Ciudad de Mexico</p>

  <p class="temas-title">Temas del dia:</p>
  <ol class="temas">
    <li>Optional: <code>orElse</code> y <code>orElseGet</code> con metodo que retorna Optional</li>
    <li>Stream API: IntStream con filter, peek, map y count</li>
    <li>Stream API: IntStream con filter, peek, map y sum</li>
    <li>Stream API: <code>boxed()</code> y <code>flatMap</code> para aplanar listas</li>
    <li>Stream API: flatMap con collect a List</li>
    <li>Stream API: <code>Stream.iterate()</code> con seed y Predicate</li>
    <li>Stream API: <code>reduce()</code> con Optional (sin identidad)</li>
    <li>Stream API: <code>reduce()</code> con identidad (sin Optional)</li>
    <li>Stream API: <code>Collectors.toCollection()</code> con TreeSet</li>
    <li>Stream API: <code>IntSummaryStatistics</code> para estadisticas agregadas</li>
    <li>Stream API: <code>Collectors.toMap()</code> con merge function y TreeMap</li>
  </ol>

  <p class="instructor">Instructor: Miguel Rugerio</p>
</div>

<!-- ==================== SECCION 1: OPTIONAL ==================== -->
<h1 class="section">1. Optional: orElse y orElseGet con metodo que retorna Optional</h1>

<p>Retomamos Optional con un patron comun: un metodo que retorna <code>Optional</code> para manejar la ausencia de resultado.</p>

<h2>El codigo: optional v2</h2>

<pre><code>public static Optional&lt;Double&gt; average(int... scores) {
    if (scores.length == 0) {
        return Optional.empty();
    }
    int sum = 0;
    for (int score : scores)
        sum += score;
    return Optional.of((double) sum / scores.length);
}

public static void main(String[] args) {
    Optional&lt;Double&gt; opt = average(); // sin argumentos

    System.out.println(opt);                           // Optional.empty
    System.out.println(opt.orElse(Double.NaN));        // NaN
    System.out.println(opt.orElseGet(() -&gt; Math.random())); // numero aleatorio
}</code></pre>

<h2>Flujo de ejecucion</h2>

<pre><code>average()  &lt;- sin argumentos (scores.length == 0)
    |
    v
return Optional.empty()
    |
    v
opt.orElse(Double.NaN)           -&gt; NaN (valor por defecto directo)
opt.orElseGet(() -&gt; Math.random()) -&gt; 0.xxxx (Supplier genera el valor)</code></pre>

<h2>orElse vs orElseGet: diferencia clave</h2>

<pre><code>orElse(valor):
  -&gt; El valor se EVALUA SIEMPRE, tenga o no dato el Optional
  -&gt; Ejemplo: orElse(calcularDefault()) &lt;- calcularDefault() se ejecuta siempre

orElseGet(Supplier):
  -&gt; El Supplier se ejecuta SOLO si el Optional esta vacio
  -&gt; Ejemplo: orElseGet(() -&gt; calcularDefault()) &lt;- solo si esta vacio

Para valores simples (NaN, 0, "") -&gt; orElse esta bien
Para valores costosos (BD, API) -&gt; orElseGet es preferible</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Un metodo puede retornar <code>Optional</code> para indicar que el resultado puede no existir. <code>orElse()</code> evalua el valor default siempre; <code>orElseGet()</code> solo lo evalua cuando el Optional esta vacio (evaluacion lazy).
</div>

<!-- ==================== SECCION 2 ==================== -->
<div class="page-break"></div>
<h1 class="section">2. Stream API: IntStream con filter, peek, map y count</h1>

<p>Pasamos al tema principal del dia: <strong>Stream API avanzado</strong>. Comenzamos con <code>IntStream</code>, un Stream especializado para primitivos <code>int</code>.</p>

<h2>El codigo: Stream v1 Principal</h2>

<pre><code>int[] enteros = {1,2,3,4,5,6,7,8,9,0};

IntStream stream = Arrays.stream(enteros);

long l = stream.filter(n -&gt; n%2==0)
      .peek(System.out::println)
      .map(x -&gt; x*10)
      .count();

System.out.println("Count: "+l);</code></pre>

<h2>Salida del programa</h2>

<pre><code>2          &lt;- peek imprime los pares ANTES de map
4
6
8
0
Count: 5   &lt;- 5 elementos pasaron el filtro</code></pre>

<h2>Pipeline paso a paso</h2>

<pre><code>Source:       [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    |
filter(n%2==0): [2, 4, 6, 8, 0]  &lt;- solo pares
    |
peek(println):  imprime cada par (2, 4, 6, 8, 0)
    |
map(x*10):     [20, 40, 60, 80, 0]  &lt;- multiplica por 10
    |
count():       5  &lt;- cuenta los elementos</code></pre>

<h2>IntStream vs Stream&lt;Integer&gt;</h2>

<pre><code>Arrays.stream(int[])  -&gt; IntStream  (primitivos, mas eficiente)
list.stream()         -&gt; Stream&lt;T&gt;  (objetos)

IntStream tiene operaciones especializadas: sum(), average(), max(), min()</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>IntStream</code> es un Stream primitivo para <code>int</code>. <code>peek()</code> permite observar elementos en cualquier punto del pipeline sin modificarlos. <code>count()</code> es una operacion terminal que retorna <code>long</code>.
</div>

<!-- ==================== SECCION 3 ==================== -->
<div class="page-break"></div>
<h1 class="section">3. Stream API: IntStream con sum</h1>

<h2>El codigo: Stream v1 Principal2</h2>

<pre><code>int[] enteros = {1,2,3,4,5,6,7,8,9,0};

IntStream stream = Arrays.stream(enteros);

long l = stream.filter(n -&gt; n%2==0)
      .peek(System.out::println) //Lazy
      .map(x -&gt; x*10)
      .sum();

System.out.println("Sum: "+l);</code></pre>

<h2>Salida del programa</h2>

<pre><code>2
4
6
8
0
Sum: 200   &lt;- 20+40+60+80+0 = 200</code></pre>

<h2>count() vs sum()</h2>

<pre><code>count():  cuenta CUANTOS elementos hay        -&gt; 5
sum():    SUMA los valores de los elementos    -&gt; 200

Ambos son operaciones TERMINALES de IntStream.
count() ignora los valores, sum() los acumula.</code></pre>

<h2>Lazy evaluation: peek demuestra el orden</h2>

<pre><code>peek imprime: 2, 4, 6, 8, 0 (valores ANTES de map)
sum suma:     20+40+60+80+0 = 200 (valores DESPUES de map)

Si no hubiera operacion terminal, peek NO imprimiria nada.
Las operaciones intermedias son LAZY: solo se ejecutan cuando
hay una operacion terminal que las necesita.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>sum()</code> es exclusiva de <code>IntStream</code> (no existe en <code>Stream&lt;Integer&gt;</code>). Las operaciones intermedias (filter, peek, map) son lazy: no se ejecutan hasta que una operacion terminal (count, sum) las activa.
</div>

<!-- ==================== SECCION 4 ==================== -->
<div class="page-break"></div>
<h1 class="section">4. Stream API: boxed() y flatMap</h1>

<h2>El codigo: Stream v1 Principal3</h2>

<pre><code>int[] enteros1 = {1,2,3,4,5,6,7,8,9,10};
int[] enteros2 = {11,12,13,14,15,16,17,18,19,20};
int[] enteros3 = {51,52,53,54,55,56,57,58,59,60};

List&lt;Integer&gt; list1 = Arrays.stream(enteros1) //IntStream
                        .boxed()              //Stream&lt;Integer&gt;
                        .toList();            //List&lt;Integer&gt;

List&lt;Integer&gt; list2 = Arrays.stream(enteros2).boxed().toList();
List&lt;Integer&gt; list3 = Arrays.stream(enteros3).boxed().toList();

Stream&lt;List&lt;Integer&gt;&gt; stream = Stream.of(list1, list2, list3);

Stream&lt;Integer&gt; streamEnteros = stream.flatMap(l -&gt; l.stream());

streamEnteros.forEach(System.out::println);</code></pre>

<h2>boxed(): de primitivo a objeto</h2>

<pre><code>Arrays.stream(int[])  -&gt; IntStream          (primitivos int)
    .boxed()          -&gt; Stream&lt;Integer&gt;    (objetos Integer)
    .toList()         -&gt; List&lt;Integer&gt;      (lista inmutable)

boxed() hace autoboxing: int -&gt; Integer
Necesario porque List&lt;int&gt; NO existe en Java, solo List&lt;Integer&gt;.</code></pre>

<h2>flatMap(): aplanar un Stream de listas</h2>

<pre><code>Stream&lt;List&lt;Integer&gt;&gt;  &lt;- 3 listas separadas
    |
    v  flatMap(l -&gt; l.stream())
    |
Stream&lt;Integer&gt;  &lt;- todos los elementos en un solo stream

Antes:  [[1,2,...,10], [11,12,...,20], [51,52,...,60]]
            lista 1       lista 2        lista 3

Despues: [1, 2, 3, ..., 10, 11, 12, ..., 20, 51, 52, ..., 60]
         todos los elementos en secuencia</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>boxed()</code> convierte un <code>IntStream</code> a <code>Stream&lt;Integer&gt;</code> (autoboxing). <code>flatMap()</code> toma un Stream de colecciones y las "aplana" en un solo Stream con todos los elementos.
</div>

<!-- ==================== SECCION 5 ==================== -->
<div class="page-break"></div>
<h1 class="section">5. Stream API: flatMap con collect a List</h1>

<h2>El codigo: Stream v1 Principal4</h2>

<pre><code>// ... misma preparacion de listas ...

Stream&lt;List&lt;Integer&gt;&gt; stream = Stream.of(list1, list2, list3);

Stream&lt;Integer&gt; streamEnteros = stream.flatMap(l -&gt; l.stream());

List&lt;Integer&gt; lista = streamEnteros.toList();

System.out.println(lista);
// [1, 2, 3, ..., 10, 11, 12, ..., 20, 51, 52, ..., 60]</code></pre>

<h2>Diferencia con Principal3</h2>

<pre><code>Principal3: flatMap -&gt; forEach(println)      &lt;- imprime uno por uno
Principal4: flatMap -&gt; toList()              &lt;- recolecta en una lista

forEach() consume el stream imprimiendo cada elemento.
toList() consume el stream recolectando todos los elementos en una List.</code></pre>

<h2>toList() vs Collectors.toList()</h2>

<pre><code>stream.toList()              -&gt; List inmutable (Java 16+)
stream.collect(Collectors.toList()) -&gt; List mutable

toList() es mas conciso y retorna una lista que NO se puede modificar.
Si necesitas agregar/remover elementos despues, usa Collectors.toList().</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>flatMap()</code> + <code>toList()</code> es un patron comun para combinar multiples listas en una sola. <code>toList()</code> (Java 16+) es la forma moderna y concisa de recolectar, pero retorna una lista inmutable.
</div>

<!-- ==================== SECCION 6 ==================== -->
<div class="page-break"></div>
<h1 class="section">6. Stream API: Stream.iterate() con Predicate</h1>

<h2>El codigo: Stream v2 Principal</h2>

<pre><code>Stream&lt;Integer&gt; oddNumberUnder100 =
        Stream.iterate(
                1,             // seed (valor inicial)
                n -&gt; n &lt; 100,  // Predicate (cuando parar)
                n -&gt; n + 2);   // UnaryOperator (siguiente valor)

oddNumberUnder100.forEach(System.out::println);
// 1, 3, 5, 7, 9, ..., 97, 99

System.out.println("*************");

oddNumberUnder100 =
        Stream.iterate(
                0,             // seed
                n -&gt; n &lt; 50,   // Predicate
                n -&gt; n + 3);   // UnaryOperator

oddNumberUnder100.forEach(System.out::println);
// 0, 3, 6, 9, 12, ..., 48</code></pre>

<h2>Anatomia de Stream.iterate()</h2>

<pre><code>Stream.iterate(seed, predicate, unaryOperator)
                |        |           |
                v        v           v
        valor      ¿continuo?    siguiente
        inicial                   valor

Ejemplo 1: iterate(1, n -&gt; n &lt; 100, n -&gt; n + 2)
  1 -&gt; 3 -&gt; 5 -&gt; 7 -&gt; ... -&gt; 97 -&gt; 99 -&gt; STOP (101 &gt;= 100)

Ejemplo 2: iterate(0, n -&gt; n &lt; 50, n -&gt; n + 3)
  0 -&gt; 3 -&gt; 6 -&gt; 9 -&gt; ... -&gt; 45 -&gt; 48 -&gt; STOP (51 &gt;= 50)</code></pre>

<h2>Stream.iterate() de 3 parametros (Java 9+)</h2>

<pre><code>Java 8:  Stream.iterate(seed, unaryOperator)  -&gt; Stream INFINITO
Java 9+: Stream.iterate(seed, predicate, unaryOperator) -&gt; Stream FINITO

La version con Predicate es similar a un for:
  for (int n = 0; n &lt; 50; n += 3)  equivale a
  Stream.iterate(0, n -&gt; n &lt; 50, n -&gt; n + 3)</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>Stream.iterate()</code> con 3 parametros genera una secuencia finita: seed (inicio), Predicate (condicion de continuacion) y UnaryOperator (generador del siguiente valor). Es el equivalente funcional de un bucle <code>for</code>.
</div>

<!-- ==================== SECCION 7 ==================== -->
<div class="page-break"></div>
<h1 class="section">7. Stream API: reduce() con Optional</h1>

<h2>El codigo: Stream v3 Principal</h2>

<pre><code>int arreglo[] = {1,2,3,4,5};

arreglo = new int[]{};  // arreglo VACIO

Stream&lt;Integer&gt; stream1 = Arrays.stream(arreglo) //IntStream
                             .boxed();            //Stream&lt;Integer&gt;

Optional&lt;Integer&gt; opt = stream1.reduce((x,y) -&gt; x*y);
opt.ifPresent(System.out::println);
System.out.println(opt.orElseGet(() -&gt; 1));</code></pre>

<h2>reduce() sin identidad retorna Optional</h2>

<pre><code>reduce(BinaryOperator)  -&gt; Optional&lt;T&gt;

Con arreglo {1,2,3,4,5}:
  Paso 1: 1 * 2 = 2
  Paso 2: 2 * 3 = 6
  Paso 3: 6 * 4 = 24
  Paso 4: 24 * 5 = 120
  Resultado: Optional[120]

Con arreglo vacio {}:
  No hay elementos -&gt; Optional.empty
  ifPresent: no imprime nada
  orElseGet(() -&gt; 1): retorna 1</code></pre>

<h2>Diagrama de reduce()</h2>

<pre><code>reduce((x,y) -&gt; x*y) con [1, 2, 3, 4, 5]:

    1   2
     \ /
      2   3       x*y: acumulador
       \ /
        6   4
         \ /
         24   5
          \ /
          120  -&gt; Optional[120]</code></pre>

<h2>Por que retorna Optional?</h2>

<pre><code>Si el Stream esta VACIO, no hay valor que retornar.
Optional maneja esa posibilidad:
  - Stream con datos -&gt; Optional[resultado]
  - Stream vacio     -&gt; Optional.empty</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>reduce()</code> sin identidad retorna <code>Optional</code> porque el Stream podria estar vacio. Combina todos los elementos usando un <code>BinaryOperator</code> (acumulador). Si hay 0 elementos, retorna <code>Optional.empty</code>.
</div>

<!-- ==================== SECCION 8 ==================== -->
<div class="page-break"></div>
<h1 class="section">8. Stream API: reduce() con identidad</h1>

<h2>El codigo: Stream v4 Principal</h2>

<pre><code>int arreglo[] = {1,2,3,4,5};

arreglo = new int[]{};

Stream&lt;Integer&gt; stream1 = Arrays.stream(arreglo) //IntStream
                             .boxed();            //Stream&lt;Integer&gt;

int r = stream1.reduce(1, (x,y) -&gt; x*y);

System.out.println(r);</code></pre>

<h2>reduce() con identidad retorna T (no Optional)</h2>

<pre><code>reduce(identity, BinaryOperator)  -&gt; T

Con arreglo {1,2,3,4,5}:
  Paso 0: identidad = 1  (valor inicial)
  Paso 1: 1 * 1 = 1
  Paso 2: 1 * 2 = 2
  Paso 3: 2 * 3 = 6
  Paso 4: 6 * 4 = 24
  Paso 5: 24 * 5 = 120
  Resultado: 120

Con arreglo vacio {}:
  Solo hay identidad = 1
  Resultado: 1  (la identidad se retorna directamente)</code></pre>

<h2>Diferencia entre las dos versiones de reduce</h2>

<pre><code>reduce((x,y) -&gt; x*y)           -&gt; Optional&lt;Integer&gt;
  - Sin identidad
  - Stream vacio -&gt; Optional.empty
  - Necesita orElse/orElseGet para extraer valor

reduce(1, (x,y) -&gt; x*y)       -&gt; int
  - Con identidad = 1
  - Stream vacio -&gt; retorna 1 (la identidad)
  - NO necesita Optional, siempre tiene resultado</code></pre>

<h2>Que es la identidad?</h2>

<pre><code>Es el valor que, al combinarse con cualquier elemento, retorna ese elemento.

Para multiplicacion: identidad = 1  (1 * x = x)
Para suma:          identidad = 0  (0 + x = x)
Para concatenacion: identidad = "" ("" + s = s)</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>reduce(identity, BinaryOperator)</code> siempre retorna un valor (no Optional) porque si el Stream esta vacio, retorna la identidad. La identidad es el elemento neutro de la operacion.
</div>

<!-- ==================== SECCION 9 ==================== -->
<div class="page-break"></div>
<h1 class="section">9. Stream API: Collectors.toCollection() con TreeSet</h1>

<h2>El codigo: Stream v5 Principal</h2>

<pre><code>Stream&lt;String&gt; stream = Stream.of("w", "o", "l", "f");

Collector&lt;String,?,TreeSet&lt;String&gt;&gt; collector =
        Collectors.toCollection(() -&gt; new TreeSet&lt;String&gt;());

TreeSet&lt;String&gt; set = stream.collect(collector);

System.out.println(set); // [f, l, o, w]</code></pre>

<h2>Que hace Collectors.toCollection()?</h2>

<pre><code>Collectors.toCollection(Supplier)
                          |
                          v
                   crea la coleccion destino

Collectors.toList()                    -&gt; ArrayList (no controlas el tipo)
Collectors.toSet()                     -&gt; HashSet (no controlas el tipo)
Collectors.toCollection(TreeSet::new)  -&gt; TreeSet (TU eliges el tipo)</code></pre>

<h2>Por que TreeSet ordena los elementos?</h2>

<pre><code>Stream:  ["w", "o", "l", "f"]  &lt;- orden de insercion
TreeSet: [f, l, o, w]          &lt;- orden natural (alfabetico)

TreeSet ordena automaticamente sus elementos.
HashSet NO garantiza orden.
ArrayList mantiene orden de insercion.</code></pre>

<h2>El Collector desglosado</h2>

<pre><code>Collector&lt;String, ?, TreeSet&lt;String&gt;&gt;
    |          |           |
    T          A           R
    |          |           |
  tipo de    tipo       tipo de
  entrada   intermedio  resultado</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>Collectors.toCollection(Supplier)</code> permite elegir exactamente que tipo de coleccion usar. El Supplier crea la instancia de la coleccion. <code>TreeSet::new</code> ordena los elementos automaticamente.
</div>

<!-- ==================== SECCION 10 ==================== -->
<div class="page-break"></div>
<h1 class="section">10. Stream API: IntSummaryStatistics</h1>

<h2>El codigo: Stream v6 Principal</h2>

<pre><code>IntStream ints = IntStream.of(51, 2, 8, 0, 23, 32);

IntSummaryStatistics stats = ints.summaryStatistics();

System.out.println("Average: " + stats.getAverage()); // 19.333...
System.out.println("Count: " + stats.getCount());     // 6
System.out.println("Max: " + stats.getMax());          // 51
System.out.println("Min: " + stats.getMin());          // 0
System.out.println("Sum: " + stats.getSum());          // 116</code></pre>

<h2>summaryStatistics(): todas las estadisticas en una sola pasada</h2>

<pre><code>Sin summaryStatistics (consume el stream 5 veces -&gt; ERROR):
  ints.average()  -&gt; necesita un stream
  ints.count()    -&gt; necesita OTRO stream (el primero ya se consumio)
  ints.max()      -&gt; necesita OTRO stream
  ...

Con summaryStatistics (consume el stream UNA sola vez):
  IntSummaryStatistics stats = ints.summaryStatistics();
  stats.getAverage()  -&gt; todas las estadisticas
  stats.getCount()    -&gt; disponibles del mismo
  stats.getMax()      -&gt; objeto, sin crear
  stats.getMin()      -&gt; nuevos streams
  stats.getSum()</code></pre>

<h2>Los 5 metodos de IntSummaryStatistics</h2>

<table>
  <tr><th>Metodo</th><th>Retorna</th><th>Ejemplo</th></tr>
  <tr><td><code>getAverage()</code></td><td>double</td><td>19.333...</td></tr>
  <tr><td><code>getCount()</code></td><td>long</td><td>6</td></tr>
  <tr><td><code>getMax()</code></td><td>int</td><td>51</td></tr>
  <tr><td><code>getMin()</code></td><td>int</td><td>0</td></tr>
  <tr><td><code>getSum()</code></td><td>long</td><td>116</td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>summaryStatistics()</code> recolecta average, count, max, min y sum en una sola pasada del Stream. Es eficiente porque un Stream solo se puede consumir una vez.
</div>

<!-- ==================== SECCION 11 ==================== -->
<div class="page-break"></div>
<h1 class="section">11. Stream API: Collectors.toMap()</h1>

<h2>Version 1: toMap basico (key, value)</h2>

<pre><code>Stream&lt;String&gt; ohMy = Stream.of("lions", "tigers", "bears");

Map&lt;String, Integer&gt; map1 = ohMy.collect(
                    Collectors.toMap(s -&gt; s, String::length));

System.out.println(map1); // {lions=5, bears=5, tigers=6}</code></pre>

<h2>Version 2: toMap con merge function (manejo de duplicados)</h2>

<pre><code>ohMy = Stream.of("lions", "tigers", "bears", "lions", "pato");

Map&lt;Integer, String&gt; map2 = ohMy.collect(
        Collectors.toMap(
            String::length,          // key: longitud
            k -&gt; k,                  // value: el string
            (s1, s2) -&gt; s1 + "," + s2)); // merge: concatenar

System.out.println(map2); // {4=pato, 5=lions,bears,lions, 6=tigers}</code></pre>

<h2>Version 3: toMap con TreeMap (tipo de mapa especifico)</h2>

<pre><code>ohMy = Stream.of("lions", "tigers", "bears", "lions", "pato");

TreeMap&lt;Integer, String&gt; map = ohMy.collect(
        Collectors.toMap(
            String::length,
            k -&gt; k,
            (s1, s2) -&gt; s1 + "," + s2,
            TreeMap::new));

System.out.println(map.getClass()); // TreeMap
System.out.println(map);            // {4=pato, 5=lions,bears,lions, 6=tigers}</code></pre>

<h2>Las 3 versiones de toMap()</h2>

<pre><code>toMap(keyMapper, valueMapper)
  -&gt; 2 parametros, sin duplicados permitidos

toMap(keyMapper, valueMapper, mergeFunction)
  -&gt; 3 parametros, define que hacer con claves duplicadas

toMap(keyMapper, valueMapper, mergeFunction, mapSupplier)
  -&gt; 4 parametros, ademas eliges el tipo de Map</code></pre>

<h2>Que es la merge function?</h2>

<pre><code>Cuando dos elementos generan la MISMA clave:

"lions" -&gt; length 5 -&gt; key=5, value="lions"
"bears" -&gt; length 5 -&gt; key=5, value="bears"   &lt;- CONFLICTO! misma key

Sin merge function: IllegalStateException
Con merge function: (s1, s2) -&gt; s1 + "," + s2 -&gt; "lions,bears"</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>Collectors.toMap()</code> tiene 3 sobrecargas. Con 2 parametros no permite claves duplicadas. Con 3 parametros, la merge function resuelve conflictos. Con 4 parametros, ademas eliges el tipo de Map (TreeMap, LinkedHashMap, etc.).
</div>

<!-- ==================== RESUMEN ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Resumen de conceptos clave</h1>

<table>
  <tr><th>Concepto</th><th>Descripcion</th></tr>
  <tr><td><code>orElse(v)</code></td><td>Retorna valor default, se evalua SIEMPRE</td></tr>
  <tr><td><code>orElseGet(Supplier)</code></td><td>Retorna valor default, se evalua solo si vacio (lazy)</td></tr>
  <tr><td><code>IntStream</code></td><td>Stream primitivo para <code>int</code>, mas eficiente que <code>Stream&lt;Integer&gt;</code></td></tr>
  <tr><td><code>count()</code></td><td>Terminal que cuenta elementos (retorna <code>long</code>)</td></tr>
  <tr><td><code>sum()</code></td><td>Terminal exclusiva de IntStream que suma valores</td></tr>
  <tr><td><code>boxed()</code></td><td>Convierte <code>IntStream</code> a <code>Stream&lt;Integer&gt;</code> (autoboxing)</td></tr>
  <tr><td><code>flatMap()</code></td><td>Aplana un Stream de colecciones en un solo Stream</td></tr>
  <tr><td><code>toList()</code></td><td>Terminal que recolecta en List inmutable (Java 16+)</td></tr>
  <tr><td><code>Stream.iterate(seed, pred, op)</code></td><td>Genera secuencia finita (Java 9+)</td></tr>
  <tr><td><code>reduce(BinaryOperator)</code></td><td>Acumula elementos, retorna <code>Optional</code></td></tr>
  <tr><td><code>reduce(identity, BinaryOperator)</code></td><td>Acumula con valor inicial, retorna <code>T</code></td></tr>
  <tr><td><code>Collectors.toCollection(Supplier)</code></td><td>Recolecta en coleccion especifica (TreeSet, etc.)</td></tr>
  <tr><td><code>summaryStatistics()</code></td><td>Obtiene avg, count, max, min, sum en una pasada</td></tr>
  <tr><td><code>Collectors.toMap(key, value)</code></td><td>Recolecta en Map (sin duplicados)</td></tr>
  <tr><td><code>Collectors.toMap(key, value, merge)</code></td><td>Recolecta en Map (con manejo de duplicados)</td></tr>
  <tr><td><code>Collectors.toMap(key, value, merge, supplier)</code></td><td>Recolecta en Map especifico (TreeMap, etc.)</td></tr>
</table>

<!-- ==================== PROGRESION ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Progresion de los ejercicios del dia</h1>

<table>
  <tr><th>Proyecto</th><th>Paquete</th><th>Version</th><th>Tema</th></tr>
  <tr><td>optional</td><td><code>com.curso</code></td><td>v2</td><td>Optional: orElse y orElseGet con metodo</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v1</td><td>IntStream: filter, peek, map y count</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v1</td><td>IntStream: filter, peek, map y sum</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v1</td><td>boxed() y flatMap con forEach</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v1</td><td>flatMap con collect a List</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v2</td><td>Stream.iterate() con Predicate</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v3</td><td>reduce() con Optional</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v4</td><td>reduce() con identidad</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v5</td><td>Collectors.toCollection() con TreeSet</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v6</td><td>IntSummaryStatistics</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v7</td><td>Collectors.toMap() con merge y TreeMap</td></tr>
</table>

</body>
</html>
"""

if __name__ == "__main__":
    html = weasyprint.HTML(string=HTML_CONTENT)
    html.write_pdf("260226.pdf")
    print("PDF generado: 260226.pdf")
