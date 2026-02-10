package com.curso.v0; // Mismo paquete que Aguila (com.curso.v0)

// Clase que demuestra el acceso a campos desde el MISMO PAQUETE (sin herencia)
public class OtroPrincipal {

	public static void main(String[] args) {

		// Crea una instancia de Aguila (misma clase, mismo paquete)
		Aguila aguila = new Aguila();

		// Desde el MISMO paquete se puede acceder a:
		System.out.println(aguila.name);  // public: SI - accesible desde cualquier lugar
		System.out.println(aguila.real);  // protected: SI - accesible desde el mismo paquete
		System.out.println(aguila.tipo);  // default: SI - accesible desde el mismo paquete

		// private: NO - solo accesible dentro de la propia clase Aguila
		//System.out.println(aguila.age); // Error de compilacion: age tiene acceso private


	}

}
