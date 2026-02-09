package com.curso.v0; // Define el paquete donde vive esta clase

// Clase PADRE: ave generica
// El metodo volarPato() esta comentado para demostrar que NO pertenece a Ave
// sino exclusivamente a Pato - esto motiva el uso de casting
public class Ave {

	// Metodo de vuelo generico disponible para Ave y todas sus subclases
	void volar() {
		System.out.println("Ave Volar");
	}

	// Comentado a proposito: si se descomenta, no seria necesario hacer cast
	// El objetivo es que volarPato() SOLO exista en Pato para ensenar downcasting
//	void volarPato() {
//		System.out.println("volarPato()");
//	}

}
