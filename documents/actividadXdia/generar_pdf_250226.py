#!/usr/bin/env python3
"""
Genera el PDF de la Guia de Repaso del 25 de febrero de 2026.
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
      content: "Pagina " counter(page) "/24";
      font-size: 10px;
      color: #999;
    }
    @top-left {
      content: "Curso de Java - Programacion Funcional";
      font-size: 9px;
      color: #999;
    }
    @top-right {
      content: "Semana 03 | 25 Feb 2026";
      font-size: 9px;
      color: #999;
    }
  }

  @page:first {
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: "Pagina 1/24"; font-size: 10px; color: #999; }
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
  <h2>Predicate, Method Reference,<br>Optional y Stream API</h2>
  <div class="separator"></div>
  <p class="info">Semana 03 - Martes 25 de Febrero de 2026</p>
  <p class="info">Academia Java - Ciudad de Mexico</p>

  <p class="temas-title">Temas del dia:</p>
  <ol class="temas">
    <li>Predicate: variable local dentro de lambda</li>
    <li>Predicate: variable de instancia vs variable local (shadowing)</li>
    <li>Predicate: renombrar parametro lambda para evitar conflicto</li>
    <li>Predicate: effectively final en variables locales</li>
    <li>Predicate: variables locales, de instancia y static en lambdas</li>
    <li>Method Reference <code>objeto::metodo</code> con Supplier y Consumer</li>
    <li>Method Reference <code>Clase::metodo</code> con Function y BiConsumer</li>
    <li>Method Reference <code>Clase::new</code> con Supplier, Function y BiFunction</li>
    <li>Optional: creacion con <code>empty()</code>, <code>of()</code> y <code>ofNullable()</code></li>
    <li>Optional: map, filter, orElse y tests con JUnit 5</li>
    <li>Stream API: source, intermediate y terminal</li>
    <li>Stream API: filter, map, max, peek y orElseGet</li>
  </ol>

  <p class="instructor">Instructor: Miguel Rugerio</p>
</div>

<!-- ==================== SECCION 1: PREDICATE ==================== -->
<h1 class="section">1. Predicate: variable local dentro de lambda</h1>

<p>En la sesion anterior creamos predicados con <code>java.util.function.Predicate&lt;T&gt;</code>. Hoy exploramos como interactuan las lambdas con las variables del contexto.</p>

<h2>El codigo: predicate v1</h2>

<pre><code>String lenjuage = "Phyton"; // variable local

Predicate&lt;String&gt; pre1 = pato -&gt; pato.contains("v");

res = pre1.test(lenjuage);
System.out.println(res); // false ("Phyton" no contiene "v")</code></pre>

<h2>Parametro lambda vs variable local</h2>

<pre><code>Lambda: pato -&gt; pato.contains("v")
              |
              +-- "pato" es el PARAMETRO de la lambda
                   Solo existe dentro del cuerpo de la lambda
                   NO tiene relacion con las variables externas

Variable local: lenjuage = "Phyton"
                |
                +-- Se pasa como ARGUMENTO a test()
                     La lambda lo recibe como "pato"</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> El parametro de la lambda (<code>pato</code>) es una variable nueva que solo existe dentro de la lambda. La variable local (<code>lenjuage</code>) se pasa como argumento al invocar <code>test()</code>.
</div>

<!-- ==================== SECCION 2 ==================== -->
<div class="page-break"></div>
<h1 class="section">2. Predicate: variable de instancia vs local</h1>

<h2>El codigo: predicate v2</h2>

<pre><code>public class Principal {

    String lenjuage = "Java"; // variable de INSTANCIA

    public static void main(String[] args) {

        String lenjuage = "Phyton"; // variable LOCAL (mismo nombre)

        Predicate&lt;String&gt; pre1 = pato -&gt; pato.contains("v");

        res = pre1.test(lenjuage);           // usa la LOCAL: "Phyton"
        System.out.println(res);             // false

        res = pre1.test(new Principal().lenjuage); // usa la de INSTANCIA: "Java"
        System.out.println(res);             // true ("Java" contiene "v" en "va")
    }
}</code></pre>

<h2>Dos variables con el mismo nombre</h2>

<pre><code>Clase Principal
+-- String lenjuage = "Java"        &lt;- variable de INSTANCIA (del objeto)
|
+-- main()
    +-- String lenjuage = "Phyton"  &lt;- variable LOCAL (del metodo)</code></pre>

<h2>Cual se usa en cada llamada</h2>

<pre><code>pre1.test(lenjuage)
           |
           +-- Usa la variable LOCAL "Phyton" (la mas cercana al scope)

pre1.test(new Principal().lenjuage)
                          |
                          +-- Crea un objeto y accede a su variable de INSTANCIA "Java"</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Cuando una variable local tiene el mismo nombre que una de instancia, la local tiene prioridad (<strong>shadowing</strong>). Para acceder a la de instancia desde un metodo static, necesitas crear un objeto: <code>new Principal().lenjuage</code>.
</div>

<!-- ==================== SECCION 3 ==================== -->
<div class="page-break"></div>
<h1 class="section">3. Predicate: renombrar parametro lambda</h1>

<h2>El codigo: predicate v3</h2>

<pre><code>public class Principal {

    String lenjuage = "Java"; // Instancia

    public static void main(String[] args) {

        String len = "Phyton"; // Local (nombre diferente)

        Predicate&lt;String&gt; pre1 = lenjuage -&gt; lenjuage.contains("v");

        res = pre1.test(len);
        System.out.println(res);             // false

        res = pre1.test(new Principal().lenjuage);
        System.out.println(res);             // true
    }
}</code></pre>

<h2>Que cambio respecto a v2</h2>

<pre><code>v2: String lenjuage = "Phyton";     // local con MISMO nombre que instancia
    Predicate&lt;String&gt; pre1 = pato -&gt; pato.contains("v");

v3: String len = "Phyton";          // local con nombre DIFERENTE
    Predicate&lt;String&gt; pre1 = lenjuage -&gt; lenjuage.contains("v");</code></pre>

<h2>Por que se puede usar <code>lenjuage</code> como parametro lambda?</h2>

<pre><code>En v2: la variable local "lenjuage" bloquea usar ese nombre en la lambda
En v3: la variable local se llama "len", asi que "lenjuage" queda libre
       para usarse como parametro de la lambda

El parametro lambda "lenjuage" NO es la variable de instancia.
Es un parametro nuevo que solo vive dentro de la lambda.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Un parametro de lambda no puede tener el mismo nombre que una variable local del mismo scope. Pero si la variable local se renombra, el nombre queda disponible para la lambda. El parametro lambda siempre es una variable nueva.
</div>

<!-- ==================== SECCION 4 ==================== -->
<div class="page-break"></div>
<h1 class="section">4. Effectively final: variables locales en lambdas</h1>

<h2>El codigo: predicate v4</h2>

<pre><code>public class Principal {

    static String len0 = "C++";     // Static
    String len1 = "Java";           // Instancia

    public static void main(String[] args) {

        // Effective Final
        String len2 = "Phyton";     // Local
        //len2 = "Javascript";      // Si descomentas, NO COMPILA

        Predicate&lt;String&gt; pre1 = x -&gt; x.equals(len2); // Uso local

        System.out.println(pre1.test("Java")); // false
    }
}</code></pre>

<h2>Que es effectively final</h2>

<pre><code>Una variable es "effectively final" si:
  1. Se le asigna un valor UNA sola vez
  2. Nunca se reasigna despues

String len2 = "Phyton";     // effectively final (nunca se reasigna)

String len2 = "Phyton";
len2 = "Javascript";        // YA NO es effectively final -&gt; lambda no compila</code></pre>

<h2>Regla para variables locales en lambdas</h2>

<pre><code>Variable local usada DENTRO de lambda:
  -&gt; DEBE ser effectively final (asignada una sola vez)
  -&gt; Si se reasigna -&gt; error de compilacion

Variable local usada como PARAMETRO de test():
  -&gt; NO tiene esta restriccion
  -&gt; Se puede cambiar libremente</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Las variables locales referenciadas desde dentro de una lambda deben ser <strong>effectively final</strong>: asignadas una sola vez y nunca reasignadas. Esta es una restriccion del compilador para garantizar consistencia.
</div>

<!-- ==================== SECCION 5 ==================== -->
<div class="page-break"></div>
<h1 class="section">5. Variables locales, de instancia y static en lambdas</h1>

<h2>El codigo: predicate v5</h2>

<pre><code>public class Principal {

    static String len0 = "C++";     // Static
    String len1 = "Java";           // Instancia

    public static void main(String[] args) {
        Principal prin = new Principal();
        String len2 = "Phyton";     // Local (effectively final)

        Predicate&lt;String&gt; pre1 = x -&gt; x.equals(len2); // Local
        System.out.println(pre1.test("Java")); // false

        prin.len1 = "Rust";         // Se puede reasignar

        Predicate&lt;String&gt; pre2 = x -&gt; x.equals(prin.len1); // Instancia
        System.out.println(pre2.test("Java")); // false

        len0 = "PHP";               // Se puede reasignar

        Predicate&lt;String&gt; pre3 = x -&gt; x.equals(len0); // Static
        System.out.println(pre3.test("Java")); // false
    }
}</code></pre>

<h2>Tres tipos de variable en lambdas</h2>

<table>
  <tr><th>Tipo</th><th>Reasignable</th><th>En lambda</th></tr>
  <tr><td>Local</td><td>NO</td><td>Debe ser effectively final</td></tr>
  <tr><td>De instancia</td><td>SI</td><td>Via referencia al objeto</td></tr>
  <tr><td>Static</td><td>SI</td><td>Via nombre de clase</td></tr>
</table>

<h2>Por que instancia y static SI se pueden reasignar?</h2>

<pre><code>Variable LOCAL: vive en el stack del metodo
  -&gt; La lambda captura una COPIA del valor
  -&gt; Si cambiara, la copia seria inconsistente
  -&gt; Java lo prohibe: effectively final

Variable de INSTANCIA: vive en el heap (dentro del objeto)
  -&gt; La lambda captura la referencia al objeto (prin)
  -&gt; prin es effectively final (no se reasigna)
  -&gt; Pero prin.len1 puede cambiar (es un campo del objeto)

Variable STATIC: vive en la clase (memoria compartida)
  -&gt; La lambda accede directamente via la clase
  -&gt; No se captura valor, se lee en tiempo de ejecucion</code></pre>

<div class="callout callout-principio">
  <strong>Principio:</strong> Solo las variables <strong>locales</strong> deben ser effectively final. Las variables de instancia y static pueden cambiar porque la lambda las accede por referencia (al objeto o a la clase), no por copia de valor.
</div>

<!-- ==================== SECCION 6: METHOD REFERENCES ==================== -->
<div class="page-break"></div>
<h1 class="section">6. Method Reference: objeto::metodo</h1>

<p>Segundo tema del dia: <strong>Method References</strong>. Son una forma concisa de escribir lambdas cuando la lambda solo invoca un metodo existente.</p>

<h2>El codigo: methodReferenceObjMethodInst v0 (lambda)</h2>

<pre><code>Empleado emp = new Empleado("Filologo");

Supplier&lt;String&gt; sup = () -&gt; emp.getName();
String nombre = sup.get();
System.out.println(nombre); // Filologo

Consumer&lt;String&gt; con = name -&gt; emp.setName(name);
con.accept("Aristobulo");
System.out.println(emp);   // Empleado [name=Aristobulo]</code></pre>

<h2>El codigo: methodReferenceObjMethodInst v1 (method reference)</h2>

<pre><code>Empleado emp = new Empleado("Patrobas");

Supplier&lt;String&gt; sup = emp::getName;       // object::method
String nombre = sup.get();
System.out.println(nombre); // Patrobas

Consumer&lt;String&gt; con = emp::setName;       // object::method
con.accept("Aristobulo");
System.out.println(emp);   // Empleado [name=Aristobulo]</code></pre>

<h2>Lambda vs Method Reference</h2>

<pre><code>Lambda:                          Method Reference:
() -&gt; emp.getName()       -&gt;      emp::getName
name -&gt; emp.setName(name) -&gt;      emp::setName

Regla: si la lambda SOLO invoca un metodo, se puede reemplazar
por una referencia al metodo.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>object::method</code> es equivalente a una lambda que invoca ese metodo en ese objeto. Es mas conciso y legible. Se usa con Supplier (sin parametros) y Consumer (con un parametro).
</div>

<!-- ==================== SECCION 7 ==================== -->
<div class="page-break"></div>
<h1 class="section">7. Method Reference: Clase::metodo</h1>

<h2>El codigo: methodReferenceClassMethodInst v0 (lambda)</h2>

<pre><code>Empleado emp = new Empleado("Filologo");

Function&lt;Empleado,String&gt; sup = (employee) -&gt; employee.getName();
String nombre = sup.apply(emp);
System.out.println(nombre); // Filologo

BiConsumer&lt;Empleado,String&gt; con = (employee,name) -&gt; employee.setName(name);
con.accept(emp,"Aristobulo");
System.out.println(emp);   // Empleado [name=Aristobulo]</code></pre>

<h2>El codigo: methodReferenceClassMethodInst v1 (method reference)</h2>

<pre><code>Empleado emp = new Empleado("Filologo");

Function&lt;Empleado,String&gt; sup = Empleado::getName;
String nombre = sup.apply(emp);
System.out.println(nombre); // Filologo

BiConsumer&lt;Empleado,String&gt; con = Empleado::setName;
con.accept(emp,"Aristobulo");
System.out.println(emp);   // Empleado [name=Aristobulo]</code></pre>

<h2>Diferencia: object::method vs Class::method</h2>

<pre><code>object::method (seccion anterior):
  emp::getName              -&gt; Supplier&lt;String&gt;
  "Ya conozco el objeto, solo dame el resultado"

Class::method (esta seccion):
  Empleado::getName         -&gt; Function&lt;Empleado,String&gt;
  "No conozco el objeto, pasamelo como primer parametro"</code></pre>

<h2>Comparacion de interfaces funcionales</h2>

<table>
  <tr><th>Operacion</th><th>object::method</th><th>Class::method</th></tr>
  <tr><td>Getter (getName)</td><td><code>Supplier&lt;String&gt;</code></td><td><code>Function&lt;Empleado,String&gt;</code></td></tr>
  <tr><td>Setter (setName)</td><td><code>Consumer&lt;String&gt;</code></td><td><code>BiConsumer&lt;Empleado,String&gt;</code></td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>Class::method</code> referencia un metodo de instancia a traves de la clase. El objeto se pasa como primer argumento. Esto agrega un parametro extra a la interfaz funcional (Supplier&rarr;Function, Consumer&rarr;BiConsumer).
</div>

<!-- ==================== SECCION 8 ==================== -->
<div class="page-break"></div>
<h1 class="section">8. Method Reference: Clase::new</h1>

<h2>Evolucion progresiva: methodReferenceNew v0 a v3</h2>

<h3>v0: Supplier con lambda (constructor sin parametros)</h3>

<pre><code>Supplier&lt;Empleado&gt; sup = () -&gt; new Empleado();
Empleado emp1 = sup.get();</code></pre>

<h3>v1: Function con lambda (constructor con 1 parametro)</h3>

<pre><code>Function&lt;String,Empleado&gt; fun = n -&gt; new Empleado(n);
Empleado emp2 = fun.apply("Patrobas");</code></pre>

<h3>v2: BiFunction con lambda (constructor con 2 parametros)</h3>

<pre><code>BiFunction&lt;String,Integer,Empleado&gt; bifun = (t,v) -&gt; new Empleado(t,v);
Empleado emp3 = bifun.apply("Epeneto", 10);</code></pre>

<h3>v3: Todas con Method Reference (::new)</h3>

<pre><code>Supplier&lt;Empleado&gt; sup = Empleado::new;
Empleado emp1 = sup.get();

Function&lt;String,Empleado&gt; fun = Empleado::new;
Empleado emp2 = fun.apply("Patrobas");

BiFunction&lt;String,Integer,Empleado&gt; bifun = Empleado::new;
Empleado emp3 = bifun.apply("Epeneto", 10);</code></pre>

<h2>Como Java sabe cual constructor usar</h2>

<pre><code>Empleado::new  se escribe IGUAL para los tres, pero:

Supplier&lt;Empleado&gt;                    -&gt; Java elige Empleado()
Function&lt;String,Empleado&gt;             -&gt; Java elige Empleado(String)
BiFunction&lt;String,Integer,Empleado&gt;   -&gt; Java elige Empleado(String,int)

El compilador infiere el constructor por el tipo de la interfaz funcional.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>Class::new</code> referencia un constructor. Java resuelve cual constructor usar basandose en la interfaz funcional asignada. La misma sintaxis <code>Empleado::new</code> puede invocar constructores diferentes.
</div>

<!-- ==================== SECCION 9 ==================== -->
<div class="page-break"></div>
<h1 class="section">9. Resumen: los 4 tipos de Method Reference</h1>

<p>Java tiene 4 formas de method reference:</p>

<table>
  <tr><th>Tipo</th><th>Sintaxis</th><th>Ejemplo</th><th>Lambda equivalente</th></tr>
  <tr><td>Metodo estatico</td><td><code>Class::staticMethod</code></td><td><code>Math::abs</code></td><td><code>x -&gt; Math.abs(x)</code></td></tr>
  <tr><td>Metodo de objeto</td><td><code>object::method</code></td><td><code>emp::getName</code></td><td><code>() -&gt; emp.getName()</code></td></tr>
  <tr><td>Metodo de clase</td><td><code>Class::method</code></td><td><code>Empleado::getName</code></td><td><code>e -&gt; e.getName()</code></td></tr>
  <tr><td>Constructor</td><td><code>Class::new</code></td><td><code>Empleado::new</code></td><td><code>() -&gt; new Empleado()</code></td></tr>
</table>

<h2>Cuando usar cada uno</h2>

<pre><code>Lambda solo invoca un metodo estatico?                -&gt; Class::staticMethod
Lambda solo invoca un metodo en un objeto conocido?   -&gt; object::method
Lambda recibe un objeto y llama un metodo en el?      -&gt; Class::method
Lambda solo crea un objeto nuevo?                     -&gt; Class::new</code></pre>

<h2>Regla general</h2>

<pre><code>Si tu lambda SOLO hace UNA cosa (invocar un metodo o crear un objeto),
puedes reemplazarla por un method reference.

Si tu lambda tiene logica adicional (calculos, condiciones, etc.),
NO puedes usar method reference. Usa lambda.</code></pre>

<div class="callout callout-principio">
  <strong>Principio:</strong> Los method references son azucar sintactica para lambdas simples. Hacen el codigo mas conciso y legible. Java infiere los tipos automaticamente basandose en la interfaz funcional.
</div>

<!-- ==================== SECCION 10: OPTIONAL ==================== -->
<div class="page-break"></div>
<h1 class="section">10. Optional: creacion y verificacion basica</h1>

<p>Tercer tema: <strong>Optional</strong>, una clase contenedora que puede o no tener un valor. Evita NullPointerException.</p>

<h2>El codigo: optional v0 Principal</h2>

<pre><code>Optional&lt;String&gt; empty = Optional.empty();
System.out.println(empty);            // Optional.empty
boolean res = empty.isPresent();
System.out.println(res);              // false

String name = "baeldung";
Optional&lt;String&gt; opt = Optional.of(name);
res = opt.isPresent();
System.out.println(res);              // true

name = null;
//Optional.of(name);                  // NullPointerException!
opt = Optional.ofNullable(name);
res = opt.isPresent();
System.out.println(res);              // false

opt = Optional.of("baeldung");
opt.ifPresent(nombre -&gt; System.out.println(nombre.length())); // 8</code></pre>

<h2>Tres formas de crear un Optional</h2>

<pre><code>Optional.empty()           -&gt; Optional vacio (sin valor)
Optional.of(valor)         -&gt; Optional con valor (NO acepta null -&gt; NPE)
Optional.ofNullable(valor) -&gt; Optional con valor o vacio si es null</code></pre>

<h2>Diagrama de decision</h2>

<pre><code>El valor puede ser null?
  +-- SI  -&gt; Optional.ofNullable(valor)
  +-- NO  -&gt; Optional.of(valor)
  +-- Sin valor -&gt; Optional.empty()</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>Optional.of()</code> lanza NullPointerException si recibe null. Usa <code>Optional.ofNullable()</code> cuando el valor pueda ser null. <code>ifPresent()</code> ejecuta una lambda solo si el Optional tiene valor.
</div>

<!-- ==================== SECCION 11 ==================== -->
<div class="page-break"></div>
<h1 class="section">11. Optional: tests con JUnit 5</h1>

<h2>El codigo: optional v0 TestOptional</h2>

<pre><code>@Test
public void whenCreatesEmptyOptional_thenCorrect() {
    Optional&lt;String&gt; empty = Optional.empty();
    assertFalse(empty.isPresent());
}

@Test
public void givenNonNull_whenCreatesNonNullable_thenCorrect() {
    String name = "baeldung";
    Optional&lt;String&gt; opt = Optional.of(name);
    assertTrue(opt.isPresent());
}

@Test
void givenNull_whenThrowsErrorOnCreate_thenCorrect() {
    String name = null;
    assertThrows(NullPointerException.class,
            () -&gt; Optional.of(name));
}

@Test
public void givenNull_whenCreatesNullable_thenCorrect() {
    String name = null;
    Optional&lt;String&gt; opt = Optional.ofNullable(name);
    assertFalse(opt.isPresent());
}</code></pre>

<h2>Que valida cada test</h2>

<pre><code>1. empty()           -&gt; isPresent() retorna false
2. of("baeldung")    -&gt; isPresent() retorna true
3. of(null)          -&gt; lanza NullPointerException
4. ofNullable(null)  -&gt; isPresent() retorna false</code></pre>

<h2>assertThrows: verificar excepciones</h2>

<pre><code>assertThrows(NullPointerException.class, () -&gt; Optional.of(name));
              |                            |
              |                            +-- lambda que debe lanzar la excepcion
              +-- tipo de excepcion esperada

Si la lambda NO lanza NPE, el test FALLA.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Los tests con JUnit 5 verifican el comportamiento de Optional: <code>assertFalse</code>, <code>assertTrue</code> para estados, y <code>assertThrows</code> para verificar que <code>Optional.of(null)</code> lanza NullPointerException.
</div>

<!-- ==================== SECCION 12 ==================== -->
<div class="page-break"></div>
<h1 class="section">12. Optional: map y orElse con listas</h1>

<h2>El codigo: optional v1 Principal</h2>

<pre><code>List&lt;String&gt; companyNames = Arrays.asList(
        "paypal", "oracle", "", "microsoft", "", "apple");

companyNames = null; // simular lista nula

Optional&lt;List&lt;String&gt;&gt; listOptional =
        Optional.ofNullable(companyNames);

int tamanio = listOptional
    .map(l -&gt; l.size())  // Function&lt;T,U&gt;
    .orElse(0);

System.out.println("Size: " + tamanio); // Size: 0</code></pre>

<h2>Flujo de ejecucion con lista null</h2>

<pre><code>companyNames = null
    |
Optional.ofNullable(null)  -&gt;  Optional.empty
    |
.map(l -&gt; l.size())       -&gt;  Optional.empty (map no ejecuta la lambda)
    |
.orElse(0)                 -&gt;  0 (retorna el valor por defecto)</code></pre>

<h2>Flujo de ejecucion con lista valida</h2>

<pre><code>companyNames = ["paypal", "oracle", "", "microsoft", "", "apple"]
    |
Optional.ofNullable(lista)  -&gt;  Optional[lista]
    |
.map(l -&gt; l.size())        -&gt;  Optional[6]
    |
.orElse(0)                  -&gt;  6 (retorna el valor real)</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>map()</code> transforma el contenido del Optional sin riesgo de NPE. Si el Optional esta vacio, <code>map()</code> simplemente retorna otro Optional vacio. <code>orElse()</code> proporciona un valor por defecto seguro.
</div>

<!-- ==================== SECCION 13 ==================== -->
<div class="page-break"></div>
<h1 class="section">13. Optional: filter, isEmpty vs isBlank</h1>

<h2>El codigo: optional v1 Principal2</h2>

<pre><code>List&lt;String&gt; companyNames = Arrays.asList(
        "paypal", "oracle", "", "microsoft", "", "apple");

Optional&lt;List&lt;String&gt;&gt; listOptional = Optional.of(companyNames);

listOptional = listOptional.filter(lista -&gt; !lista.isEmpty());
List&lt;String&gt; newList = listOptional.get();
System.out.println(newList);</code></pre>

<h2>filter() en Optional</h2>

<pre><code>filter(Predicate) -&gt; si el valor cumple la condicion, lo conserva
                     si NO cumple, retorna Optional.empty

listOptional.filter(lista -&gt; !lista.isEmpty())
                     |              |
                     |              +-- la lista NO esta vacia?
                     +-- el contenido del Optional (la lista)

La lista tiene 6 elementos -&gt; no esta vacia -&gt; filter la conserva</code></pre>

<h2>isEmpty() vs isBlank() en String</h2>

<table>
  <tr><th>Metodo</th><th><code>""</code> (vacio)</th><th><code>" "</code> (espacio)</th><th>Descripcion</th></tr>
  <tr><td><code>isEmpty()</code></td><td>true</td><td>false</td><td>true si length() == 0</td></tr>
  <tr><td><code>isBlank()</code></td><td>true</td><td>true</td><td>true si solo tiene espacios (Java 11)</td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>filter()</code> en Optional conserva el valor si cumple la condicion, o lo vacia si no. <code>isEmpty()</code> verifica longitud cero, <code>isBlank()</code> (Java 11) tambien detecta strings con solo espacios.
</div>

<!-- ==================== SECCION 14 ==================== -->
<div class="page-break"></div>
<h1 class="section">14. Optional con removeIf en listas</h1>

<h2>El codigo: optional v1 Principal3</h2>

<pre><code>List&lt;String&gt; companyNames = Arrays.asList(
        "paypal", "oracle", "", "microsoft", "", "apple");

companyNames = new ArrayList&lt;&gt;(companyNames); // lista mutable

companyNames.removeIf(n -&gt; n.isEmpty());      // elimina strings vacios

Optional&lt;List&lt;String&gt;&gt; listOptional =
        Optional.ofNullable(companyNames);

List&lt;String&gt; companyNamesOther = listOptional.get();
System.out.println(companyNamesOther);
// [paypal, oracle, microsoft, apple]</code></pre>

<h2>Por que <code>new ArrayList&lt;&gt;(companyNames)</code>?</h2>

<pre><code>Arrays.asList() -&gt; lista de tamanio FIJO (no soporta removeIf)
new ArrayList&lt;&gt;(lista) -&gt; copia en lista MUTABLE (soporta removeIf)</code></pre>

<h2>Flujo completo</h2>

<pre><code>Original:  ["paypal", "oracle", "", "microsoft", "", "apple"]
                                 ^                  ^
                              vacios a eliminar
    |
removeIf(n -&gt; n.isEmpty())
    |
Resultado: ["paypal", "oracle", "microsoft", "apple"]
    |
Optional.ofNullable(lista) -&gt; Optional[lista con 4 elementos]
    |
listOptional.get() -&gt; retorna la lista directamente</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Combinar <code>removeIf()</code> con <code>Optional.ofNullable()</code> permite limpiar la lista y proteger contra nulls. Recuerda convertir <code>Arrays.asList()</code> a <code>new ArrayList&lt;&gt;()</code> para poder modificar la lista.
</div>

<!-- ==================== SECCION 15: STREAM ==================== -->
<div class="page-break"></div>
<h1 class="section">15. Stream API: conceptos fundamentales</h1>

<p>Cuarto tema: <strong>Stream API</strong>. Un Stream es una secuencia de elementos que soporta operaciones funcionales para procesar datos.</p>

<h2>Anatomia de un Stream pipeline</h2>

<pre><code>Stream Source        Intermediate          Terminal
(origen)             (transformacion)      (resultado)
    |                     |                    |
lista.stream()    -&gt;   .filter()       -&gt;   .collect()
                       .map()               .max()
                       .peek()              .forEach()</code></pre>

<h2>Reglas del Stream</h2>

<pre><code>1. Un Stream NO almacena datos (es un flujo, no una coleccion)
2. Un Stream NO modifica la fuente original
3. Las operaciones intermedias son LAZY (no se ejecutan hasta el terminal)
4. Un Stream solo se puede usar UNA VEZ
5. Un Stream se consume al ejecutar la operacion terminal</code></pre>

<h2>El codigo: Stream v0 Principal (pipeline separado)</h2>

<pre><code>List&lt;String&gt; companyNames = Arrays.asList(
        "paypal", "oracle", "", "microsoft", "", "apple");

// Stream Source
Stream&lt;String&gt; stream1 = companyNames.stream();

// Intermediate
Stream&lt;String&gt; stream2 = stream1.filter(name -&gt; !name.isBlank());

// Terminal
List&lt;String&gt; listNames = stream2.collect(Collectors.toList());

System.out.println(listNames); // [paypal, oracle, microsoft, apple]</code></pre>

<div class="callout callout-principio">
  <strong>Principio:</strong> Un Stream pipeline tiene 3 fases: <strong>source</strong> (origen de datos), <strong>intermediate</strong> (transformaciones lazy) y <strong>terminal</strong> (ejecuta todo y produce resultado). Las fases intermediate son opcionales, pero el terminal es obligatorio.
</div>

<!-- ==================== SECCION 16 ==================== -->
<div class="page-break"></div>
<h1 class="section">16. Stream: encadenamiento fluido</h1>

<h2>El codigo: Stream v0 Principal1</h2>

<pre><code>List&lt;String&gt; listNames = companyNames.stream()
        .filter(name -&gt; !name.isBlank()) // Predicate
        .collect(Collectors.toList());

System.out.println(listNames); // [paypal, oracle, microsoft, apple]</code></pre>

<h2>Diferencia con v0: encadenamiento</h2>

<pre><code>v0 (separado):                    v1 (encadenado):
Stream&lt;String&gt; s1 = ...stream()   companyNames.stream()
Stream&lt;String&gt; s2 = s1.filter()       .filter(...)
List&lt;String&gt; r = s2.collect()         .collect(...)

El resultado es IDENTICO. La forma encadenada es mas idiomatica en Java.</code></pre>

<h2>filter() con Predicate</h2>

<pre><code>.filter(name -&gt; !name.isBlank())
         |              |
         |              +-- condicion: NO esta en blanco
         +-- cada elemento del stream

Recibe: Predicate&lt;String&gt;  (funcion que retorna boolean)
Mantiene: los elementos que retornan TRUE
Elimina:  los elementos que retornan FALSE

"paypal"    -&gt; !isBlank() -&gt; true  -&gt; se mantiene
""          -&gt; !isBlank() -&gt; false -&gt; se elimina
"oracle"    -&gt; !isBlank() -&gt; true  -&gt; se mantiene</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> El encadenamiento fluido (<code>stream().filter().collect()</code>) es la forma idiomatica de usar Streams. Cada operacion retorna un nuevo Stream, permitiendo encadenar sin variables intermedias.
</div>

<!-- ==================== SECCION 17 ==================== -->
<div class="page-break"></div>
<h1 class="section">17. Stream: map() para transformar</h1>

<h2>El codigo: Stream v0 Principal2</h2>

<pre><code>List&lt;Integer&gt; listNames = companyNames.stream()
        .filter(name -&gt; !name.isBlank()) // Predicate
        .map(String::length)             // Function
        .collect(Collectors.toList());

System.out.println(listNames); // [6, 6, 9, 5]</code></pre>

<h2>Que hace map()</h2>

<pre><code>.map(String::length)     equivale a     .map(x -&gt; x.length())

Transforma cada elemento:
  "paypal"    -&gt; 6
  "oracle"    -&gt; 6
  "microsoft" -&gt; 9
  "apple"     -&gt; 5

Recibe: Function&lt;String,Integer&gt;
Entrada: Stream&lt;String&gt;
Salida:  Stream&lt;Integer&gt;</code></pre>

<h2>Pipeline completo</h2>

<pre><code>Source:         ["paypal", "oracle", "", "microsoft", "", "apple"]
    |
filter(!isBlank): ["paypal", "oracle", "microsoft", "apple"]
    |
map(length):    [6, 6, 9, 5]
    |
collect:        List&lt;Integer&gt; -&gt; [6, 6, 9, 5]</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>map()</code> transforma cada elemento del Stream usando una Function. Puede cambiar el tipo del Stream (ej: <code>Stream&lt;String&gt;</code> a <code>Stream&lt;Integer&gt;</code>). <code>String::length</code> es un method reference equivalente a <code>x -&gt; x.length()</code>.
</div>

<!-- ==================== SECCION 18 ==================== -->
<div class="page-break"></div>
<h1 class="section">18. Stream: max() con Optional</h1>

<h2>El codigo: Stream v0 Principal3</h2>

<pre><code>Optional&lt;Integer&gt; valorMaximo = companyNames.stream()
        .filter(name -&gt; !name.isBlank()) // Predicate
        .map(String::length)             // Function
        .max((t,u) -&gt; t-u);             // Comparator

System.out.println(valorMaximo); // Optional[9]

int max = valorMaximo.get();
System.out.println(max);        // 9</code></pre>

<h2>Por que max() retorna Optional?</h2>

<pre><code>max() podria recibir un Stream VACIO.
Si no hay elementos, no hay maximo.
Optional maneja esa posibilidad:

Stream con datos -&gt; Optional[9]       -&gt; .get() retorna 9
Stream vacio     -&gt; Optional.empty    -&gt; .get() lanza NoSuchElementException</code></pre>

<h2>El Comparator</h2>

<pre><code>.max((t,u) -&gt; t-u)
       |  |     |
       |  |     +-- resta para comparar
       |  +-- segundo elemento
       +-- primer elemento

t - u &gt; 0  -&gt; t es mayor
t - u &lt; 0  -&gt; u es mayor
t - u == 0 -&gt; son iguales</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>max()</code> retorna <code>Optional</code> porque el Stream podria estar vacio. Se necesita un <code>Comparator</code> para definir el criterio de comparacion. Usa <code>.get()</code> solo si estas seguro de que tiene valor.
</div>

<!-- ==================== SECCION 19 ==================== -->
<div class="page-break"></div>
<h1 class="section">19. Stream: orElseGet() para streams vacios</h1>

<h2>El codigo: Stream v0 Principal4</h2>

<pre><code>companyNames = new ArrayList&lt;&gt;(); // lista VACIA

int max = companyNames.stream()
        .filter(name -&gt; !name.isBlank()) // Predicate
        .map(String::length)             // Function
        .max((t,u) -&gt; t-u)              // Comparator -&gt; Optional&lt;Integer&gt;
        .orElseGet(() -&gt; 0);            // Supplier

System.out.println(max); // 0</code></pre>

<h2>Flujo con lista vacia</h2>

<pre><code>Source:         []  (lista vacia)
    |
filter:         []  (nada que filtrar)
    |
map:            []  (nada que mapear)
    |
max:            Optional.empty  (no hay maximo)
    |
orElseGet(-&gt;0):  0  (valor por defecto del Supplier)</code></pre>

<h2>orElse vs orElseGet</h2>

<pre><code>.orElse(0)           -&gt; valor por defecto directo
.orElseGet(() -&gt; 0)  -&gt; Supplier que genera el valor por defecto

orElse:    el valor se evalua SIEMPRE (incluso si Optional tiene dato)
orElseGet: el Supplier se ejecuta SOLO si Optional esta vacio (lazy)</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>orElseGet(Supplier)</code> proporciona un valor por defecto de forma lazy: el Supplier solo se ejecuta si el Optional esta vacio. Es preferible a <code>orElse()</code> cuando el valor por defecto es costoso de calcular.
</div>

<!-- ==================== SECCION 20 ==================== -->
<div class="page-break"></div>
<h1 class="section">20. Stream: peek() y Comparator.naturalOrder()</h1>

<h2>El codigo: Stream v0 Principal5</h2>

<pre><code>int max = companyNames.stream()
        .filter(name -&gt; !name.isBlank()) // Predicate
        .map(String::length)             // Function
        .peek(System.out::println)       // Consumer (debug)
        .max(Comparator.naturalOrder())  // Comparator
        .orElseGet(() -&gt; 0);            // Supplier

System.out.println("Valor Maximo: " + max);</code></pre>

<h2>Salida del programa</h2>

<pre><code>6          &lt;- peek imprime cada longitud
6
9
5
Valor Maximo: 9</code></pre>

<h2>peek(): operacion intermedia para debug</h2>

<pre><code>.peek(System.out::println)
       |
       +-- Consumer&lt;Integer&gt;: imprime cada elemento sin modificarlo

peek() NO modifica el stream, solo observa los elementos.
Es util para debugging: ver que elementos pasan por el pipeline.</code></pre>

<h2>Comparator.naturalOrder()</h2>

<pre><code>.max((t,u) -&gt; t-u)              &lt;- lambda manual
.max(Comparator.naturalOrder()) &lt;- metodo built-in

Ambos ordenan numericamente de menor a mayor.
naturalOrder() es mas legible y funciona con cualquier Comparable.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>peek()</code> es una operacion intermedia que ejecuta una accion (Consumer) por cada elemento sin modificar el stream. Ideal para debug. <code>Comparator.naturalOrder()</code> es la alternativa limpia a escribir un comparador manual.
</div>

<!-- ==================== RESUMEN ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Resumen de conceptos clave</h1>

<table>
  <tr><th>Concepto</th><th>Descripcion</th></tr>
  <tr><td>Variable local en lambda</td><td>Debe ser <strong>effectively final</strong> (asignada una sola vez)</td></tr>
  <tr><td>Variable de instancia en lambda</td><td>Puede cambiar (se accede via referencia al objeto)</td></tr>
  <tr><td>Variable static en lambda</td><td>Puede cambiar (se accede via la clase)</td></tr>
  <tr><td>Shadowing</td><td>Variable local oculta la de instancia con el mismo nombre</td></tr>
  <tr><td><code>object::method</code></td><td>Method reference a metodo de instancia via objeto conocido</td></tr>
  <tr><td><code>Class::method</code></td><td>Method reference a metodo de instancia via la clase</td></tr>
  <tr><td><code>Class::new</code></td><td>Method reference a constructor (Java elige por interfaz funcional)</td></tr>
  <tr><td><code>Optional.empty()</code></td><td>Crea Optional sin valor</td></tr>
  <tr><td><code>Optional.of(v)</code></td><td>Crea Optional con valor (NPE si null)</td></tr>
  <tr><td><code>Optional.ofNullable(v)</code></td><td>Crea Optional con valor o vacio si null</td></tr>
  <tr><td><code>map(Function)</code></td><td>Transforma el valor dentro del Optional o Stream</td></tr>
  <tr><td><code>filter(Predicate)</code></td><td>Conserva si cumple condicion, vacia si no</td></tr>
  <tr><td><code>orElse</code> / <code>orElseGet</code></td><td>Valor por defecto si Optional esta vacio</td></tr>
  <tr><td>Stream pipeline</td><td>Source &rarr; Intermediate (lazy) &rarr; Terminal</td></tr>
  <tr><td><code>stream().filter()</code></td><td>Filtra elementos con Predicate</td></tr>
  <tr><td><code>stream().map()</code></td><td>Transforma elementos con Function</td></tr>
  <tr><td><code>stream().peek()</code></td><td>Observa elementos sin modificar (debug)</td></tr>
  <tr><td><code>stream().max()</code></td><td>Obtiene el maximo (retorna Optional)</td></tr>
  <tr><td><code>Collectors.toList()</code></td><td>Terminal que recolecta en una List</td></tr>
</table>

<!-- ==================== PROGRESION ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Progresion de los ejercicios del dia</h1>

<table>
  <tr><th>Proyecto</th><th>Paquete</th><th>Version</th><th>Tema</th></tr>
  <tr><td>predicate</td><td><code>com.curso</code></td><td>v1</td><td>Variable local en Predicate</td></tr>
  <tr><td>predicate</td><td><code>com.curso</code></td><td>v2</td><td>Variable de instancia vs local (shadowing)</td></tr>
  <tr><td>predicate</td><td><code>com.curso</code></td><td>v3</td><td>Renombrar parametro lambda</td></tr>
  <tr><td>predicate</td><td><code>com.curso</code></td><td>v4</td><td>Effectively final en variables locales</td></tr>
  <tr><td>predicate</td><td><code>com.curso</code></td><td>v5</td><td>Variables locales, de instancia y static</td></tr>
  <tr><td>methodReferenceObjMethodInst</td><td><code>com.curso</code></td><td>v0</td><td>Lambda: Supplier y Consumer con objeto</td></tr>
  <tr><td>methodReferenceObjMethodInst</td><td><code>com.curso</code></td><td>v1</td><td>Method reference: <code>emp::getName</code></td></tr>
  <tr><td>methodReferenceClassMethodInst</td><td><code>com.curso</code></td><td>v0</td><td>Lambda: Function y BiConsumer con clase</td></tr>
  <tr><td>methodReferenceClassMethodInst</td><td><code>com.curso</code></td><td>v1</td><td>Method reference: <code>Empleado::getName</code></td></tr>
  <tr><td>methodReferenceNew</td><td><code>com.curso</code></td><td>v0</td><td>Lambda: Supplier con constructor vacio</td></tr>
  <tr><td>methodReferenceNew</td><td><code>com.curso</code></td><td>v1</td><td>Lambda: Function con constructor 1 param</td></tr>
  <tr><td>methodReferenceNew</td><td><code>com.curso</code></td><td>v2</td><td>Lambda: BiFunction con constructor 2 params</td></tr>
  <tr><td>methodReferenceNew</td><td><code>com.curso</code></td><td>v3</td><td>Method reference: <code>Empleado::new</code></td></tr>
  <tr><td>optional</td><td><code>com.curso</code></td><td>v0</td><td>Optional: empty, of, ofNullable, ifPresent</td></tr>
  <tr><td>optional</td><td><code>com.curso</code></td><td>v0</td><td>TestOptional: tests JUnit 5</td></tr>
  <tr><td>optional</td><td><code>com.curso</code></td><td>v1</td><td>Optional con map y orElse en listas</td></tr>
  <tr><td>optional</td><td><code>com.curso</code></td><td>v1</td><td>Optional con filter, isEmpty vs isBlank</td></tr>
  <tr><td>optional</td><td><code>com.curso</code></td><td>v1</td><td>Optional con removeIf en listas mutables</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v0</td><td>Stream pipeline separado</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v0</td><td>Stream encadenado: filter + collect</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v0</td><td>Stream con map: String a Integer</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v0</td><td>Stream con max y Optional</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v0</td><td>Stream con orElseGet: streams vacios</td></tr>
  <tr><td>Stream</td><td><code>com.curso</code></td><td>v0</td><td>Stream con peek y naturalOrder()</td></tr>
</table>

</body>
</html>
"""

if __name__ == "__main__":
    html = weasyprint.HTML(string=HTML_CONTENT)
    html.write_pdf("250226.pdf")
    print("PDF generado: 250226.pdf")
