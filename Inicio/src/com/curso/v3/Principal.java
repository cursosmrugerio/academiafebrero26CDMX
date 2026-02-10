package com.curso.v3; // Define el paquete donde vive esta clase

// Importa la clase System de java.lang (es opcional porque java.lang se importa automaticamente)
import java.lang.System;

// Clase principal que demuestra la creacion de un objeto String y la salida por consola
public class Principal {

	// Punto de entrada del programa: el JVM busca este metodo para iniciar la ejecucion
	public static void main(String[] args) {

		// Crea un objeto String usando el constructor con 'new' (forma explicita)
		// Tambien se puede crear directamente: String hello = "Hola mundo";
		String hello = new String("Hola mundo");

		// Imprime el contenido del String en la consola seguido de un salto de linea
		System.out.println(hello);
	}

}
