package com.curso.v5; // Define el paquete donde vive esta clase

// Subclase de Ave: perico que sobreescribe el comportamiento de vuelo
public class Perico implements Ave {

	// Override: redefine volar() con el comportamiento especifico del perico
	public void volar() {
		System.out.println("Volar Perico");
	}

}
