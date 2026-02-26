#!/usr/bin/env python3
"""
Genera el PDF de la Guia de Repaso del 24 de febrero de 2026.
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
      content: "Curso de Java - Wildcards y Collections";
      font-size: 9px;
      color: #999;
    }
    @top-right {
      content: "Semana 03 | 24 Feb 2026";
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
  <h2>Wildcards Super, Collections<br>y Predicate</h2>
  <div class="separator"></div>
  <p class="info">Semana 03 - Martes 24 de Febrero de 2026</p>
  <p class="info">Academia Java - Ciudad de Mexico</p>

  <p class="temas-title">Temas del dia:</p>
  <ol class="temas">
    <li>Lower Bounded Wildcard <code>List&lt;? super Animal&gt;</code>: lectura</li>
    <li>Lower Bounded Wildcard <code>List&lt;? super Animal&gt;</code>: escritura</li>
    <li>Regla PECS: Producer Extends, Consumer Super</li>
    <li>Collection Framework: <code>Collection&lt;T&gt;</code> con removeIf y forEach</li>
    <li>List: <code>Arrays.asList()</code>, replaceAll y sort con Comparator</li>
    <li><code>@FunctionalInterface</code>: interfaz con metodo abstracto unico</li>
    <li>Metodos static y default en interfaces funcionales</li>
    <li>Composicion de predicados: metodo static generico <code>and()</code></li>
    <li>Lambdas inline y simplificacion progresiva</li>
    <li><code>java.util.function.Predicate&lt;T&gt;</code>: la interfaz built-in de Java</li>
  </ol>

  <p class="instructor">Instructor: Miguel Rugerio</p>
</div>

<!-- ==================== SECCION 1 ==================== -->
<h1 class="section">1. Repaso: Wildcards en generics</h1>

<p>En la sesion anterior vimos tres formas de tipar un parametro de lista:</p>

<table>
  <tr><th>Forma</th><th>Acepta</th><th>Puede leer como</th><th>Puede escribir</th></tr>
  <tr><td><code>List&lt;Animal&gt;</code></td><td>Solo <code>List&lt;Animal&gt;</code></td><td><code>Animal</code></td><td>Si</td></tr>
  <tr><td><code>List&lt;?&gt;</code></td><td>Cualquier <code>List&lt;X&gt;</code></td><td><code>Object</code></td><td>No</td></tr>
  <tr><td><code>List&lt;? extends Animal&gt;</code></td><td><code>List&lt;Animal&gt;</code>, <code>List&lt;Pato&gt;</code>, <code>List&lt;Perico&gt;</code></td><td><code>Animal</code></td><td>No</td></tr>
  <tr><td><code>List&lt;? super Animal&gt;</code></td><td><code>List&lt;Animal&gt;</code>, <code>List&lt;Object&gt;</code></td><td><code>Object</code></td><td>Si (subtipos de Animal)</td></tr>
</table>

<p>Hoy nos enfocamos en la ultima fila: <strong>Lower Bounded Wildcard</strong> con <code>super</code>.</p>

<!-- ==================== SECCION 2 ==================== -->
<div class="page-break"></div>
<h1 class="section">2. Lower Bounded Wildcard: <code>List&lt;? super Animal&gt;</code></h1>

<h2>Que significa <code>? super Animal</code></h2>

<pre><code>List&lt;? super Animal&gt;
          |     |
          |     +-- limite inferior: Animal
          +-- "?" = tipo desconocido, pero DEBE ser Animal o superclase de Animal

Acepta: List&lt;Animal&gt;, List&lt;Object&gt;
NO acepta: List&lt;Pato&gt;, List&lt;Perico&gt;</code></pre>

<h2>Por que NO acepta <code>List&lt;Pato&gt;</code>?</h2>

<pre><code>Pato es SUBTIPO de Animal (Pato extends Animal)
super pide SUPERTIPO de Animal
Pato NO es supertipo de Animal -&gt; NO compila</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>? super Animal</code> va "hacia arriba" en la jerarquia de herencia. Solo acepta Animal y sus superclases (en este caso, Object).
</div>

<!-- ==================== SECCION 3 ==================== -->
<div class="page-break"></div>
<h1 class="section">3. <code>? super</code> en lectura</h1>

<h2>El codigo: v8</h2>

<pre><code>static void showAnimal(List&lt;? super Animal&gt; listaAnimal) {

    for (Object ani : listaAnimal) {

        System.out.println(ani.getClass().getSimpleName());
        if (ani instanceof Perico)
            ((Perico)ani).volarPerico();
        if (ani instanceof Pato p) //Pattern Matching Java 14
            p.volarPato();
        if (ani instanceof Animal)
            ((Animal)ani).volar();
    }
}</code></pre>

<h2>Que listas acepta este metodo</h2>

<pre><code>List&lt;Animal&gt; listaAnimal = new ArrayList&lt;&gt;();
listaAnimal.add(new Perico());
listaAnimal.add(new Pato());
listaAnimal.add(new Animal());
showAnimal(listaAnimal);     // Animal ES Animal

List&lt;Object&gt; listaObject = new ArrayList&lt;&gt;();
listaObject.add(new Object());
listaObject.add(new Perico());
listaObject.add(Integer.valueOf(1000));
listaObject.add("Patrobas");
showAnimal(listaObject);     // Object ES superclase de Animal

List&lt;Pato&gt; listaPato = new ArrayList&lt;&gt;();
//showAnimal(listaPato);     // NO COMPILA: Pato NO es superclase de Animal</code></pre>

<h2>Por que se itera como <code>Object</code>?</h2>

<pre><code>List&lt;? super Animal&gt; podria ser:
  - List&lt;Animal&gt;  -&gt; elementos son Animal
  - List&lt;Object&gt;  -&gt; elementos son Object

El tipo comun mas seguro es Object.
Por eso el for usa: for (Object ani : ...)</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Con <code>? super</code>, la lectura siempre es como <code>Object</code>. Si necesitas usar metodos especificos, debes hacer instanceof + cast (o Pattern Matching).
</div>

<!-- ==================== SECCION 4 ==================== -->
<div class="page-break"></div>
<h1 class="section">4. <code>? super</code> en escritura</h1>

<h2>La diferencia clave: <code>super</code> permite agregar elementos</h2>

<pre><code>static void showAnimal(List&lt;? super Animal&gt; listaAnimal) {

    //listaAnimal.add(new Object()); // NO COMPILA
    listaAnimal.add(new Perico());   // SI compila

    for (Object ani : listaAnimal) {
        System.out.println(ani.getClass().getSimpleName());
        if (ani instanceof Perico)
            ((Perico)ani).volarPerico();
        if (ani instanceof Pato p)
            p.volarPato();
        if (ani instanceof Animal)
            ((Animal)ani).volar();
    }
}</code></pre>

<h2>Que se puede agregar a <code>List&lt;? super Animal&gt;</code>?</h2>

<pre><code>listaAnimal.add(new Animal());   // Animal
listaAnimal.add(new Pato());     // subtipo de Animal
listaAnimal.add(new Perico());   // subtipo de Animal
listaAnimal.add(new Object());   // NO: Object es supertipo, no subtipo</code></pre>

<h2>Por que Object no se puede agregar?</h2>

<pre><code>List&lt;? super Animal&gt; podria ser List&lt;Animal&gt;.
Si fuera List&lt;Animal&gt;, meter un Object romperia el tipo.
Java lo bloquea por seguridad.

Solo puedes agregar Animal o sus SUBTIPOS (Pato, Perico)
porque esos son seguros para CUALQUIER lista que sea
Animal o superior.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>? super Animal</code> permite <strong>escribir</strong> subtipos de Animal en la lista. Esta es la gran diferencia con <code>? extends</code> (que es solo lectura).
</div>

<!-- ==================== SECCION 5 ==================== -->
<div class="page-break"></div>
<h1 class="section">5. Comparacion completa de Wildcards</h1>

<table>
  <tr><th></th><th><code>List&lt;?&gt;</code></th><th><code>List&lt;? extends Animal&gt;</code></th><th><code>List&lt;? super Animal&gt;</code></th></tr>
  <tr><td><strong>Acepta</strong></td><td>Cualquier lista</td><td>Animal y subtipos</td><td>Animal y supertipos</td></tr>
  <tr><td><strong>Leer como</strong></td><td><code>Object</code></td><td><code>Animal</code></td><td><code>Object</code></td></tr>
  <tr><td><strong>Escribir</strong></td><td>No</td><td>No</td><td>Si (subtipos de Animal)</td></tr>
  <tr><td><strong>Ejemplo</strong></td><td><code>List&lt;String&gt;</code>, <code>List&lt;Integer&gt;</code></td><td><code>List&lt;Animal&gt;</code>, <code>List&lt;Pato&gt;</code></td><td><code>List&lt;Animal&gt;</code>, <code>List&lt;Object&gt;</code></td></tr>
</table>

<h2>Regla PECS: Producer Extends, Consumer Super</h2>

<pre><code>La lista PRODUCE datos? (solo lees de ella)
  -&gt; usa extends: List&lt;? extends Animal&gt;

La lista CONSUME datos? (escribes en ella)
  -&gt; usa super: List&lt;? super Animal&gt;

Solo necesitas iterar sin tipo especifico?
  -&gt; usa unbounded: List&lt;?&gt;</code></pre>

<div class="callout callout-principio">
  <strong>Principio:</strong> PECS es la regla mnemotecnica para decidir que wildcard usar. <strong>P</strong>roducer <strong>E</strong>xtends, <strong>C</strong>onsumer <strong>S</strong>uper. Si la coleccion te da datos, usa extends. Si le metes datos, usa super.
</div>

<!-- ==================== SECCION 6 ==================== -->
<div class="page-break"></div>
<h1 class="section">6. Java Collections Framework: introduccion</h1>

<p>Dejamos generics y entramos a <strong>Collections Framework</strong>, que usa generics intensivamente.</p>

<h2>Jerarquia basica</h2>

<pre><code>Iterable&lt;T&gt;
    +-- Collection&lt;T&gt;
            +-- List&lt;T&gt;        (ordenada, permite duplicados)
            +-- Set&lt;T&gt;         (sin duplicados)
            +-- Queue&lt;T&gt;       (FIFO)

Map&lt;K,V&gt;                       (pares clave-valor, NO extiende Collection)</code></pre>

<h2>Metodos de <code>Collection&lt;T&gt;</code> que usan interfaces funcionales</h2>

<table>
  <tr><th>Metodo</th><th>Interfaz funcional</th><th>Que hace</th></tr>
  <tr><td><code>removeIf(Predicate&lt;T&gt;)</code></td><td><code>Predicate&lt;T&gt;</code></td><td>Elimina elementos que cumplen la condicion</td></tr>
  <tr><td><code>forEach(Consumer&lt;T&gt;)</code></td><td><code>Consumer&lt;T&gt;</code></td><td>Ejecuta una accion por cada elemento</td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> Collection es la interfaz raiz de listas, sets y colas. Sus metodos <code>removeIf</code> y <code>forEach</code> reciben interfaces funcionales como parametro, conectando Collections con programacion funcional.
</div>

<!-- ==================== SECCION 7 ==================== -->
<div class="page-break"></div>
<h1 class="section">7. Collection: removeIf y forEach</h1>

<h2>El codigo: collections v0</h2>

<pre><code>Collection&lt;String&gt; names = new ArrayList&lt;&gt;();

names.add("Patrobas");
names.add("Herodion");
names.add("Estaquis");
names.add("Trifosa");
names.add("Asincrito");
names.add("Jason");

//Predicate&lt;String&gt;
names.removeIf(z -&gt; z.contains("a"));

//Consumer&lt;String&gt;
names.forEach(name -&gt; System.out.println(name));

//Method Reference
//names.forEach(System.out::println);</code></pre>

<h2>Que hace <code>removeIf</code></h2>

<pre><code>names.removeIf(z -&gt; z.contains("a"))
                |          |
                |          +-- condicion: el nombre contiene "a"?
                +-- lambda que implementa Predicate&lt;String&gt;

Antes:  [Patrobas, Herodion, Estaquis, Trifosa, Asincrito, Jason]

Contienen "a": Patrobas, Estaquis, Trifosa, Asincrito, Jason

Despues: [Herodion]   (el unico sin "a" minuscula)</code></pre>

<h2>Que hace <code>forEach</code></h2>

<pre><code>names.forEach(name -&gt; System.out.println(name))
               |              |
               |              +-- accion a ejecutar por cada elemento
               +-- lambda que implementa Consumer&lt;String&gt;

Equivale a:
for (String name : names) {
    System.out.println(name);
}</code></pre>

<h2>Method Reference (alternativa)</h2>

<pre><code>names.forEach(System.out::println);
//            |           |
//            |           +-- metodo a invocar
//            +-- objeto que tiene el metodo

// Equivale a: name -&gt; System.out.println(name)</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>removeIf</code> recibe un <code>Predicate&lt;T&gt;</code> (funcion que retorna boolean) y elimina los elementos que cumplen la condicion. <code>forEach</code> recibe un <code>Consumer&lt;T&gt;</code> (funcion que no retorna nada) y la ejecuta por cada elemento.
</div>

<!-- ==================== SECCION 8 ==================== -->
<div class="page-break"></div>
<h1 class="section">8. List: Arrays.asList(), replaceAll y sort</h1>

<h2>El codigo: list v0</h2>

<pre><code>String[] names = {"Erasto", "Rufo", "Andronico","Epeneto"};

List&lt;String&gt; listNames = Arrays.asList(names);

System.out.println(listNames.getClass().getName());

listNames.set(2, "Filologo");
//listNames.removeIf(z -&gt; z.contains("a"));

listNames.replaceAll(n -&gt; n.concat("-"+n.length()));

Comparator&lt;String&gt; comp = (u,v) -&gt; u.length() - v.length();
listNames.sort(comp);

listNames.forEach(System.out::println);</code></pre>

<h2>Arrays.asList(): array a lista</h2>

<pre><code>String[] names = {"Erasto", "Rufo", "Andronico", "Epeneto"};
List&lt;String&gt; listNames = Arrays.asList(names);

Tipo real: java.util.Arrays$ArrayList (NO es java.util.ArrayList)</code></pre>

<h2>Restriccion: lista de tamanio fijo</h2>

<pre><code>listNames.set(2, "Filologo");     // modificar SI se puede
listNames.removeIf(...);          // UnsupportedOperationException
listNames.add("Nuevo");           // UnsupportedOperationException

Arrays.asList() crea una lista respaldada por el array original.
Puedes MODIFICAR elementos, pero no AGREGAR ni ELIMINAR.</code></pre>

<!-- ==================== SECCION 9 ==================== -->
<div class="page-break"></div>
<h1 class="section">9. replaceAll y sort en List</h1>

<h2>replaceAll: transformar todos los elementos</h2>

<pre><code>listNames.replaceAll(n -&gt; n.concat("-"+n.length()));
//                   |         |
//                   |         +-- concatena "-" y la longitud del nombre
//                   +-- UnaryOperator&lt;String&gt;

Antes:  [Erasto, Rufo, Filologo, Epeneto]
Despues: [Erasto-6, Rufo-4, Filologo-8, Epeneto-7]</code></pre>

<h2>sort: ordenar con Comparator</h2>

<pre><code>Comparator&lt;String&gt; comp = (u,v) -&gt; u.length() - v.length();
listNames.sort(comp);

Comparator recibe dos elementos y retorna:
  negativo -&gt; u va primero
  cero     -&gt; son iguales
  positivo -&gt; v va primero

u.length() - v.length() -&gt; ordena de menor a mayor longitud</code></pre>

<h2>Resultado final</h2>

<pre><code>Rufo-4       (4 caracteres)
Erasto-6     (8 caracteres)
Epeneto-7    (9 caracteres)
Filologo-8   (10 caracteres)</code></pre>

<h2>Metodos de List que usan interfaces funcionales</h2>

<table>
  <tr><th>Metodo</th><th>Interfaz funcional</th><th>Que hace</th></tr>
  <tr><td><code>replaceAll(UnaryOperator&lt;T&gt;)</code></td><td><code>UnaryOperator&lt;T&gt;</code></td><td>Transforma cada elemento in-place</td></tr>
  <tr><td><code>sort(Comparator&lt;T&gt;)</code></td><td><code>Comparator&lt;T&gt;</code></td><td>Ordena la lista segun el criterio</td></tr>
  <tr><td><code>forEach(Consumer&lt;T&gt;)</code></td><td><code>Consumer&lt;T&gt;</code></td><td>Ejecuta accion por cada elemento</td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>List</code> agrega metodos funcionales propios: <code>replaceAll</code> para transformar elementos y <code>sort</code> para ordenar. Ambos reciben interfaces funcionales como parametro.
</div>

<!-- ==================== SECCION 10 ==================== -->
<div class="page-break"></div>
<h1 class="section">10. @FunctionalInterface: que es y como se crea</h1>

<p>Una <strong>interfaz funcional</strong> es una interfaz con exactamente <strong>un metodo abstracto</strong>. Se puede implementar con una lambda.</p>

<h2>Estructura de una interfaz funcional</h2>

<pre><code>@FunctionalInterface
public interface Predicado&lt;T&gt; {

    boolean probar(T t);          // unico metodo abstracto

    static void and() {           // metodo static (no cuenta)
        System.out.println("Metodo and()");
    }

    default void or() {           // metodo default (no cuenta)
        System.out.println("Metodo or()");
    }
}</code></pre>

<h2>Reglas de @FunctionalInterface</h2>

<pre><code>1 metodo abstracto          -&gt; obligatorio
N metodos static             -&gt; permitidos (no cuentan)
N metodos default            -&gt; permitidos (no cuentan)
2+ metodos abstractos       -&gt; NO compila con @FunctionalInterface</code></pre>

<h2>La anotacion @FunctionalInterface</h2>

<pre><code>@FunctionalInterface
        |
        +-- Anotacion OPCIONAL pero recomendada.
            Le dice al compilador: "verifica que solo tenga
            un metodo abstracto". Si agregas otro, no compila.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>@FunctionalInterface</code> es una restriccion de compilacion que garantiza que la interfaz tenga exactamente un metodo abstracto. Los metodos <code>static</code> y <code>default</code> no cuentan porque ya tienen implementacion.
</div>

<!-- ==================== SECCION 11 ==================== -->
<div class="page-break"></div>
<h1 class="section">11. Implementar una interfaz funcional con lambda</h1>

<h2>El codigo: predicate v0</h2>

<pre><code>Predicado.and();                // llamar metodo static

Predicado&lt;Integer&gt; pre = i -&gt; true;   // lambda implementa probar()

pre.or();                       // llamar metodo default</code></pre>

<h2>Que sucede paso a paso</h2>

<pre><code>1. Predicado.and()
   -&gt; Llama al metodo static directamente desde la interfaz
   -&gt; Imprime: "Metodo and()"

2. Predicado&lt;Integer&gt; pre = i -&gt; true;
   -&gt; Crea una instancia de Predicado&lt;Integer&gt;
   -&gt; La lambda "i -&gt; true" implementa: boolean probar(Integer i) { return true; }

3. pre.or()
   -&gt; Llama al metodo default desde la instancia
   -&gt; Imprime: "Metodo or()"</code></pre>

<h2>Como se invoca cada tipo de metodo</h2>

<table>
  <tr><th>Tipo de metodo</th><th>Se invoca desde</th><th>Ejemplo</th></tr>
  <tr><td><code>static</code></td><td>La interfaz directamente</td><td><code>Predicado.and()</code></td></tr>
  <tr><td><code>default</code></td><td>Una instancia</td><td><code>pre.or()</code></td></tr>
  <tr><td><code>abstracto</code></td><td>Una instancia (via lambda)</td><td><code>pre.probar(5)</code></td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> Los metodos <code>static</code> se llaman desde la interfaz (<code>Predicado.and()</code>). Los metodos <code>default</code> y el abstracto se llaman desde una instancia creada con lambda.
</div>

<!-- ==================== SECCION 12 ==================== -->
<div class="page-break"></div>
<h1 class="section">12. Metodo static generico: composicion con and()</h1>

<h2>El problema: combinar dos predicados</h2>

<p>Queremos hacer un AND logico entre dos predicados: que ambas condiciones se cumplan.</p>

<h2>La solucion: metodo static generico en la interfaz</h2>

<pre><code>@FunctionalInterface
public interface Predicado&lt;T&gt; {

    boolean probar(T t);

    static &lt;W&gt; Predicado&lt;W&gt; and(Predicado&lt;W&gt; pre1, Predicado&lt;W&gt; pre2) {
        System.out.println("Metodo static and()");
        return x -&gt; pre1.probar(x) &amp;&amp; pre2.probar(x);
    }
}</code></pre>

<h2>Anatomia del metodo</h2>

<pre><code>static &lt;W&gt; Predicado&lt;W&gt; and(Predicado&lt;W&gt; pre1, Predicado&lt;W&gt; pre2)
        |       |               |                    |
        |       |               |                    +-- segundo predicado
        |       |               +-- primer predicado
        |       +-- retorna un nuevo Predicado&lt;W&gt;
        +-- declara su propio parametro de tipo W

El metodo recibe dos predicados del mismo tipo W
y retorna un NUEVO predicado que hace AND entre ambos.</code></pre>

<h2>El retorno es una lambda</h2>

<pre><code>return x -&gt; pre1.probar(x) &amp;&amp; pre2.probar(x);
//     |         |                    |
//     |         |                    +-- evalua el segundo predicado
//     |         +-- evalua el primer predicado
//     +-- parametro del nuevo predicado

Esto crea un NUEVO Predicado&lt;W&gt; cuyo metodo probar() hace:
  1. Evalua pre1.probar(x)
  2. Si es true, evalua pre2.probar(x)
  3. Retorna true solo si AMBOS son true</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Un metodo <code>static</code> generico puede declarar su propio parametro de tipo <code>&lt;W&gt;</code> independiente del <code>&lt;T&gt;</code> de la interfaz. La composicion retorna una nueva lambda que combina las dos condiciones.
</div>

<!-- ==================== SECCION 13 ==================== -->
<div class="page-break"></div>
<h1 class="section">13. Usando el metodo and() con variables</h1>

<h2>El codigo: predicate v2</h2>

<pre><code>Predicado&lt;Double&gt; pre1 = d -&gt; {
                            System.out.println("paso1");
                            return d &gt; 5.0;
                          };

Predicado&lt;Double&gt; pre2 = d -&gt; {
                            System.out.println("paso2");
                            return d &gt; 100.0;
                          };

Predicado&lt;Double&gt; pre3 = Predicado.and(pre1, pre2);

res = pre3.probar(500.0);
System.out.println(res);</code></pre>

<h2>Flujo de ejecucion con 500.0</h2>

<pre><code>pre3.probar(500.0)
  |
  +-- pre1.probar(500.0) -&gt; "paso1" -&gt; 500.0 &gt; 5.0 -&gt; true
  |
  +-- pre2.probar(500.0) -&gt; "paso2" -&gt; 500.0 &gt; 100.0 -&gt; true
  |
  +-- true &amp;&amp; true -&gt; true

Salida:
  Metodo static and()
  paso1
  paso2
  true</code></pre>

<h2>Flujo de ejecucion con 50.0</h2>

<pre><code>pre3.probar(50.0)
  |
  +-- pre1.probar(50.0) -&gt; "paso1" -&gt; 50.0 &gt; 5.0 -&gt; true
  |
  +-- pre2.probar(50.0) -&gt; "paso2" -&gt; 50.0 &gt; 100.0 -&gt; false
  |
  +-- true &amp;&amp; false -&gt; false

Salida:
  Metodo static and()
  paso1
  paso2
  false</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>and()</code> se ejecuta una sola vez (al crear pre3). Despues, cada llamada a <code>pre3.probar()</code> ejecuta ambas lambdas internamente. El <code>&amp;&amp;</code> de Java es short-circuit: si pre1 es false, pre2 ni se evalua.
</div>

<!-- ==================== SECCION 14 ==================== -->
<div class="page-break"></div>
<h1 class="section">14. Composicion inline: lambdas en and()</h1>

<h2>El codigo: predicate v3</h2>

<pre><code>System.out.println(Predicado.&lt;Double&gt;and(
        d -&gt; {
            System.out.println("paso1");
            return d &gt; 5.0;
         }, d -&gt; {
            System.out.println("paso2");
            return d &gt; 100.0;
         }).probar(50.0));</code></pre>

<h2>Que cambio respecto a v2</h2>

<pre><code>v2: Crea variables pre1 y pre2, luego las pasa a and()
v3: Pasa las lambdas DIRECTAMENTE como argumentos de and()

v2:                              v3:
  Predicado&lt;Double&gt; pre1 = ...     Predicado.&lt;Double&gt;and(
  Predicado&lt;Double&gt; pre2 = ...         d -&gt; ...,
  Predicado.and(pre1, pre2)            d -&gt; ...
                                   ).probar(50.0)</code></pre>

<h2>Nota: <code>Predicado.&lt;Double&gt;and(...)</code> con tipo explicito</h2>

<pre><code>Predicado.&lt;Double&gt;and(...)
          |
          +-- El compilador necesita saber que W = Double
              porque las lambdas inline no dan suficiente
              informacion para inferir el tipo.</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> No es necesario guardar las lambdas en variables. Se pueden pasar directamente como argumentos. Esto es mas conciso pero puede ser menos legible en lambdas complejas.
</div>

<!-- ==================== SECCION 15 ==================== -->
<div class="page-break"></div>
<h1 class="section">15. Lambdas simplificadas: de bloque a expresion</h1>

<h2>El codigo: predicate v4</h2>

<pre><code>System.out.println(Predicado.&lt;Double&gt;and(
        d -&gt; d &gt; 5.0
      , d -&gt; d &gt; 100.0
     ).probar(50.0));</code></pre>

<h2>Evolucion de la simplificacion</h2>

<pre><code>v2: Lambdas con bloque {} y variables separadas
    Predicado&lt;Double&gt; pre1 = d -&gt; {
        System.out.println("paso1");
        return d &gt; 5.0;
    };

v3: Lambdas con bloque {} inline en and()
    Predicado.&lt;Double&gt;and(
        d -&gt; { return d &gt; 5.0; },
        d -&gt; { return d &gt; 100.0; }
    ).probar(50.0)

v4: Lambdas de expresion (sin {} ni return)
    Predicado.&lt;Double&gt;and(
        d -&gt; d &gt; 5.0,
        d -&gt; d &gt; 100.0
    ).probar(50.0)</code></pre>

<h2>Regla de simplificacion de lambdas</h2>

<pre><code>Lambda con bloque (varias lineas):
  d -&gt; {
      System.out.println("paso1");
      return d &gt; 5.0;
  }

Lambda de expresion (una sola linea):
  d -&gt; d &gt; 5.0

Si el cuerpo es UNA SOLA EXPRESION:
  - Se quitan las llaves {}
  - Se quita el return
  - Se quita el punto y coma
  - El valor de la expresion ES el retorno</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Cuando una lambda tiene una sola expresion, se puede simplificar a la forma <code>parametro -&gt; expresion</code>. El resultado de la expresion se retorna automaticamente.
</div>

<!-- ==================== SECCION 16 ==================== -->
<div class="page-break"></div>
<h1 class="section">16. java.util.function.Predicate: la interfaz built-in</h1>

<p>Java ya incluye una interfaz <code>Predicate&lt;T&gt;</code> en el paquete <code>java.util.function</code>. No necesitas crear la tuya propia.</p>

<h2>El codigo: predicate v0</h2>

<pre><code>import java.util.function.Predicate;
import java.math.BigDecimal;

Predicate&lt;String&gt; pre1 = w -&gt; w.contains("v");

boolean res = pre1.test("Phyton");     // false (no tiene "v")
System.out.println(res);

res = pre1.test("Java");               // true (tiene "v" en "va")
System.out.println(res);

Predicate&lt;BigDecimal&gt; pre2 = x -&gt; x.equals(new BigDecimal(4.0));
res = pre2.test(new BigDecimal(4.0));  // true
System.out.println("BigDecimal: "+res);</code></pre>

<h2>Predicate custom vs built-in</h2>

<table>
  <tr><th></th><th>Tu <code>Predicado&lt;T&gt;</code></th><th><code>java.util.function.Predicate&lt;T&gt;</code></th></tr>
  <tr><td>Metodo abstracto</td><td><code>probar(T)</code></td><td><code>test(T)</code></td></tr>
  <tr><td>and()</td><td>Tu implementacion static</td><td><code>pre1.and(pre2)</code> (metodo default)</td></tr>
  <tr><td>or()</td><td>Tu implementacion default</td><td><code>pre1.or(pre2)</code> (metodo default)</td></tr>
  <tr><td>negate()</td><td>No lo tiene</td><td><code>pre1.negate()</code> (metodo default)</td></tr>
  <tr><td>Paquete</td><td>Tu paquete</td><td><code>java.util.function</code></td></tr>
</table>

<h2>Metodos del Predicate built-in</h2>

<pre><code>Predicate&lt;T&gt;
  |
  +-- boolean test(T t)           // metodo abstracto
  +-- Predicate&lt;T&gt; and(Predicate) // default: AND logico
  +-- Predicate&lt;T&gt; or(Predicate)  // default: OR logico
  +-- Predicate&lt;T&gt; negate()       // default: NOT logico
  +-- static Predicate&lt;T&gt; isEqual(Object) // static: igualdad</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>java.util.function.Predicate&lt;T&gt;</code> es la version oficial de Java. Su metodo abstracto es <code>test(T)</code>. Ya incluye <code>and()</code>, <code>or()</code> y <code>negate()</code> como metodos default. Es la misma interfaz que usan <code>removeIf()</code>, <code>filter()</code> y otras APIs de Collections y Streams.
</div>

<!-- ==================== SECCION 17 ==================== -->
<div class="page-break"></div>
<h1 class="section">17. Conexion: Collections usa interfaces funcionales</h1>

<p>Los temas del dia se conectan directamente:</p>

<pre><code>Generics                    Interfaces Funcionales
   |                              |
   +-- List&lt;String&gt;               +-- Predicate&lt;String&gt;
       Collection&lt;String&gt;             Consumer&lt;String&gt;
       Comparator&lt;String&gt;             UnaryOperator&lt;String&gt;
              |                              |
              +----------+-------------------+
                         |
                   Collections API
                         |
              +----------+----------+
              |          |          |
         removeIf    forEach    replaceAll
        (Predicate) (Consumer) (UnaryOperator)</code></pre>

<h2>Ejemplo integrador</h2>

<pre><code>Collection&lt;String&gt; names = new ArrayList&lt;&gt;();
names.add("Patrobas");
names.add("Jason");

// Predicate: funcion que retorna boolean
names.removeIf(z -&gt; z.contains("a"));    // elimina los que tienen "a"

// Consumer: funcion que no retorna nada
names.forEach(name -&gt; System.out.println(name));</code></pre>

<div class="callout callout-principio">
  <strong>Principio:</strong> Collections Framework usa generics para tipar las colecciones e interfaces funcionales para operar sobre ellas. Los tres temas del dia (Generics, Collections, Predicate) estan interconectados.
</div>

<!-- ==================== RESUMEN ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Resumen de conceptos clave</h1>

<table>
  <tr><th>Concepto</th><th>Descripcion</th></tr>
  <tr><td><code>List&lt;? super Animal&gt;</code></td><td>Lower Bounded Wildcard. Acepta Animal y supertipos</td></tr>
  <tr><td>PECS</td><td>Producer Extends, Consumer Super</td></tr>
  <tr><td><code>? super</code> lectura</td><td>Se lee como <code>Object</code> (tipo mas general)</td></tr>
  <tr><td><code>? super</code> escritura</td><td>Se puede agregar Animal y sus subtipos</td></tr>
  <tr><td><code>Collection&lt;T&gt;</code></td><td>Interfaz raiz de List, Set y Queue</td></tr>
  <tr><td><code>removeIf(Predicate)</code></td><td>Elimina elementos que cumplen la condicion</td></tr>
  <tr><td><code>forEach(Consumer)</code></td><td>Ejecuta accion por cada elemento</td></tr>
  <tr><td><code>Arrays.asList()</code></td><td>Convierte array en lista de tamanio fijo</td></tr>
  <tr><td><code>replaceAll(UnaryOperator)</code></td><td>Transforma cada elemento in-place</td></tr>
  <tr><td><code>sort(Comparator)</code></td><td>Ordena la lista segun criterio</td></tr>
  <tr><td><code>@FunctionalInterface</code></td><td>Interfaz con exactamente un metodo abstracto</td></tr>
  <tr><td>Metodo <code>static</code> en interfaz</td><td>Se invoca desde la interfaz: <code>Predicado.and()</code></td></tr>
  <tr><td>Metodo <code>default</code> en interfaz</td><td>Se invoca desde una instancia: <code>pre.or()</code></td></tr>
  <tr><td>Lambda de expresion</td><td><code>d -&gt; d &gt; 5.0</code> (sin llaves ni return)</td></tr>
  <tr><td>Lambda de bloque</td><td><code>d -&gt; { return d &gt; 5.0; }</code> (con llaves y return)</td></tr>
  <tr><td><code>Predicate&lt;T&gt;</code> built-in</td><td><code>java.util.function.Predicate&lt;T&gt;</code> con metodo <code>test(T)</code></td></tr>
</table>

<!-- ==================== PROGRESION ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Progresion de los ejercicios del dia</h1>

<table>
  <tr><th>Proyecto</th><th>Paquete</th><th>Version</th><th>Tema</th></tr>
  <tr><td>generics</td><td><code>com.curso</code></td><td>v8</td><td>Lower Bounded Wildcard <code>? super Animal</code> (lectura)</td></tr>
  <tr><td>generics</td><td><code>com.curso</code></td><td>v9</td><td>Lower Bounded Wildcard <code>? super Animal</code> (escritura con add)</td></tr>
  <tr><td>collections</td><td><code>com.curso</code></td><td>v0</td><td><code>Collection&lt;String&gt;</code> con removeIf y forEach</td></tr>
  <tr><td>collections</td><td><code>com.list</code></td><td>v0</td><td><code>List&lt;String&gt;</code> con Arrays.asList, replaceAll y sort</td></tr>
  <tr><td>interfaceFunctional</td><td><code>com.predicate</code></td><td>v0</td><td>@FunctionalInterface: metodo abstracto, static y default</td></tr>
  <tr><td>interfaceFunctional</td><td><code>com.predicate</code></td><td>v1</td><td>Refuerzo: crear lambda e invocar metodos de la interfaz</td></tr>
  <tr><td>interfaceFunctional</td><td><code>com.predicate</code></td><td>v2</td><td>Metodo static generico <code>and()</code> con variables separadas</td></tr>
  <tr><td>interfaceFunctional</td><td><code>com.predicate</code></td><td>v3</td><td>Composicion inline: lambdas como argumentos de and()</td></tr>
  <tr><td>interfaceFunctional</td><td><code>com.predicate</code></td><td>v4</td><td>Simplificacion: lambdas de expresion en una linea</td></tr>
  <tr><td>predicate</td><td><code>com.curso</code></td><td>v0</td><td><code>java.util.function.Predicate&lt;T&gt;</code> built-in con test()</td></tr>
</table>

</body>
</html>
"""

if __name__ == "__main__":
    html = weasyprint.HTML(string=HTML_CONTENT)
    html.write_pdf("240226.pdf")
    print("PDF generado: 240226.pdf")
