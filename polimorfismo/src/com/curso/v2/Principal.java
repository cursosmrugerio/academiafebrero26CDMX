package com.curso.v2; // Define el paquete donde vive esta clase

// Evolucion de v1: demuestra polimorfismo a traves de PARAMETROS de metodo
// Un solo metodo puede recibir cualquier subclase de Ave
public class Principal {

	public static void main(String[] args) {

		// Se pasan diferentes subclases al mismo metodo comportamientoVolar()
		// Cada objeto ejecutara su propia version de volar() (dispatch dinamico)
		comportamientoVolar(new Pato());      // Ejecuta: "Volar Pato"
		comportamientoVolar(new Pinguino());   // Ejecuta: "No vuelar Pinguino"
		comportamientoVolar(new Ave());        // Ejecuta: "Volar Ave"
		comportamientoVolar(new Perico());     // Ejecuta: "Volar Perico"

	}

	// Metodo que acepta CUALQUIER Ave (o subclase) como parametro
	// Este es el poder del polimorfismo: un solo metodo maneja multiples tipos
	static void comportamientoVolar(Ave ave) {
		// Java decide en tiempo de ejecucion cual version de volar() invocar
		// segun el tipo REAL del objeto (no el tipo de la variable)
		ave.volar();
	}

}
