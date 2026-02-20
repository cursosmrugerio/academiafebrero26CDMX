package com.curso.v1B;

// v1: Hilos con implements Runnable
// Runnable separa la TAREA del MECANISMO de ejecucion (Thread)
public class Principal {

	public static void main(String[] args) {

		System.out.println("Runnable Lambdas v2");
		System.out.println("Hilo principal: " + Thread.currentThread().getName());
		

		// Creamos los hilos y les pasamos la tarea
		Thread hilo1 = new Thread(() -> {
			for (int i = 1; i <= 5; i++) {
				System.out.println("Tarea-A" + " -> " + i);
			}
			System.out.println("Tarea-A" + " termino!");
		});
		
		Thread hilo2 = new Thread(() -> {
			for (int i = 1; i <= 8; i++) {
				System.out.println("Tarea-B" + " -> " + i);
			}
			System.out.println("Tarea-B" + " termino!");
		});

		hilo1.start();
		hilo2.start();

		// Observa: el orden de ejecucion NO es determinista
		// Ejecuta varias veces y veras resultados diferentes
		System.out.println("Main termina...");
	}
}
