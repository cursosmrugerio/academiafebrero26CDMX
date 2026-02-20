package com.curso.v5;

// v5: Race condition - dos hilos incrementan el mismo contador
// El resultado esperado es 20000, pero casi nunca lo sera
// Esto motiva el tema de sincronizacion (synchronized, locks, etc.)
public class Principal {

	public static void main(String[] args) throws InterruptedException {

		Contador contador = new Contador(); // recurso COMPARTIDO

		Thread hilo1 = new Thread(() -> {
			for (int i = 0; i < 10_000; i++) {
				contador.incrementar();
			}
		});

		Thread hilo2 = new Thread(() -> {
			for (int i = 0; i < 10_000; i++) {
				contador.incrementar();
			}
		});

		hilo1.start();
		hilo2.start();

		hilo1.join();
		hilo2.join();

		// Resultado esperado: 20,000
		// Resultado real: casi siempre MENOR a 20,000
		System.out.println("Resultado esperado: 20000");
		System.out.println("Resultado real:     " + contador.getValor());

		if (contador.getValor() != 20_000) {
			System.out.println("HAY UN PROBLEMA! Los hilos se pisaron entre si.");
			System.out.println("Esto se llama RACE CONDITION.");
			System.out.println("Solucion: synchronized (siguiente tema)");
		} else {
			System.out.println("Salio correcto esta vez, pero NO esta garantizado.");
			System.out.println("Ejecuta varias veces y veras el error.");
		}
	}
}
