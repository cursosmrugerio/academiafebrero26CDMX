package com.curso.v2A; // Define el paquete donde vive esta clase

// Se importa Random para seleccionar un ave aleatoria
import java.util.Random;

// ANTI-PATRON: demuestra lo que NO se debe hacer
// Hace downcast SIN verificar con instanceof, causando ClassCastException
// Este es un CONTRAEJEMPLO educativo de v1 y v2
public class Principal {

	public static void main(String[] args) {

		// Se obtiene un Ave aleatoria (puede ser cualquier subclase)
		Ave ave = getAve();

		// Se pasa al metodo que hace cast INSEGURO
		comportamientoVolar(ave);

	}

	static void comportamientoVolar(Ave ave) {
		// volar() funciona bien con polimorfismo
		ave.volar();
		// PELIGRO: se hace downcast a Pato SIN verificar el tipo con instanceof
		// Si getAve() retorna Perico, Murcielago, Pinguino o Ave, esta linea
		// LANZA ClassCastException en tiempo de ejecucion
		// La forma correcta es usar instanceof ANTES (ver v1) o Pattern Matching (ver v2)
		((Pato)ave).volarPato(); //ClassCastExcpetion
	}

	// Retorna un Ave aleatoria de un arreglo polimorfico
	private static Ave getAve() {

		// Arreglo con diferentes subclases - solo 1 de 5 es Pato
		// Hay 80% de probabilidad de ClassCastException
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
