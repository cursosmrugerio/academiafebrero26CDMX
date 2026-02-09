package com.curso.v2A; // Define el paquete donde vive esta clase

// Subclase de Ave: pato con metodo exclusivo volarPato()
public class Pato extends Ave {

	// Override: redefine volar() con el comportamiento del pato
	void volar() {
		System.out.println("Volar Pato");
	}

	// Metodo EXCLUSIVO de Pato: requiere downcast para invocarse desde referencia Ave
	void volarPato() {
		System.out.println("volarPato()");
	}

}
