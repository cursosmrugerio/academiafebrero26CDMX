package com.curso.v1;

// v1: Hilos con implements Runnable
// Runnable separa la TAREA del MECANISMO de ejecucion (Thread)
public class Principal {

	public static void main(String[] args) {

		// Creamos la tarea (Runnable)
		MiTarea tarea1 = new MiTarea("Tarea-A", 5);
		MiTarea tarea2 = new MiTarea("Tarea-B", 5);

		// Creamos los hilos y les pasamos la tarea
		Thread hilo1 = new Thread(tarea1);
		Thread hilo2 = new Thread(tarea2);

		hilo1.start();
		hilo2.start();

		// Observa: el orden de ejecucion NO es determinista
		// Ejecuta varias veces y veras resultados diferentes
		System.out.println("Main continua...");
	}
}
