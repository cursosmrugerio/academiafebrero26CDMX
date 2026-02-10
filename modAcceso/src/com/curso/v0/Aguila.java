package com.curso.v0; // Define el paquete donde vive esta clase

// Clase que demuestra los 4 niveles de modificadores de acceso en Java
public class Aguila {

	// PUBLIC: accesible desde cualquier clase, paquete o subclase
	public String name = "America";
	// PRIVATE: accesible SOLO dentro de esta clase (ni subclases ni mismo paquete)
	private int age;

	// PROTECTED: accesible desde el mismo paquete Y desde subclases (incluso en otros paquetes)
	protected boolean real = true;

	// DEFAULT (package-private): sin modificador, accesible solo desde el mismo paquete
	String tipo;

}
