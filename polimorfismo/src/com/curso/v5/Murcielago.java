package com.curso.v5; // Define el paquete donde vive esta clase

// Subclase de Ave: murcielago (nueva subclase agregada en v3)
// Demuestra la extensibilidad del diseno polimorfico: se agrega un nuevo tipo
// sin modificar el codigo existente (principio Open/Closed)
public class Murcielago implements Ave {

	// Override: redefine volar() con el comportamiento del murcielago
	public void volar() {
		System.out.println("Volar Murcielago");
	}

}
