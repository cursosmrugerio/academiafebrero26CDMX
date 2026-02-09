package com.curso.v2A; // Define el paquete donde vive esta clase

// Subclase de Ave: perico que sobreescribe el comportamiento de vuelo
public class Perico extends Ave {

	// Override: redefine volar() con el comportamiento especifico del perico
	void volar() {
		System.out.println("Volar Perico");
	}

}
