package com.curso.v1;

// v1: Crear hilos implementando Runnable (PREFERIDO)
// Ventaja: la clase puede extender otra clase, porque Runnable es una interfaz
// Promueve composicion sobre herencia
public class MiTarea implements Runnable {

	private String nombre;
	private int contador;

	public MiTarea(String nombre, int contador) {
		this.nombre = nombre;
		this.contador = contador;
	}

	@Override
	public void run() {
		for (int i = 1; i <= contador; i++) {
			System.out.println(nombre + " -> " + i);
		}
		System.out.println(nombre + " termino!");
	}
}
