package com.curso.v0; // Define el paquete donde vive esta clase

// Subclase de Ave: representa un perico
public class Perico extends Ave {

	// Override de volar(): el perico tiene su propia implementacion de vuelo
	void volar() {
		System.out.println("Volar Perico");
	}

}
