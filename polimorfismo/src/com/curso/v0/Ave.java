package com.curso.v0; // Define el paquete donde vive esta clase

// Clase PADRE (superclase): representa un ave generica
// Sirve como tipo base para que las subclases hereden y sobreescriban su comportamiento
public class Ave {

	// Metodo que define el comportamiento de vuelo por defecto
	// Las subclases pueden sobreescribirlo (override) con su propia implementacion
	void volar() {
		System.out.println("Volar Ave");
	}

}
