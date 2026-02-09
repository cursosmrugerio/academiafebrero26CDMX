package com.curso.v0; // Define el paquete donde vive esta clase

// Subclase de Ave: representa un pato
// 'extends Ave' establece la relacion de herencia IS-A (Pato "es un" Ave)
public class Pato extends Ave {

	// Override (sobreescritura) del metodo volar() de Ave
	// Cuando se invoque volar() sobre un objeto Pato, se ejecutara ESTA version
	void volar() {
		System.out.println("Volar Pato");
	}

}
