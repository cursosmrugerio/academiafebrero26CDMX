#!/usr/bin/env python3
"""
Generador de la guia PDF para alumnos - Semana 01 (09 Feb 2026)
Curso de Java: Fundamentos de OOP
"""

from fpdf import FPDF
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "guia_semana01_090226.pdf")


class GuiaPDF(FPDF):

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "Curso de Java - Fundamentos de OOP", align="L")
        self.cell(0, 8, "Semana 01 | 09 Feb 2026", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(41, 128, 185)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Pagina {self.page_no()}/{{nb}}", align="C")

    def titulo_seccion(self, numero, titulo):
        self.add_page()
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(41, 128, 185)
        self.cell(0, 14, f"{numero}. {titulo}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(41, 128, 185)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

    def subtitulo(self, texto):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(52, 73, 94)
        self.ln(4)
        self.cell(0, 10, texto, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def parrafo(self, texto):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6, texto)
        self.ln(2)

    def concepto_clave(self, titulo, descripcion):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(41, 128, 185)
        self.cell(0, 7, f"  {titulo}", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, f"     {descripcion}")
        self.ln(2)

    def codigo(self, texto):
        self.set_font("Courier", "", 9)
        self.set_fill_color(245, 245, 245)
        self.set_text_color(30, 30, 30)
        self.set_draw_color(200, 200, 200)
        x = self.get_x()
        y = self.get_y()
        lines = texto.strip().split("\n")
        h = len(lines) * 5 + 6
        if y + h > 270:
            self.add_page()
            y = self.get_y()
        self.rect(12, y, 186, h)
        self.set_xy(14, y + 3)
        for line in lines:
            self.cell(0, 5, line, new_x="LMARGIN", new_y="NEXT")
            self.set_x(14)
        self.set_xy(10, y + h + 3)

    def nota(self, texto):
        self.set_fill_color(255, 243, 205)
        self.set_draw_color(255, 193, 7)
        y = self.get_y()
        self.rect(12, y, 186, 14, style="DF")
        self.set_xy(16, y + 2)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(133, 100, 4)
        self.cell(8, 5, "!")
        self.set_font("Helvetica", "", 10)
        self.multi_cell(170, 5, texto)
        self.set_xy(10, y + 16)

    def tabla_variables(self, headers, rows):
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(41, 128, 185)
        self.set_text_color(255, 255, 255)
        col_widths = [190 / len(headers)] * len(headers)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, fill=True, align="C")
        self.ln()
        self.set_font("Courier", "", 9)
        self.set_text_color(30, 30, 30)
        fill = False
        for row in rows:
            if fill:
                self.set_fill_color(240, 248, 255)
            else:
                self.set_fill_color(255, 255, 255)
            for i, val in enumerate(row):
                self.cell(col_widths[i], 6, str(val), border=1, fill=True, align="C")
            self.ln()
            fill = not fill
        self.ln(3)


def crear_guia():
    pdf = GuiaPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # --- PORTADA ---
    pdf.add_page()
    pdf.ln(35)
    pdf.set_font("Helvetica", "B", 32)
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 16, "Guia de Repaso", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 20)
    pdf.set_text_color(52, 73, 94)
    pdf.cell(0, 12, "Fundamentos de Java y OOP", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(1)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(10)
    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "Semana 01 - Lunes 09 de Febrero de 2026", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, "Academia Java - Ciudad de Mexico", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)

    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(52, 73, 94)
    pdf.cell(0, 8, "Temas del dia:", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    temas = [
        "1. Clases, objetos y tipos primitivos",
        "2. Mutabilidad: String vs StringBuilder",
        "3. Variables static",
        "4. Garbage Collector y referencias",
        "5. Polimorfismo y herencia",
        "6. Casting: upcasting, downcasting e instanceof",
    ]
    pdf.set_font("Helvetica", "", 12)
    for t in temas:
        pdf.cell(0, 8, t, align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(15)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 8, "Instructor: Miguel Rugerio", align="C", new_x="LMARGIN", new_y="NEXT")

    # ==========================================================
    # SECCION 1: INICIO - Clases, objetos y primitivos
    # ==========================================================
    pdf.titulo_seccion("1", "Clases, Objetos y Tipos Primitivos")
    pdf.parrafo(
        "En Java existen dos grandes categorias de datos: los tipos primitivos (int, boolean, "
        "char, etc.) que se almacenan directamente en el stack, y los objetos que se crean en "
        "el heap usando el operador 'new'."
    )

    pdf.subtitulo("Proyecto: Inicio / v0")
    pdf.parrafo(
        "Se creo la clase Pato con un metodo volar() y una clase Principal que instancia el "
        "objeto y lo invoca. Este es el ejemplo mas basico de Programacion Orientada a Objetos."
    )

    pdf.concepto_clave(
        "Operador new",
        "Reserva memoria en el heap y ejecuta el constructor. La variable guarda la REFERENCIA "
        "(direccion) al objeto, no el objeto en si."
    )
    pdf.concepto_clave(
        "NullPointerException",
        "Si una referencia apunta a null y se intenta invocar un metodo sobre ella, Java lanza "
        "esta excepcion en tiempo de ejecucion."
    )

    pdf.codigo(
        'Pato pato1 = new Pato();   // Se crea el objeto en el heap\n'
        'pato1.volar();              // Imprime "Pato vuela"\n'
        '// pato1 = null;\n'
        '// pato1.volar();           // NullPointerException!'
    )

    pdf.subtitulo("Primitivos vs Objetos")

    pdf.tabla_variables(
        ["Caracteristica", "Primitivos (int)", "Objetos (Pato)"],
        [
            ["Almacenamiento", "Stack", "Heap"],
            ["Contiene", "El valor directo", "Una referencia"],
            ["Valor default", "0 (si es campo)", "null"],
            ["Puede ser null?", "No", "Si"],
        ],
    )

    # ==========================================================
    # SECCION 2: MUTABILIDAD
    # ==========================================================
    pdf.titulo_seccion("2", "Mutabilidad: String vs StringBuilder")
    pdf.parrafo(
        "Un concepto fundamental en Java: algunos objetos son INMUTABLES (no se pueden "
        "modificar despues de creados) y otros son MUTABLES (si se pueden modificar)."
    )

    pdf.subtitulo("Proyecto: Inicio / v1")
    pdf.parrafo(
        "Se demuestra que String.concat() NO modifica el String original (es inmutable), "
        "mientras que StringBuilder.append() SI modifica el objeto (es mutable). "
        "Los primitivos se pasan por valor, asi que las modificaciones locales no afectan al original."
    )

    pdf.codigo(
        'int x = 10;\n'
        'String cadena = "Hello";\n'
        'StringBuilder sb = new StringBuilder("Hola");\n'
        '\n'
        'show(x, cadena, sb);\n'
        '\n'
        'System.out.println(x);       // 10     (primitivo: copia)\n'
        'System.out.println(cadena);   // Hello  (inmutable: no cambio)\n'
        'System.out.println(sb);       // Hola Mundo (mutable: SI cambio)'
    )

    pdf.nota(
        'String es inmutable: concat() crea un NUEVO String. Si no capturas el retorno, el resultado se pierde.'
    )

    pdf.subtitulo("Proyecto: Inicio / v2 - Solucion correcta")
    pdf.parrafo(
        "La solucion es que el metodo RETORNE el nuevo String y el llamador lo reasigne:"
    )
    pdf.codigo(
        'cadena = show(x, cadena, sb);  // Se captura el retorno\n'
        '// Dentro de show():\n'
        'return cadena.concat(" World"); // Se retorna el nuevo String'
    )

    pdf.subtitulo("Resumen de mutabilidad")
    pdf.tabla_variables(
        ["Tipo", "Mutable?", "concat/append", "Que pasa?"],
        [
            ["int (primitivo)", "N/A", "x += 10", "Solo copia local"],
            ["String", "INMUTABLE", ".concat()", "Crea nuevo objeto"],
            ["StringBuilder", "MUTABLE", ".append()", "Modifica el mismo"],
        ],
    )

    # ==========================================================
    # SECCION 3: STATIC
    # ==========================================================
    pdf.titulo_seccion("3", "Variables Static")
    pdf.parrafo(
        "Una variable static (de clase) pertenece a la CLASE, no a las instancias. "
        "Existe una sola copia compartida por todos los objetos."
    )

    pdf.subtitulo("Proyecto: statico / v0")
    pdf.parrafo(
        "La clase Pato tiene un campo 'static int contador' que se incrementa en cada "
        "constructor. Al crear 3 patos, el contador llega a 3 y las 3 instancias ven ese mismo valor."
    )

    pdf.codigo(
        'public class Pato {\n'
        '    String name;           // Variable de INSTANCIA (cada pato tiene la suya)\n'
        '    static int contador;   // Variable de CLASE (compartida por todos)\n'
        '\n'
        '    Pato(String name) {\n'
        '        this.name = name;\n'
        '        contador++;        // Incrementa el contador global\n'
        '    }\n'
        '}'
    )

    pdf.codigo(
        'new Pato("Donald");   // contador = 1\n'
        'new Pato("Lucas");    // contador = 2\n'
        'new Pato("Feo");      // contador = 3\n'
        'Pato.contador;        // 3 (se accede con el nombre de la CLASE)'
    )

    pdf.subtitulo("Instancia vs Static")
    pdf.tabla_variables(
        ["Caracteristica", "Variable de instancia", "Variable static"],
        [
            ["Pertenece a", "Cada objeto", "La clase"],
            ["Copias", "Una por objeto", "Una sola"],
            ["Acceso", "objeto.campo", "Clase.campo"],
            ["Ejemplo", "pato1.name", "Pato.contador"],
        ],
    )

    # ==========================================================
    # SECCION 4: GARBAGE COLLECTOR
    # ==========================================================
    pdf.titulo_seccion("4", "Garbage Collector y Referencias")
    pdf.parrafo(
        "El Garbage Collector (GC) de Java libera automaticamente la memoria de objetos que "
        "ya no tienen ninguna referencia activa. No necesitas liberar memoria manualmente."
    )

    pdf.subtitulo("Proyecto: gc / v0 - NewClass")
    pdf.parrafo(
        "Se demuestra paso a paso como las referencias cambian y cuando los objetos se "
        "vuelven elegibles para recoleccion:"
    )

    pdf.codigo(
        'Object obj = new Object();    // ObjA creado, ref: obj\n'
        'NewClass tc = new NewClass();  // tc creado\n'
        'tc.doSomething(obj);           // tc.o -> ObjA (2 refs)\n'
        'obj = new Object();            // obj -> ObjB, ObjA aun vivo (tc.o)\n'
        'obj = null;                    // ObjB sin refs -> elegible GC\n'
        'tc.doSomething(null);          // tc.o -> null, ObjA sin refs -> elegible GC'
    )

    pdf.concepto_clave(
        "Regla del GC",
        "Un objeto es elegible para recoleccion cuando NINGUNA variable activa apunta a el, "
        "ni directa ni indirectamente a traves de otros objetos."
    )

    pdf.subtitulo("Proyecto: gc / v0 - TestClass (Nodos enlazados)")
    pdf.parrafo(
        "Un nodo n2 apunta a n1 via n2.next. Aunque anulemos la variable n1, "
        "el objeto sigue vivo porque n2.next lo referencia."
    )

    pdf.subtitulo("Proyecto: gc / v1 - Referencias circulares")
    pdf.parrafo(
        "Se crea un ciclo: n1 -> n3 -> n2 -> n1. La expresion (n1 == n3.next.next) es true "
        "porque recorrer la cadena nos regresa al mismo objeto. En Java, el GC PUEDE recolectar "
        "ciclos (a diferencia de lenguajes con reference counting)."
    )

    pdf.nota(
        "El operador == compara REFERENCIAS (direcciones de memoria), no contenido. "
        "Para comparar contenido de objetos se usa .equals()."
    )

    # ==========================================================
    # SECCION 5: POLIMORFISMO
    # ==========================================================
    pdf.titulo_seccion("5", "Polimorfismo y Herencia")
    pdf.parrafo(
        "Polimorfismo significa 'muchas formas': una referencia de tipo padre puede apuntar "
        "a cualquier objeto hijo, y el metodo que se ejecuta es el del OBJETO REAL, "
        "no el del tipo de la variable. Esto se conoce como dynamic dispatch."
    )

    pdf.subtitulo("Jerarquia de clases")
    pdf.codigo(
        '           Ave (padre)\n'
        '     volar() -> "Volar Ave"\n'
        '        |          |          |           |\n'
        '      Pato      Pinguino    Perico    Murcielago\n'
        '   "Volar     "No volar   "Volar     "Volar\n'
        '    Pato"      Pinguino"   Perico"    Murcielago"'
    )

    pdf.subtitulo("v0 - Polimorfismo basico")
    pdf.parrafo("Una referencia tipo Ave puede apuntar a cualquier subclase:")
    pdf.codigo(
        'Ave ave2 = new Pato();      // Upcasting automatico\n'
        'ave2.volar();                // "Volar Pato" (se ejecuta el del objeto real)'
    )

    pdf.subtitulo("v1 - Una sola variable polimorfica")
    pdf.parrafo("Se reutiliza una sola referencia Ave reasignandola a diferentes subclases:")
    pdf.codigo(
        'Ave ave;\n'
        'ave = new Perico();    ave.volar();  // "Volar Perico"\n'
        'ave = new Pinguino();  ave.volar();  // "No volar Pinguino"\n'
        'ave = new Pato();      ave.volar();  // "Volar Pato"'
    )

    pdf.subtitulo("v2 - Parametros polimorficos")
    pdf.parrafo("Un metodo que recibe Ave funciona con CUALQUIER subclase:")
    pdf.codigo(
        'static void comportamientoVolar(Ave ave) {\n'
        '    ave.volar();  // Java decide en runtime cual version ejecutar\n'
        '}\n'
        'comportamientoVolar(new Pato());      // "Volar Pato"\n'
        'comportamientoVolar(new Pinguino());   // "No volar Pinguino"'
    )

    pdf.subtitulo("v3 - Arreglos polimorficos + Random")
    pdf.parrafo("Un arreglo Ave[] puede contener mezcla de subclases. Se selecciona aleatoriamente:")
    pdf.codigo(
        'Ave[] aves = {new Pato(), new Ave(), new Murcielago(),\n'
        '              new Perico(), new Pinguino()};\n'
        'int aleatorio = new Random().nextInt(aves.length);\n'
        'return aves[aleatorio];  // Retorna cualquier subclase'
    )

    # ==========================================================
    # SECCION 6: CASTING
    # ==========================================================
    pdf.titulo_seccion("6", "Casting: Upcasting, Downcasting e instanceof")
    pdf.parrafo(
        "Casting es convertir una referencia de un tipo a otro dentro de la jerarquia de herencia."
    )

    pdf.subtitulo("Upcasting (automatico y seguro)")
    pdf.parrafo(
        "Asignar un objeto hijo a una referencia padre. Siempre es seguro y automatico:"
    )
    pdf.codigo(
        'Ave ave = new Pato();  // Upcasting: Pato -> Ave (automatico)\n'
        '// Regla: SUPERCLASE = SUBCLASE  (PAPAS = HIJOS)'
    )

    pdf.subtitulo("Downcasting (explicito y riesgoso)")
    pdf.parrafo(
        "Convertir una referencia padre a tipo hijo. Requiere cast explicito y puede fallar:"
    )
    pdf.codigo(
        'Ave ave = new Pato();\n'
        '((Pato)ave).volarPato();  // OK: el objeto real SI es Pato\n'
        '\n'
        'Ave ave2 = new Perico();\n'
        '((Pato)ave2).volarPato(); // ClassCastException! No es Pato'
    )

    pdf.subtitulo("v1 - instanceof (casting seguro)")
    pdf.parrafo("Se verifica el tipo ANTES de hacer cast:")
    pdf.codigo(
        'if (ave instanceof Pato)\n'
        '    ((Pato)ave).volarPato();  // Solo si realmente es Pato'
    )

    pdf.subtitulo("v2 - Pattern Matching (Java 14+)")
    pdf.parrafo("Sintaxis moderna que combina verificacion + cast en una linea:")
    pdf.codigo(
        'if (ave instanceof Pato patito)   // Verifica Y castea\n'
        '    patito.volarPato();            // patito ya es tipo Pato'
    )

    pdf.nota(
        "v2A es un ANTI-PATRON: hacer cast sin instanceof causa ClassCastException "
        "cuando el objeto no es del tipo esperado. Siempre verificar primero."
    )

    pdf.subtitulo("v3 - Reglas de asignacion")
    pdf.tabla_variables(
        ["Asignacion", "Valido?", "Razon"],
        [
            ["B b = new B1()", "SI", "Upcasting (auto)"],
            ["B1 b1 = (B1) b", "Depende", "Downcast (puede fallar)"],
            ["B2 b2 = b1", "NO", "Hermanas, no compatibles"],
        ],
    )

    # ==========================================================
    # SECCION 7: RESUMEN GENERAL
    # ==========================================================
    pdf.titulo_seccion("7", "Resumen del Dia")

    pdf.tabla_variables(
        ["Proyecto", "Tema principal", "Concepto clave"],
        [
            ["Inicio v0", "OOP basico", "new, referencias, NPE"],
            ["Inicio v1", "Mutabilidad", "String inmutable vs SB mutable"],
            ["Inicio v2", "Inmutables", "Capturar valor de retorno"],
            ["statico", "Static", "Variable compartida de clase"],
            ["gc v0", "Garbage Collector", "Elegibilidad por referencias"],
            ["gc v1", "Refs circulares", "GC maneja ciclos"],
            ["polimorfismo v0-v3", "Polimorfismo", "Dynamic dispatch"],
            ["cast v0-v3", "Casting", "instanceof y pattern matching"],
        ],
    )

    pdf.subtitulo("Estructura de los proyectos")
    pdf.parrafo(
        "Cada proyecto esta organizado en versiones (v0, v1, v2...) que evolucionan "
        "el mismo concepto progresivamente. Los archivos fuente estan en src/com/curso/vX/ "
        "y contienen comentarios explicativos en cada linea."
    )

    pdf.subtitulo("Para repasar")
    pdf.parrafo(
        "1. Clona el repositorio y abre los proyectos en Eclipse.\n"
        "2. Ejecuta cada Principal.java version por version.\n"
        "3. Lee los comentarios de cada linea para entender que hace.\n"
        "4. Modifica el codigo y observa como cambia el comportamiento.\n"
        "5. Intenta predecir la salida ANTES de ejecutar."
    )

    pdf.output(OUTPUT_FILE)
    print(f"PDF generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    crear_guia()
