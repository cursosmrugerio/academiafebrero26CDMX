package com.curso.v5; // Define el paquete donde vive esta clase

// Subclase de Ave: pato que sobreescribe el comportamiento de vuelo
public class Pato implements Ave {

	// Override: redefine volar() con el comportamiento especifico del pato
	public void volar() {
		System.out.println("Volar Pato");
	}

}
