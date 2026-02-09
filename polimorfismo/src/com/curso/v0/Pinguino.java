package com.curso.v0; // Define el paquete donde vive esta clase

// Subclase de Ave: representa un pinguino
// Demuestra que una subclase puede tener comportamiento DIFERENTE al padre
public class Pinguino extends Ave {

	// Override de volar(): el pinguino NO vuela, cambiando el comportamiento base
	// Esto es valido en OOP: la subclase redefine el metodo segun su naturaleza
	void volar() {
		System.out.println("No vuelar Pinguino");
	}

}
