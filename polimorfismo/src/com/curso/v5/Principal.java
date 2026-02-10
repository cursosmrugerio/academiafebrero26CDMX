package com.curso.v5; // Define el paquete donde vive esta clase

// Se importa Random para generar numeros aleatorios
import java.util.Random;


public class Principal {

	public static void main(String[] args) {
		System.out.println("Interface");
		Ave ave = getAve();

		comportamientoVolar(ave);

	}

	static void comportamientoVolar(Ave ave) {
		ave.volar();
	}

	// Metodo privado que retorna un Ave aleatoria de un arreglo polimorfico
	private static Ave getAve() {

		// Arreglo de tipo Ave[] que contiene diferentes subclases mezcladas
		// Esto es posible gracias al polimorfismo: todas IS-A Ave
		Ave[] aves = {new Pato(),
					  //new Ave(), //MAL
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
