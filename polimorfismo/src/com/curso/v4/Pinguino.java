package com.curso.v4; // Define el paquete donde vive esta clase

// Subclase de Ave: pinguino que NO vuela
public class Pinguino extends Ave {

	// Override: redefine volar() indicando que el pinguino no puede volar
	void volar() {
		System.out.println("No volar Pinguino");
	}

}
