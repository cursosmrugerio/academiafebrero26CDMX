package com.curso.v2; // Define el paquete donde vive esta clase

// Evolucion de v1: muestra como manejar correctamente objetos inmutables
// usando valores de retorno en lugar de intentar modificarlos directamente
public class Principal {

	public static void main(String[] args) {

		// Variable primitiva con valor 10
		int x = 10;
		// String inmutable con valor "Hello"
		String cadena = "Hello";
		// StringBuilder mutable con valor "Hola"
		StringBuilder sb = new StringBuilder("Hola");

		// CLAVE: ahora se CAPTURA el valor de retorno del metodo
		// La referencia 'cadena' se reasigna al nuevo String devuelto por show()
		// Esta es la forma correcta de trabajar con objetos inmutables
		cadena = show(x,cadena, sb);

		// x sigue siendo 10: los primitivos se pasan por valor (copia)
		System.out.println(x);  //10
		// cadena ahora SI es "Hello World": se reasigno con el retorno de show()
		System.out.println(cadena); //Hello World
		// sb ahora es "Hola Mundo": StringBuilder es mutable, se modifico directamente
		System.out.println(sb); //Hola Mundo

	}

	// Ahora retorna String en lugar de void - este es el cambio clave vs v1
	static String show(int x, String cadena, StringBuilder sb) {
		// Modifica solo la copia local de x
		x+=10;
		// append() modifica el StringBuilder directamente (mutable)
		sb.append(" Mundo"); //MUTABLE
		// concat() crea un NUEVO String "Hello World" y lo RETORNA
		// El metodo que llama debe capturar este retorno para no perder el resultado
		return cadena.concat(" World"); //INMUTABLE
	}

}
