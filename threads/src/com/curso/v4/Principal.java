package com.curso.v4;

// v4: join() - esperar a que los hilos terminen antes de continuar
// Sin join(), el main puede terminar antes que los hilos hijos
// Con join(), el main espera a que cada hilo termine
public class Principal {

	public static void main(String[] args) {

		Thread hilo1 = new Thread(() -> {
			System.out.println("Hilo-1: Consultando base de datos...");
			pausar(3000);
			System.out.println("Hilo-1: Consulta terminada!");
		});

		Thread hilo2 = new Thread(() -> {
			System.out.println("Hilo-2: Llamando API externa...");
			pausar(2000);
			System.out.println("Hilo-2: Respuesta recibida!");
		});

		Thread hilo3 = new Thread(() -> {
			System.out.println("Hilo-3: Procesando archivo...");
			pausar(1000);
			System.out.println("Hilo-3: Archivo procesado!");
		});

		long inicio = System.currentTimeMillis();

		hilo1.start();
		hilo2.start();
		hilo3.start();

		// join() hace que main ESPERE a que cada hilo termine
		try {
			hilo1.join();
			hilo2.join();
			hilo3.join();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

		long duracion = System.currentTimeMillis() - inicio;

		// Sin hilos, tardaria 3+2+1 = 6 segundos
		// Con hilos, tarda ~3 segundos (el maximo de los tres)
		System.out.println("Todas las tareas terminaron en " + duracion + " ms");
		System.out.println("(Sin hilos habrian tardado ~6000 ms)");
	}

	static void pausar(int milisegundos) {
		try {
			Thread.sleep(milisegundos);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
