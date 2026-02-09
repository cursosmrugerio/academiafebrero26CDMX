package com.curso.v2; // Define el paquete donde vive esta clase

// Se importa Random para seleccionar un ave aleatoria
import java.util.Random;

// Evolucion de v1: usa PATTERN MATCHING con instanceof (Java 14+)
// Combina la verificacion de tipo y el cast en una sola expresion
public class Principal {

	public static void main(String[] args) {

		// Se obtiene un Ave aleatoria
		Ave ave = getAve();

		// Se pasa al metodo que maneja el comportamiento de vuelo
		comportamientoVolar(ave);

	}

	static void comportamientoVolar(Ave ave) {
		// Se invoca volar() polimorficamente
		ave.volar();

		// PATTERN MATCHING (Java 14+):
		// 'ave instanceof Pato patito' hace DOS cosas en una linea:
		// 1. Verifica si 'ave' es una instancia de Pato
		// 2. Si es true, crea la variable 'patito' ya casteada a tipo Pato
		// Esto elimina la necesidad del cast explicito ((Pato)ave) de v1
		if (ave instanceof Pato patito) //JAVA 14
			patito.volarPato(); // 'patito' ya es tipo Pato, sin cast manual
	}

	// Retorna un Ave aleatoria de un arreglo polimorfico
	private static Ave getAve() {

		// Arreglo con diferentes subclases de Ave
		Ave[] aves = {new Pato(),
					  new Ave(),
					  new Murcielago(),
					  new Perico(),
					  new Pinguino()
		};

		// Genera un indice aleatorio
		int aleatorio = new Random().nextInt(aves.length);

		return aves[aleatorio];
	}

}
