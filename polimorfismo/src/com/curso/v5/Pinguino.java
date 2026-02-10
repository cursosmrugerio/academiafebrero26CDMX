package com.curso.v5; // Define el paquete donde vive esta clase

// Subclase de Ave: pinguino que NO vuela
public class Pinguino implements Ave {

	// Override: redefine volar() indicando que el pinguino no puede volar
	public void volar() {
		System.out.println("No volar Pinguino");
	}

}
