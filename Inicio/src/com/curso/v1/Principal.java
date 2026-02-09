package com.curso.v1; // Define el paquete donde vive esta clase

// Clase que demuestra la diferencia entre objetos mutables e inmutables
// y como se comporta el paso de parametros en Java (siempre por valor)
public class Principal {

	public static void main(String[] args) {

		// Variable primitiva: se almacena directamente en el stack con valor 10
		int x = 10;
		// String es un objeto INMUTABLE: una vez creado, su contenido no puede cambiar
		String cadena = "Hello";
		// StringBuilder es un objeto MUTABLE: su contenido puede modificarse despues de creado
		StringBuilder sb = new StringBuilder("Hola");

		// Se pasa una COPIA del valor de x, una COPIA de la referencia de cadena,
		// y una COPIA de la referencia de sb al metodo show()
		show(x,cadena, sb);

		// x sigue siendo 10: el metodo modifico su copia local, no la original
		System.out.println(x);  //10
		// cadena sigue siendo "Hello": concat() crea un NUEVO String pero nadie lo captura
		// porque String es INMUTABLE, el original nunca cambia
		System.out.println(cadena); //Hello World
		// sb ahora es "Hola Mundo": append() modifico el MISMO objeto en memoria
		// porque StringBuilder es MUTABLE y ambas referencias apuntan al mismo objeto
		System.out.println(sb); //Hola Mundo

	}

	// Metodo estatico que recibe copias de los valores/referencias
	static void  show(int x, String cadena, StringBuilder sb) {
		// Modifica la copia local de x (la original no se afecta)
		x+=10;
		// concat() genera un nuevo String "Hello World", pero el resultado se PIERDE
		// porque no se asigna a ninguna variable - el String original no cambia (INMUTABLE)
		cadena.concat(" World"); //INMUTABLE
		// append() modifica el objeto StringBuilder original directamente en memoria
		// porque StringBuilder es MUTABLE - el cambio SI se ve fuera del metodo
		sb.append(" Mundo"); //MUTABLE
	}

}
