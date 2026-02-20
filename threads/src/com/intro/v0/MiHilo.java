package com.intro.v0;

public class MiHilo {

	private String nombre;
	private int contador;

	public MiHilo(String nombre, int contador) {
		this.nombre = nombre; 
		this.contador = contador;
	}

	public void run() {
		for (int i = 1; i <= contador; i++) {
			System.out.println(nombre + " -> " + i);
		}
		System.out.println(nombre + " termino!");
	}
}
