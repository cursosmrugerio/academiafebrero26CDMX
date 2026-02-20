package com.curso.v2;

// v2: Hilos con expresiones lambda
// Runnable es una interfaz funcional (un solo metodo abstracto)
// Por lo tanto, podemos usar lambdas en lugar de crear una clase aparte
public class Principal {

	public static void main(String[] args) {

		// Lambda: forma compacta de implementar Runnable
		Thread hilo1 = new Thread(() -> {
			for (int i = 1; i <= 5; i++) {
				System.out.println("Lambda-A -> " + i);
			}
		});

		Thread hilo2 = new Thread(() -> {
			for (int i = 1; i <= 5; i++) {
				System.out.println("Lambda-B -> " + i);
			}
		});

		hilo1.start();
		hilo2.start();

		// Forma ultra compacta para tareas simples
		new Thread(() -> System.out.println("***Hilo de una sola linea!"))
					.start();

		System.out.println("Main continua...");
	}
}
