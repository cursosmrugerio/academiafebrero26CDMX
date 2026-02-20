package com.curso.v0A;

// v0: Hilos con extends Thread
// Punto clave: start() crea un hilo nuevo, run() NO lo crea
public class Principal {

	public static void main(String[] args) throws InterruptedException {

		//System.out.println("main: Inicio Programa");
		System.out.println("Hilo principal: " + Thread.currentThread().getName());

		MiHilo hilo1 = new MiHilo("Hilo1", 5);
		MiHilo hilo2 = new MiHilo("Hilo2", 8);

		// start() lanza un nuevo hilo de ejecucion
		hilo1.start();
		hilo2.start();

		// Error comun: llamar run() directamente NO crea un hilo nuevo
		// hilo1.run(); // esto se ejecutaria en el hilo main, no en uno nuevo
		
		//Hilo main que se espere hasta que terminen
		//hilo1 e hilo2
		hilo1.join();
		hilo2.join();

		System.out.println("Main termina de ejecutarse");
		//System.out.println("main: Fin de Programa");
	}
}
