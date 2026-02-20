package com.curso.v0A;

// v0: Crear un hilo extendiendo la clase Thread
// Esta es la forma mas directa, pero limita la herencia (Java no tiene herencia multiple)
public class MiHilo extends Thread {

	private int contador;

	public MiHilo(String nombre, int contador) {
		super(nombre); // asigna nombre al hilo
		this.contador = contador;
	}

	@Override
	public void run() {
		// Este metodo se ejecuta en un hilo separado cuando llamamos start()
		for (int i = 1; i <= contador; i++) {
			System.out.println(getName() + " -> " + i);
		}
		System.out.println(getName() + " termino!");
	}
}
