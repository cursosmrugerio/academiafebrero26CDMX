package com.curso.v3D;

public class Principal {

	public static void main(String[] args) throws InterruptedException  {

		Thread descarga = new Thread(() -> descargarArchivo("musica.mp3", 2));

		descarga.start();
		
		//Thread main duerme 10 segundos
		Thread.sleep(10000); 
		
		//Interrumpir sleep() del thread descarga
		descarga.interrupt();
		
		System.out.println("Descargas iniciadas... el main no se bloquea!");
	}

	static void descargarArchivo(String nombre, int segundos) {
		System.out.println("Iniciando descarga de " + nombre + "...");

		for (int i = 1; i <= segundos; i++) {
			try {
				//Thread descarga duerme 10 segundos
				Thread.sleep(10000); 
			} catch (InterruptedException e) {
				System.out.println("Descarga de " + nombre + " fue interrumpida!");
				return;
			}
			System.out.println(nombre + " -> " + i + "/" + segundos + " segundos");
		}

		System.out.println(nombre + " descargado!");
	}
}
