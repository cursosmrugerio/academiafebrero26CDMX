package com.curso.v4; // Define el paquete donde vive esta clase

// Subclase de Ave: murcielago (nueva subclase agregada en v3)
// Demuestra la extensibilidad del diseno polimorfico: se agrega un nuevo tipo
// sin modificar el codigo existente (principio Open/Closed)
public class Murcielago extends Ave {

	// Override: redefine volar() con el comportamiento del murcielago
	void volar() {
		System.out.println("Volar Murcielago");
	}

}
