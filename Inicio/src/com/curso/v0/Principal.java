package com.curso.v0; // Define el paquete donde vive esta clase

// Clase principal que demuestra la creacion de objetos y tipos primitivos
public class Principal {

	// Punto de entrada del programa - la JVM busca este metodo para iniciar
	public static void main(String[] args) {

		// --- POO (Programacion Orientada a Objetos) ---
		// Se crea una instancia de Pato usando el operador 'new'
		// 'pato1' es una variable de referencia que apunta al objeto Pato en memoria (heap)
		Pato pato1 = new Pato();
		// Si descomentamos la siguiente linea, pato1 apuntaria a null (ninguna direccion)
		//pato1 = null;
		// Se invoca el metodo volar() sobre el objeto pato1
		// Si pato1 fuera null, esta linea lanzaria NullPointerException
		pato1.volar(); //NullPointerException

		// --- PRIMITIVOS ---
		// 'int' es un tipo primitivo, no es un objeto, se almacena en el stack
		// Se declara pero no se inicializa - no se puede usar hasta asignarle un valor
		int x;
		System.out.println("End Program: ");

	}

}
