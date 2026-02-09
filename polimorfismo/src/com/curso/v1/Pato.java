package com.curso.v1; // Define el paquete donde vive esta clase

// Subclase de Ave: pato que sobreescribe el comportamiento de vuelo
public class Pato extends Ave {

	// Override: redefine volar() con el comportamiento especifico del pato
	void volar() {
		System.out.println("Volar Pato");
	}

}
