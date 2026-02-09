package com.curso.v3; // Define el paquete donde vive esta clase

// Se importa Random para generar numeros aleatorios
import java.util.Random;

// Ejemplo avanzado: polimorfismo con arreglos y seleccion aleatoria
// Demuestra que el codigo generico funciona con CUALQUIER subclase de Ave,
// incluso las que se agreguen en el futuro
public class Principal {

	public static void main(String[] args) {

		// Se obtiene un Ave aleatoria - no sabemos cual sera hasta tiempo de ejecucion
		Ave ave = getAve();

		// Se pasa al metodo polimorfico: funciona sin importar que tipo de Ave sea
		comportamientoVolar(ave);

	}

	// Metodo que acepta cualquier Ave y ejecuta su comportamiento de vuelo
	static void comportamientoVolar(Ave ave) {
		// Java resuelve en tiempo de ejecucion cual volar() invocar (dynamic dispatch)
		ave.volar();
	}

	// Metodo privado que retorna un Ave aleatoria de un arreglo polimorfico
	private static Ave getAve() {

		// Arreglo de tipo Ave[] que contiene diferentes subclases mezcladas
		// Esto es posible gracias al polimorfismo: todas IS-A Ave
		Ave[] aves = {new Pato(),
					  new Ave(),
					  new Murcielago(),
					  new Perico(),
					  new Pinguino()
		};

		// Se genera un indice aleatorio entre 0 y aves.length-1
		int aleatorio = new Random().nextInt(aves.length);

		// Se retorna el Ave en la posicion aleatoria
		// El tipo de retorno es Ave, pero el objeto real puede ser cualquier subclase
		return aves[aleatorio];
	}

}
