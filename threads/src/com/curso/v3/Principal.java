package com.curso.v3;

// v3: sleep() - simular tareas que toman tiempo
// sleep() pausa el hilo actual por N milisegundos
// Esto permite que otros hilos se ejecuten mientras uno espera
public class Principal {

	public static void main(String[] args) {

		Thread descarga1 = new Thread(() -> descargarArchivo("foto.jpg", 3));
		Thread descarga2 = new Thread(() -> descargarArchivo("video.mp4", 5));
		Thread descarga3 = new Thread(() -> descargarArchivo("musica.mp3", 2));

		descarga1.start();
		descarga2.start();
		descarga3.start();

		System.out.println("Descargas iniciadas... el main no se bloquea!");
	}

	static void descargarArchivo(String nombre, int segundos) {
		System.out.println("Iniciando descarga de " + nombre + "...");

		for (int i = 1; i <= segundos; i++) {
			try {
				Thread.sleep(1000); // pausa 1 segundo
			} catch (InterruptedException e) {
				System.out.println("Descarga de " + nombre + " fue interrumpida!");
				return;
			}
			System.out.println(nombre + " -> " + i + "/" + segundos + " segundos");
		}

		System.out.println(nombre + " descargado!");
	}
}
