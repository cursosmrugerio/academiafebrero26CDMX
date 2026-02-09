package com.curso.v1; // Define el paquete donde vive esta clase

// Se importa Random para seleccionar un ave aleatoria
import java.util.Random;

// Demuestra casting SEGURO usando instanceof antes de hacer downcast
// Evita ClassCastException validando el tipo real del objeto
public class Principal {

	public static void main(String[] args) {

		// Se obtiene un Ave aleatoria (puede ser Pato, Perico, Pinguino, etc.)
		Ave ave = getAve();

		// Se pasa al metodo que maneja el comportamiento de vuelo
		comportamientoVolar(ave);

	}

	// Metodo que ejecuta volar() y, SI es Pato, tambien volarPato()
	static void comportamientoVolar(Ave ave) {
		// Primero se invoca volar() que funciona para cualquier Ave (polimorfismo)
		ave.volar();

		// CASTING SEGURO: se verifica con instanceof si el objeto es realmente un Pato
		// Solo si es Pato, se hace el downcast para acceder a volarPato()
		// Si no es Pato, simplemente se salta el if - sin error
		if (ave instanceof Pato)
			((Pato)ave).volarPato(); // Downcast seguro: ya sabemos que ES un Pato
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

		// Genera un indice aleatorio entre 0 y 4
		int aleatorio = new Random().nextInt(aves.length);

		// Retorna el Ave seleccionada aleatoriamente
		return aves[aleatorio];
	}

}
