package com.curso.v3; // Define el paquete donde vive esta clase

// Clase PADRE: ave generica con comportamiento de vuelo por defecto
public class Ave {

	// Metodo base que las subclases pueden sobreescribir (override)
	void volar() {
		System.out.println("Volar Ave");
	}

}
