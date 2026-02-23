#!/usr/bin/env python3
"""
Genera el PDF de la Guia de Repaso del 23 de febrero de 2026.
Tema: Generics en Java.
Estilo visual consistente con los PDFs anteriores del curso.
"""
import weasyprint

TOTAL_PAGES = 18

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  @page {{
    size: letter;
    margin: 2.5cm 2.5cm 3cm 2.5cm;
    @bottom-center {{
      content: "Pagina " counter(page) "/{TOTAL_PAGES}";
      font-size: 10px;
      color: #999;
    }}
    @top-left {{
      content: "Curso de Java - Generics";
      font-size: 9px;
      color: #999;
    }}
    @top-right {{
      content: "Semana 03 | 23 Feb 2026";
      font-size: 9px;
      color: #999;
    }}
  }}

  @page:first {{
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-center {{ content: "Pagina 1/{TOTAL_PAGES}"; font-size: 10px; color: #999; }}
  }}

  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #333;
  }}

  /* --- PORTADA --- */
  .cover {{
    text-align: center;
    padding-top: 80px;
    page-break-after: always;
  }}
  .cover h1 {{
    font-size: 36pt;
    color: #E8A838;
    font-style: italic;
    margin-bottom: 10px;
  }}
  .cover h2 {{
    font-size: 22pt;
    color: #5DADE2;
    font-weight: bold;
    margin-bottom: 30px;
  }}
  .cover .separator {{
    width: 60px;
    height: 4px;
    background: #E8A838;
    margin: 0 auto 30px;
  }}
  .cover .info {{
    font-size: 11pt;
    color: #666;
    margin-bottom: 5px;
  }}
  .cover .temas-title {{
    font-size: 12pt;
    font-weight: bold;
    margin-top: 40px;
    margin-bottom: 15px;
  }}
  .cover .temas {{
    text-align: left;
    display: inline-block;
    font-size: 11pt;
    color: #444;
  }}
  .cover .temas li {{
    margin-bottom: 6px;
  }}
  .cover .instructor {{
    font-style: italic;
    color: #E8A838;
    font-size: 13pt;
    margin-top: 50px;
  }}

  /* --- SECCIONES --- */
  h1.section {{
    font-size: 22pt;
    color: #5DADE2;
    border-bottom: none;
    margin-top: 10px;
    margin-bottom: 5px;
    page-break-after: avoid;
  }}
  h1.section::after {{
    content: '';
    display: block;
    width: 50px;
    height: 4px;
    background: #E8A838;
    margin-top: 8px;
    margin-bottom: 15px;
  }}

  h2 {{
    font-size: 15pt;
    color: #333;
    margin-top: 25px;
    margin-bottom: 10px;
    page-break-after: avoid;
  }}

  h3 {{
    font-size: 12pt;
    color: #444;
    margin-top: 20px;
    margin-bottom: 8px;
    page-break-after: avoid;
  }}

  /* --- RESUMEN TITLE --- */
  h1.resumen {{
    font-size: 22pt;
    color: #E8A838;
    margin-top: 10px;
    margin-bottom: 5px;
    page-break-after: avoid;
  }}
  h1.resumen::after {{
    content: '';
    display: block;
    width: 50px;
    height: 4px;
    background: #E8A838;
    margin-top: 8px;
    margin-bottom: 15px;
  }}

  /* --- CODIGO --- */
  pre {{
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
  }}

  code {{
    font-family: 'SF Mono', 'Menlo', 'Monaco', 'Consolas', monospace;
    font-size: 9pt;
    background: #EBF0F5;
    padding: 1px 5px;
    border-radius: 3px;
  }}

  pre code {{
    background: none;
    padding: 0;
    font-size: 8.5pt;
  }}

  /* --- CALLOUTS --- */
  .callout {{
    padding: 12px 15px;
    margin: 12px 0;
    border-radius: 0 4px 4px 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
  }}
  .callout-clave {{
    background: #E8F8E8;
    border-left: 4px solid #4CAF50;
  }}
  .callout-problema {{
    background: #FCE4E4;
    border-left: 4px solid #E74C3C;
  }}
  .callout-nota {{
    background: #FFF8E1;
    border-left: 4px solid #F5A623;
  }}
  .callout-principio {{
    background: #E3F2FD;
    border-left: 4px solid #2196F3;
  }}
  .callout strong {{
    color: inherit;
  }}
  .callout-clave strong:first-child {{ color: #2E7D32; }}
  .callout-problema strong:first-child {{ color: #C62828; }}
  .callout-nota strong:first-child {{ color: #E65100; }}
  .callout-principio strong:first-child {{ color: #1565C0; }}

  /* --- TABLAS --- */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0;
    font-size: 10pt;
    page-break-inside: avoid;
  }}
  table th {{
    background: #5DADE2;
    color: white;
    padding: 8px 12px;
    text-align: left;
    font-weight: bold;
  }}
  table td {{
    padding: 7px 12px;
    border-bottom: 1px solid #E0E0E0;
  }}
  table tr:nth-child(even) td {{
    background: #F8FAFB;
  }}

  p {{
    margin: 8px 0;
  }}

  .page-break {{
    page-break-before: always;
  }}
</style>
</head>
<body>

<!-- ==================== PORTADA ==================== -->
<div class="cover">
  <h1>Guia de Repaso</h1>
  <h2>Generics en Java</h2>
  <div class="separator"></div>
  <p class="info">Semana 03 - Lunes 23 de Febrero de 2026</p>
  <p class="info">Academia Java - Ciudad de Mexico</p>

  <p class="temas-title">Temas del dia:</p>
  <div class="temas">
    <ol>
      <li>Raw types: listas sin tipo y sus problemas</li>
      <li>ClassCastException: el peligro de no tipar colecciones</li>
      <li>Solucion con generics: <code>List&lt;Tipo&gt;</code> y seguridad en compilacion</li>
      <li>Pattern Matching con instanceof (Java 14+)</li>
      <li>Invariancia de generics: por que <code>List&lt;Pato&gt;</code> no es <code>List&lt;Animal&gt;</code></li>
      <li>Unbounded Wildcard <code>List&lt;?&gt;</code>: colecciones de solo lectura</li>
      <li>Interfaces y clases genericas propias: <code>Operacion&lt;T,U,W&gt;</code></li>
      <li>Upper bounded types: <code>&lt;T extends Number&gt;</code></li>
      <li>Metodos genericos estaticos: <code>&lt;V&gt; V metodo(V v)</code></li>
    </ol>
  </div>

  <p class="instructor">Instructor: Miguel Rugerio</p>
</div>

<!-- ==================== 1. RAW TYPES ==================== -->
<h1 class="section">1. Raw Types: listas sin tipo</h1>

<p>
  Antes de Java 5, las colecciones no tenian tipo. Se declaraban como <code>List</code> a secas (sin <code>&lt;&gt;</code>).
  Esto se conoce como <strong>raw type</strong>.
</p>

<h2>El problema: se puede meter cualquier cosa</h2>

<pre><code>List lista = new ArrayList();

lista.add("Patrobas");
lista.add(new StringBuilder("Epeneto"));
lista.add(Integer.valueOf(1000));
lista.add(new Object());
lista.add(88.88);</code></pre>

<p>La lista acepta <strong>cualquier objeto</strong>: String, StringBuilder, Integer, Object, Double.
No hay forma de saber en compilacion que tipo de datos contiene.</p>

<h2>Para iterar, todo es Object</h2>

<pre><code>for (Object o : lista) {{
    System.out.println(o.getClass().getSimpleName());
    System.out.println(o);
}}</code></pre>

<table>
  <tr><th>Objeto</th><th>getClass().getSimpleName()</th></tr>
  <tr><td><code>"Patrobas"</code></td><td>String</td></tr>
  <tr><td><code>new StringBuilder("Epeneto")</code></td><td>StringBuilder</td></tr>
  <tr><td><code>Integer.valueOf(1000)</code></td><td>Integer</td></tr>
  <tr><td><code>new Object()</code></td><td>Object</td></tr>
  <tr><td><code>88.88</code></td><td>Double</td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> Con raw types, el compilador no puede ayudarte. Todo es <code>Object</code>
  y necesitas hacer casting manual para usar metodos especificos de cada tipo.
</div>

<!-- ==================== 2. INSTANCEOF Y CASTING ==================== -->
<div class="page-break"></div>
<h1 class="section">2. instanceof y casting manual</h1>

<p>Si necesitas usar un metodo especifico de un tipo, debes hacer <code>instanceof</code> y luego un cast:</p>

<pre><code>for (Object o : lista) {{
    if (o instanceof StringBuilder)
        ((StringBuilder) o).append(" Tercio");
    System.out.println(o);
}}</code></pre>

<h2>El flujo del casting</h2>

<pre><code>Object o
   |
   +-- instanceof StringBuilder?  -> SI -> ((StringBuilder) o).append(...)
   |
   +-- instanceof String?         -> SI -> ((String) o).toUpperCase()</code></pre>

<div class="callout callout-problema">
  <strong>Problema:</strong> Este patron es fragil. Si agregas un tipo nuevo a la lista,
  el codigo de iteracion no se entera y puede fallar en tiempo de ejecucion.
</div>

<!-- ==================== 3. CLASSCASTEXCEPTION ==================== -->
<div class="page-break"></div>
<h1 class="section">3. ClassCastException: el peligro real</h1>

<h2>El escenario: una jerarquia de clases</h2>

<pre><code>class Animal {{
    void volar() {{
        System.out.println("Volar Animal");
    }}
}}

class Pato extends Animal {{
    void volarPato() {{
        System.out.println("Volar Pato");
    }}
}}

class Perico extends Animal {{
    void volarPerico() {{
        System.out.println("Volar Perico");
    }}
}}</code></pre>

<h2>El problema con raw types</h2>

<pre><code>List lista = new ArrayList();

lista.add(new Pato());
lista.add(new Pato());
lista.add(new Pato());
lista.add(new Perico());   // &lt;-- se cuela un Perico

for (Object pato : lista) {{
    ((Pato) pato).volarPato();   // BOOM! ClassCastException en el Perico
}}</code></pre>

<h2>Que pasa en tiempo de ejecucion</h2>

<pre><code>Iteracion 1: Pato    -> ((Pato) pato).volarPato()  ✓
Iteracion 2: Pato    -> ((Pato) pato).volarPato()  ✓
Iteracion 3: Pato    -> ((Pato) pato).volarPato()  ✓
Iteracion 4: Perico  -> ((Pato) pato).volarPato()  ✗ ClassCastException!</code></pre>

<div class="callout callout-problema">
  <strong>Problema:</strong> El compilador no avisa. El error ocurre <strong>en tiempo de ejecucion</strong>,
  cuando ya es demasiado tarde. Esto es exactamente lo que los generics resuelven.
</div>

<!-- ==================== 4. LA SOLUCION: GENERICS ==================== -->
<div class="page-break"></div>
<h1 class="section">4. La solucion: List con generics</h1>

<h2>Tipar la lista con <code>List&lt;Tipo&gt;</code></h2>

<pre><code>List&lt;Pato&gt; lista = new ArrayList&lt;&gt;();

lista.add(new Pato());
lista.add(new Pato());
lista.add(new Pato());
//lista.add(new Perico());  // NO COMPILA - error en compilacion

for (Pato pato : lista) {{
    pato.volarPato();   // seguro, todos son Pato
}}</code></pre>

<h2>Antes vs despues</h2>

<table>
  <tr><th>Sin generics (raw type)</th><th>Con generics</th></tr>
  <tr><td><code>List lista = new ArrayList()</code></td><td><code>List&lt;Pato&gt; lista = new ArrayList&lt;&gt;()</code></td></tr>
  <tr><td>Acepta cualquier objeto</td><td>Solo acepta <code>Pato</code></td></tr>
  <tr><td>Error en tiempo de ejecucion</td><td>Error en tiempo de compilacion</td></tr>
  <tr><td>Necesita casting manual</td><td>No necesita casting</td></tr>
  <tr><td><code>for (Object o : lista)</code></td><td><code>for (Pato p : lista)</code></td></tr>
</table>

<h2>Listas tipadas por tipo</h2>

<pre><code>List&lt;Pato&gt; listaPato = new ArrayList&lt;&gt;();
listaPato.add(new Pato());
//listaPato.add(new Perico());   // NO COMPILA

List&lt;Perico&gt; listaPerico = new ArrayList&lt;&gt;();
listaPerico.add(new Perico());
//listaPerico.add(new Pato());   // NO COMPILA

List&lt;Animal&gt; listaAnimal = new ArrayList&lt;&gt;();
listaAnimal.add(new Perico());   // SI compila (Perico ES Animal)
listaAnimal.add(new Pato());     // SI compila (Pato ES Animal)
listaAnimal.add(new Animal());   // SI compila</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>List&lt;Animal&gt;</code> acepta cualquier subtipo de Animal.
  Pero <code>List&lt;Pato&gt;</code> solo acepta Pato. Los generics mueven el error de
  <strong>runtime a compilacion</strong>.
</div>

<!-- ==================== 5. PATTERN MATCHING ==================== -->
<div class="page-break"></div>
<h1 class="section">5. Pattern Matching con instanceof (Java 14+)</h1>

<p>Cuando iteras una <code>List&lt;Animal&gt;</code>, necesitas distinguir los subtipos.
Java 14 introdujo <strong>Pattern Matching</strong> para simplificar el instanceof + cast:</p>

<h2>Antes de Java 14 (cast manual)</h2>

<pre><code>for (Animal ani : listaAnimal) {{
    if (ani instanceof Perico)
        ((Perico) ani).volarPerico();   // cast manual
}}</code></pre>

<h2>Con Pattern Matching (Java 14+)</h2>

<pre><code>for (Animal ani : listaAnimal) {{
    if (ani instanceof Pato p)       // declara variable 'p' ya casteada
        p.volarPato();               // usa 'p' directamente

    if (ani instanceof Perico per)   // declara variable 'per' ya casteada
        per.volarPerico();
}}</code></pre>

<h2>Que hace <code>instanceof Pato p</code></h2>

<pre><code>ani instanceof Pato p
        |          |  |
        |          |  +-- variable local ya casteada a Pato
        |          +-- tipo a verificar
        +-- objeto a evaluar

Equivale a:
  if (ani instanceof Pato) {{
      Pato p = (Pato) ani;
  }}</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Pattern Matching elimina la redundancia del cast manual. En una sola
  expresion verificas el tipo Y obtienes la variable casteada. Es mas seguro y legible.
</div>

<!-- ==================== 6. INVARIANCIA ==================== -->
<div class="page-break"></div>
<h1 class="section">6. Invariancia de generics</h1>

<h2>El problema: <code>List&lt;Pato&gt;</code> NO es <code>List&lt;Animal&gt;</code></h2>

<p>En herencia normal, un Pato <strong>ES</strong> un Animal. Pero en generics,
<code>List&lt;Pato&gt;</code> <strong>NO ES</strong> <code>List&lt;Animal&gt;</code>:</p>

<pre><code>static void showAnimal(List&lt;Animal&gt; listaAnimal) {{
    for (Animal ani : listaAnimal) {{
        System.out.println(ani.getClass().getSimpleName());
    }}
}}

List&lt;Animal&gt; listaAnimal = new ArrayList&lt;&gt;();
showAnimal(listaAnimal);    // ✓ compila

List&lt;Pato&gt; listaPato = new ArrayList&lt;&gt;();
showAnimal(listaPato);      // ✗ NO COMPILA

List&lt;Perico&gt; listaPerico = new ArrayList&lt;&gt;();
showAnimal(listaPerico);    // ✗ NO COMPILA</code></pre>

<h2>Por que?</h2>

<pre><code>Herencia de clases:      Pato extends Animal             ✓
Herencia de generics:    List&lt;Pato&gt; extends List&lt;Animal&gt;   ✗ NO EXISTE

Aunque Pato ES Animal,
List&lt;Pato&gt; NO ES List&lt;Animal&gt;</code></pre>

<p>Esto se llama <strong>invariancia</strong>: los generics no heredan la relacion de sus tipos parametrizados.</p>

<h2>Tampoco se puede asignar</h2>

<pre><code>List&lt;Animal&gt; listaAnimal2 = listaPato;    // NO COMPILA
List&lt;Animal&gt; listaAnimal3 = listaPerico;  // NO COMPILA</code></pre>

<div class="callout callout-problema">
  <strong>Problema:</strong> Si necesitas un metodo que acepte <code>List&lt;Pato&gt;</code>,
  <code>List&lt;Perico&gt;</code> y <code>List&lt;Animal&gt;</code>, no puedes usar
  <code>List&lt;Animal&gt;</code> como parametro. Necesitas <strong>wildcards</strong>.
</div>

<!-- ==================== 7. UNBOUNDED WILDCARD ==================== -->
<div class="page-break"></div>
<h1 class="section">7. Unbounded Wildcard: <code>List&lt;?&gt;</code></h1>

<h2>La solucion: <code>?</code> acepta cualquier tipo</h2>

<pre><code>static void showAnimal(List&lt;?&gt; listaAnimal) {{

    //Trata al collection solo de LECTURA
    //listaAnimal.add(new Pato()); //DON'T COMPILE

    for (Object ani : listaAnimal) {{
        System.out.println(ani.getClass().getSimpleName());
        if (ani instanceof Perico)
            ((Perico) ani).volarPerico();
        if (ani instanceof Pato)
            ((Pato) ani).volarPato();
        ((Animal) ani).volar();
    }}
}}</code></pre>

<p>Ahora el metodo acepta <strong>cualquier</strong> tipo de lista:</p>

<pre><code>List&lt;Animal&gt; listaAnimal = new ArrayList&lt;&gt;();
showAnimal(listaAnimal);     // ✓

List&lt;Pato&gt; listaPato = new ArrayList&lt;&gt;();
showAnimal(listaPato);       // ✓ ahora SI compila

List&lt;Perico&gt; listaPerico = new ArrayList&lt;&gt;();
showAnimal(listaPerico);     // ✓ ahora SI compila</code></pre>

<h2>Que significa <code>?</code></h2>

<pre><code>List&lt;?&gt;
      |
      +-- "?" = tipo desconocido (unbounded wildcard)

Acepta: List&lt;Animal&gt;, List&lt;Pato&gt;, List&lt;Perico&gt;, List&lt;Object&gt;, List&lt;String&gt;...</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>List&lt;?&gt;</code> es la forma de decir "acepto una lista de cualquier tipo".
  Resuelve el problema de invariancia de los generics.
</div>

<!-- ==================== 8. RESTRICCION SOLO LECTURA ==================== -->
<div class="page-break"></div>
<h1 class="section">8. Restriccion de <code>List&lt;?&gt;</code>: solo lectura</h1>

<p><code>List&lt;?&gt;</code> tiene una restriccion importante: <strong>no puedes agregar elementos</strong>.</p>

<h2>No compila: agregar a <code>List&lt;?&gt;</code></h2>

<pre><code>static void showAnimal(List&lt;?&gt; listaAnimal) {{
    listaAnimal.add(new Pato());    // NO COMPILA
    listaAnimal.add(new Perico());  // NO COMPILA
    listaAnimal.add(new Object());  // NO COMPILA
}}</code></pre>

<h2>Tampoco al asignar a una variable <code>List&lt;?&gt;</code></h2>

<pre><code>List&lt;Pato&gt; listaPato = new ArrayList&lt;&gt;();
listaPato.add(new Pato());

List&lt;?&gt; lista1 = listaPato;     // ✓ asignar SI se puede
lista1.add(new Pato());         // ✗ NO COMPILA</code></pre>

<h2>Por que no se puede agregar?</h2>

<pre><code>List&lt;?&gt; lista = listaPato;     // ? podria ser Pato
List&lt;?&gt; lista = listaPerico;   // ? podria ser Perico
List&lt;?&gt; lista = listaAnimal;   // ? podria ser Animal

Si ? es desconocido, Java no puede garantizar
que lo que agregas sea del tipo correcto.
Por seguridad, bloquea TODOS los add().</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>List&lt;?&gt;</code> convierte la coleccion en <strong>solo lectura</strong>.
  Puedes iterar y leer, pero no agregar. Esto es una garantia de seguridad de tipos en tiempo de compilacion.
</div>

<!-- ==================== 9. LIST<?> CON LIST<OBJECT> ==================== -->
<div class="page-break"></div>
<h1 class="section">9. <code>List&lt;?&gt;</code> con <code>List&lt;Object&gt;</code></h1>

<p><code>List&lt;?&gt;</code> tambien acepta <code>List&lt;Object&gt;</code>, algo que
<code>List&lt;Animal&gt;</code> no podia:</p>

<pre><code>List&lt;Object&gt; listaObject = new ArrayList&lt;&gt;();
listaObject.add(new Object());
listaObject.add(new Perico());
listaObject.add(Integer.valueOf(1000));

showAnimal(listaObject);   // ✓ funciona con List&lt;?&gt;

List&lt;?&gt; lista3 = listaObject;
lista3.add(new Object());   // ✗ NO COMPILA (sigue siendo solo lectura)</code></pre>

<h2>Comparacion: <code>List&lt;Animal&gt;</code> vs <code>List&lt;?&gt;</code></h2>

<table>
  <tr><th>Caracteristica</th><th><code>List&lt;Animal&gt;</code></th><th><code>List&lt;?&gt;</code></th></tr>
  <tr><td>Acepta <code>List&lt;Animal&gt;</code></td><td>✓</td><td>✓</td></tr>
  <tr><td>Acepta <code>List&lt;Pato&gt;</code></td><td>✗</td><td>✓</td></tr>
  <tr><td>Acepta <code>List&lt;Perico&gt;</code></td><td>✗</td><td>✓</td></tr>
  <tr><td>Acepta <code>List&lt;Object&gt;</code></td><td>✗</td><td>✓</td></tr>
  <tr><td>Se puede hacer <code>add()</code></td><td>✓</td><td>✗</td></tr>
  <tr><td>Tipo de iteracion</td><td><code>Animal</code></td><td><code>Object</code></td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>List&lt;?&gt;</code> es mas flexible que <code>List&lt;Animal&gt;</code>
  para <strong>leer</strong>, pero no permite <strong>escribir</strong>. Es un trade-off:
  flexibilidad de tipos a cambio de coleccion de solo lectura.
</div>

<!-- ==================== 10. INTERFACES GENERICAS ==================== -->
<div class="page-break"></div>
<h1 class="section">10. Interfaces genericas: <code>Operacion&lt;T,U,W&gt;</code></h1>

<p>Ademas de usar generics en colecciones, puedes <strong>crear tus propias</strong>
interfaces y clases genericas.</p>

<h2>Definir una interfaz generica con 3 parametros de tipo</h2>

<pre><code>public interface Operacion&lt;T, U, W&gt; {{
    W ejecuta(T t, U u);
}}</code></pre>

<h2>Que significa cada parametro</h2>

<pre><code>Operacion&lt;T, U, W&gt;
           |  |  |
           |  |  +-- W = tipo de RETORNO
           |  +-- U = tipo del segundo parametro
           +-- T = tipo del primer parametro</code></pre>

<h2>Implementar con tipos concretos</h2>

<pre><code>public class Suma implements Operacion&lt;Integer, Float, Double&gt; {{

    @Override
    public Double ejecuta(Integer x, Float y) {{
        double d = x + y;
        return d;
    }}
}}</code></pre>

<h2>Uso</h2>

<pre><code>Suma ope1 = new Suma();
double d = ope1.ejecuta(10, 8.0f);   // d = 18.0
System.out.println(d);</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> Al implementar <code>Operacion&lt;Integer, Float, Double&gt;</code>,
  los tipos genericos T, U, W se reemplazan por tipos concretos. El compilador verifica que
  <code>ejecuta</code> reciba un <code>Integer</code> y un <code>Float</code>,
  y retorne un <code>Double</code>.
</div>

<!-- ==================== 11. UPPER BOUNDED TYPES ==================== -->
<div class="page-break"></div>
<h1 class="section">11. Upper Bounded Types: <code>&lt;T extends Number&gt;</code></h1>

<h2>El problema: aceptar solo tipos numericos</h2>

<p>Queremos que la clase Suma funcione con cualquier combinacion de numeros
(Integer, Float, Double, Long...) pero <strong>no con String u Object</strong>.</p>

<h2>Solucion: restringir con <code>extends</code></h2>

<pre><code>public interface Operacion&lt;T, U&gt; {{
    Number ejecuta(T t, U u);
}}

public class Suma&lt;T extends Number, U extends Number&gt;
                    implements Operacion&lt;T, U&gt; {{

    @Override
    public Number ejecuta(T t, U u) {{
        double d1 = t.doubleValue();   // metodo de Number
        double d2 = u.doubleValue();   // metodo de Number
        return d1 + d2;
    }}
}}</code></pre>

<h2>Que significa <code>T extends Number</code></h2>

<pre><code>T extends Number
|         |
|         +-- limite superior: T DEBE ser Number o subtipo de Number
+-- parametro de tipo

Acepta: Integer, Float, Double, Long, Short, Byte
NO acepta: String, Object, StringBuilder</code></pre>

<h2>Uso con diferentes tipos numericos</h2>

<pre><code>Suma&lt;Integer, Float&gt; suma1 = new Suma&lt;&gt;();
Suma&lt;Long, Byte&gt; suma2 = new Suma&lt;&gt;();
Suma&lt;Double, Short&gt; suma3 = new Suma&lt;&gt;();

System.out.println(suma1.ejecuta(4, 3.0f));        // 7.0
System.out.println(suma2.ejecuta(8L, (byte) 127)); // 135.0
System.out.println(suma3.ejecuta(4.0, (short) 5)); // 9.0</code></pre>

<div class="callout callout-clave">
  <strong>Clave:</strong> <code>&lt;T extends Number&gt;</code> permite usar los metodos de
  <code>Number</code> (como <code>doubleValue()</code>) dentro de la clase. Sin el bounded type,
  T seria <code>Object</code> y no tendrias acceso a esos metodos.
</div>

<!-- ==================== 12. WRAPPERS NUMERICOS ==================== -->
<div class="page-break"></div>
<h1 class="section">12. Wrappers numericos: casteo entre primitivos y objetos</h1>

<h2>Los tipos wrapper</h2>

<p>Para usar generics con numeros, necesitas los <strong>wrappers</strong> (clases envolventes),
porque los generics no aceptan tipos primitivos:</p>

<table>
  <tr><th>Primitivo</th><th>Wrapper</th></tr>
  <tr><td><code>int</code></td><td><code>Integer</code></td></tr>
  <tr><td><code>float</code></td><td><code>Float</code></td></tr>
  <tr><td><code>double</code></td><td><code>Double</code></td></tr>
  <tr><td><code>long</code></td><td><code>Long</code></td></tr>
  <tr><td><code>byte</code></td><td><code>Byte</code></td></tr>
  <tr><td><code>short</code></td><td><code>Short</code></td></tr>
</table>

<h2>Autoboxing y casting explicito</h2>

<pre><code>Byte byte1 = 127;            // autoboxing: byte -> Byte
Short short1 = 5;            // autoboxing: short -> Short
long long0 = 5;              // primitivo long
Long long1 = (long) 5;       // cast explicito: int -> long -> Long</code></pre>

<h2>Por que <code>(byte) 127</code> en <code>suma2.ejecuta(8L, (byte) 127)</code>?</h2>

<pre><code>suma2.ejecuta(8L, (byte) 127)
               |         |
               |         +-- literal 127 es int, hay que castearlo a byte
               +-- literal con L indica tipo long

Sin el cast, 127 seria Integer y no coincidiria con Byte.</code></pre>

<div class="callout callout-nota">
  <strong>Nota:</strong> Los generics solo trabajan con objetos (clases), no con primitivos.
  Java hace autoboxing automaticamente en la mayoria de los casos, pero a veces necesitas
  un cast explicito para que el compilador elija el wrapper correcto.
</div>

<!-- ==================== 13. METODOS GENERICOS ==================== -->
<div class="page-break"></div>
<h1 class="section">13. Metodos genericos estaticos</h1>

<h2>Un metodo con su propio parametro de tipo</h2>

<p>No solo las clases e interfaces pueden ser genericas. Un <strong>metodo individual</strong>
puede declarar su propio parametro de tipo:</p>

<pre><code>class Alumno {{

    static public &lt;V&gt; V getMatricula(V v) {{
        System.out.println("Mostrar matricula: " + v);
        return v;
    }}
}}</code></pre>

<h2>Donde va el <code>&lt;V&gt;</code></h2>

<pre><code>static public &lt;V&gt; V getMatricula(V v)
              |   |               |
              |   |               +-- parametro de tipo V
              |   +-- tipo de retorno: V (mismo tipo que entra, sale)
              +-- declaracion del parametro de tipo</code></pre>

<h2>Uso: el tipo se infiere automaticamente</h2>

<pre><code>Alumno.getMatricula("XYZ100");                                    // V = String
Alumno.&lt;StringBuilder&gt;getMatricula(new StringBuilder("WER890"));  // V = StringBuilder
Alumno.getMatricula(new Object());                                // V = Object
Alumno.&lt;Double&gt;getMatricula(Math.random());                       // V = Double</code></pre>

<h2>Inferencia vs tipo explicito</h2>

<table>
  <tr><th>Llamada</th><th>V inferido</th><th>Forma</th></tr>
  <tr><td><code>getMatricula("XYZ100")</code></td><td>String</td><td>Inferencia automatica</td></tr>
  <tr><td><code>&lt;StringBuilder&gt;getMatricula(...)</code></td><td>StringBuilder</td><td>Tipo explicito con <code>&lt;&gt;</code></td></tr>
  <tr><td><code>getMatricula(new Object())</code></td><td>Object</td><td>Inferencia automatica</td></tr>
  <tr><td><code>&lt;Double&gt;getMatricula(Math.random())</code></td><td>Double</td><td>Tipo explicito con <code>&lt;&gt;</code></td></tr>
</table>

<div class="callout callout-clave">
  <strong>Clave:</strong> En un metodo generico, el parametro de tipo (<code>&lt;V&gt;</code>) se declara
  <strong>antes</strong> del tipo de retorno. El compilador infiere el tipo automaticamente en la mayoria
  de los casos, pero puedes especificarlo explicitamente con <code>Clase.&lt;Tipo&gt;metodo(...)</code>.
</div>

<!-- ==================== 14. DONDE SE DECLARAN ==================== -->
<div class="page-break"></div>
<h1 class="section">14. Donde se declaran los generics</h1>

<h2>Tres niveles de generics</h2>

<table>
  <tr><th>Nivel</th><th>Donde se declara</th><th>Ejemplo</th><th>Alcance</th></tr>
  <tr><td><strong>Interface</strong></td><td>Despues del nombre</td><td><code>interface Operacion&lt;T,U,W&gt;</code></td><td>Toda la interfaz</td></tr>
  <tr><td><strong>Clase</strong></td><td>Despues del nombre</td><td><code>class Suma&lt;T extends Number&gt;</code></td><td>Toda la clase</td></tr>
  <tr><td><strong>Metodo</strong></td><td>Antes del retorno</td><td><code>&lt;V&gt; V getMatricula(V v)</code></td><td>Solo ese metodo</td></tr>
</table>

<h2>Generics en colecciones vs propios</h2>

<table>
  <tr><th>Aspecto</th><th>Colecciones (java.util)</th><th>Propios (tu codigo)</th></tr>
  <tr><td>Quien los define</td><td>Java (ArrayList, HashMap...)</td><td>Tu</td></tr>
  <tr><td>Ejemplo</td><td><code>List&lt;String&gt;</code></td><td><code>Operacion&lt;Integer,Float,Double&gt;</code></td></tr>
  <tr><td>Proposito</td><td>Tipar el contenido</td><td>Tipar parametros/retorno</td></tr>
  <tr><td>Wildcard <code>&lt;?&gt;</code></td><td>Muy comun</td><td>Menos comun</td></tr>
</table>

<!-- ==================== 15. ARRAYS A LIST ==================== -->
<div class="page-break"></div>
<h1 class="section">15. Conversion de arrays a List con generics</h1>

<h2>Arrays.asList() y generics</h2>

<pre><code>String[] names = {{"Patrobas", "Andronico", "Filologo", "Epeneto"}};

// Opcion 1: List&lt;Object&gt; desde un array de String
List&lt;Object&gt; lista = new ArrayList&lt;&gt;(Arrays.asList(names));
System.out.println(lista);  // [Patrobas, Andronico, Filologo, Epeneto]</code></pre>

<h2>La restriccion de invariancia aplica aqui tambien</h2>

<pre><code>List&lt;String&gt; listaNames = new ArrayList&lt;&gt;();
listaNames.add("Patrobas");

// List&lt;Object&gt; listaObject = listaNames;   // NO COMPILA (invariancia)</code></pre>

<h2>Para convertir, necesitas un new ArrayList</h2>

<pre><code>// Esto SI funciona: crear una nueva lista copiando elementos
List&lt;Object&gt; lista = new ArrayList&lt;&gt;(Arrays.asList(names));</code></pre>

<div class="callout callout-nota">
  <strong>Nota:</strong> <code>Arrays.asList()</code> crea una lista de tamanio fijo (no puedes hacer
  <code>add()</code> ni <code>remove()</code>). Por eso la envolvemos en <code>new ArrayList&lt;&gt;(...)</code>
  para obtener una lista modificable.
</div>

<!-- ==================== 16. RESUMEN ==================== -->
<div class="page-break"></div>
<h1 class="resumen">Resumen de conceptos clave</h1>

<table>
  <tr><th>Concepto</th><th>Descripcion</th></tr>
  <tr><td>Raw type</td><td><code>List</code> sin <code>&lt;&gt;</code>. Acepta cualquier objeto, errores en runtime</td></tr>
  <tr><td><code>List&lt;Tipo&gt;</code></td><td>Lista tipada. Errores se detectan en compilacion</td></tr>
  <tr><td>ClassCastException</td><td>Error en runtime al hacer cast incorrecto (evitable con generics)</td></tr>
  <tr><td>Pattern Matching</td><td><code>instanceof Pato p</code> verifica tipo y castea en una expresion (Java 14+)</td></tr>
  <tr><td>Invariancia</td><td><code>List&lt;Pato&gt;</code> NO es <code>List&lt;Animal&gt;</code> aunque Pato extienda Animal</td></tr>
  <tr><td><code>List&lt;?&gt;</code></td><td>Unbounded Wildcard. Acepta lista de cualquier tipo, pero solo lectura</td></tr>
  <tr><td><code>&lt;T&gt;</code></td><td>Parametro de tipo en clase o interfaz generica</td></tr>
  <tr><td><code>&lt;T extends Number&gt;</code></td><td>Upper bounded type. Restringe T a Number y sus subtipos</td></tr>
  <tr><td><code>&lt;V&gt; V metodo(V v)</code></td><td>Metodo generico estatico. Declara su propio parametro de tipo</td></tr>
  <tr><td>Autoboxing</td><td>Conversion automatica de primitivo a wrapper (<code>int</code> a <code>Integer</code>)</td></tr>
  <tr><td>Wrapper</td><td>Clase envolvente: Integer, Double, Long, Byte, Short, Float</td></tr>
  <tr><td><code>Arrays.asList()</code></td><td>Convierte un array en una lista de tamanio fijo</td></tr>
</table>

<!-- ==================== 17. PROGRESION ==================== -->
<div class="page-break"></div>
<h2>Progresion de los ejercicios del dia</h2>

<table>
  <tr><th>Proyecto</th><th>Paquete</th><th>Version</th><th>Tema</th></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v0</td><td>Raw type: lista sin tipo, mezcla cualquier objeto</td></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v1</td><td>instanceof y casting manual con raw types</td></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v2</td><td>ClassCastException sin generics (Animal/Pato/Perico)</td></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v3</td><td><code>List&lt;Tipo&gt;</code> + Pattern Matching Java 14</td></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v4</td><td>Invariancia: <code>List&lt;Pato&gt;</code> no es <code>List&lt;Animal&gt;</code></td></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v5</td><td>Unbounded Wildcard <code>List&lt;?&gt;</code> (solo lectura)</td></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v6</td><td>Unbounded Wildcard acepta <code>List&lt;Object&gt;</code></td></tr>
  <tr><td>Generics</td><td><code>com.curso</code></td><td>v7</td><td>Variante final con cast seguro</td></tr>
  <tr><td>Generics</td><td><code>com.gen</code></td><td>v0</td><td>Interface <code>Operacion&lt;T,U,W&gt;</code> con Suma concreta</td></tr>
  <tr><td>Generics</td><td><code>com.gen</code></td><td>v1</td><td>Upper bounded <code>&lt;T extends Number&gt;</code> en Suma</td></tr>
  <tr><td>Generics</td><td><code>com.gen</code></td><td>v2</td><td>Metodo generico estatico <code>&lt;V&gt; V getMatricula(V v)</code></td></tr>
  <tr><td>Generics</td><td><code>com.gen</code></td><td>v3</td><td>Conversion de arrays a List con generics</td></tr>
</table>

</body>
</html>"""

if __name__ == "__main__":
    output_path = "/Users/mike/Desarrollo/academiafebrero26CDMX/documents/actividadXdia/230226.pdf"
    html = weasyprint.HTML(string=HTML_CONTENT)
    html.write_pdf(output_path)
    print(f"PDF generado: {output_path}")
