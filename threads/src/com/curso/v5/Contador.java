package com.curso.v5;

// v5: Problema de concurrencia - recurso compartido sin proteccion
// Cuando dos hilos modifican la misma variable al mismo tiempo,
// el resultado es IMPREDECIBLE (race condition)
public class Contador {

	private int valor = 0;

	// Este metodo NO es thread-safe
	// Internamente, valor++ son 3 operaciones: leer, sumar, escribir
	// Si dos hilos lo ejecutan al mismo tiempo, pueden pisar los valores del otro
	public void incrementar() {
		valor++;
	}

	public int getValor() {
		return valor;
	}
}
