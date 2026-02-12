package com.curso.v0; // Define el paquete donde vive esta clase

// Clase principal que demuestra como funciona una variable static
public class Principal {

	public static void main(String[] args) {

		// Se crean 3 instancias de Pato - cada 'new' ejecuta el constructor que incrementa 'contador'
		Pato pato1 = new Pato("Donald");  // contador pasa de 0 a 1
		Pato pato2 = new Pato("Lucas");   // contador pasa de 1 a 2
		Pato pato3 = new Pato("Feo");     // contador pasa de 2 a 3

		// Se accede al campo static usando el nombre de la CLASE (Pato.contador), no un objeto
		// Las 3 lineas imprimen 3 porque 'contador' es compartido por todas las instancias
		System.out.println(pato3.contador); //3
		System.out.println(pato2.contador); //3
		System.out.println(pato1.contador); //3

	}

}
