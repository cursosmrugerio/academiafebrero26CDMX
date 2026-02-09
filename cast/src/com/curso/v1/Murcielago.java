package com.curso.v1; // Define el paquete donde vive esta clase

// Subclase de Ave: murcielago que sobreescribe el comportamiento de vuelo
public class Murcielago extends Ave {

	// Override: redefine volar() con el comportamiento del murcielago
	void volar() {
		System.out.println("Volar Murcielago");
	}

}
