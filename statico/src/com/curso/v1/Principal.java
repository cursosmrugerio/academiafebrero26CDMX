package com.curso.v1; // Define el paquete donde vive esta clase

//static 
import static com.curso.v1.Pato.contador;

// Clase principal que demuestra como funciona una variable static
public class Principal {

	public static void main(String[] args) {

		// Se crean 3 instancias de Pato - cada 'new' ejecuta el constructor que incrementa 'contador'
		Pato pato1 = new Pato("Donald");  // contador pasa de 0 a 1
		Pato pato2 = new Pato("Lucas");   // contador pasa de 1 a 2
		Pato pato3 = new Pato("Feo");     // contador pasa de 2 a 3
		Pato pato4 = new Pato("Rich");

		System.out.println(contador); //4

	}

}
