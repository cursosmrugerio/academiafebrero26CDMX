package com.curso.v0; // Define el paquete donde vive esta clase

// Subclase de Ave: pato con un metodo EXCLUSIVO (volarPato)
// Este metodo no existe en Ave, por lo que se necesita CAST para invocarlo
// desde una referencia de tipo Ave
public class Pato extends Ave {

	// Override del metodo volar() heredado de Ave
	void volar() {
		System.out.println("Pato Volar");
	}

	// Metodo EXCLUSIVO de Pato: no existe en la clase padre Ave
	// Solo se puede invocar desde una referencia de tipo Pato (no Ave)
	// Si tenemos una referencia Ave, necesitamos hacer DOWNCAST a Pato primero
	void volarPato() {
		System.out.println("volarPato()");
	}

}
