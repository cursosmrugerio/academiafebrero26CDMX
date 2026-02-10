package com.curso.v1; // Paquete DIFERENTE al de Aguila (v1 vs v0)

import com.curso.v0.Aguila; // Importa Aguila desde otro paquete

// Hereda de Aguila para demostrar que accesos se permiten desde una SUBCLASE en OTRO paquete
public class Principal extends Aguila {

	public static void main(String[] args) {

		// Crea instancia de Principal (que hereda los campos de Aguila)
		Principal aguila = new Principal();

		// Desde una SUBCLASE en OTRO paquete se puede acceder a:
		System.out.println(aguila.name); // public: SI - accesible desde cualquier lugar
		System.out.println(aguila.real); // protected: SI - accesible desde subclases

		// Estos NO son accesibles desde otro paquete (ni siquiera por herencia):
		//System.out.println(aguila.tipo); // default: NO - solo accesible dentro del mismo paquete
		//System.out.println(aguila.age);  // private: NO - solo accesible dentro de Aguila


	}

}
