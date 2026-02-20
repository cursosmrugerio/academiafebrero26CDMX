package com.curso.v0;

// v0: Hilos con extends Thread
// Punto clave: start() crea un hilo nuevo, run() NO lo crea
public class Principal {

	public static void main(String[] args) {

		System.out.println("Hilo principal: " + Thread.currentThread().getName());

		MiHilo hilo1 = new MiHilo("Hilo-A", 5);
		MiHilo hilo2 = new MiHilo("Hilo-B", 5);

		// start() lanza un nuevo hilo de ejecucion
		hilo1.start();
		hilo2.start();

		// Error comun: llamar run() directamente NO crea un hilo nuevo
		// hilo1.run(); // esto se ejecutaria en el hilo main, no en uno nuevo

		System.out.println("Main continua ejecutandose...");
	}
}
