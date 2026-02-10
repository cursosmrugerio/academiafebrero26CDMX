package com.curso.v1; // Define el paquete donde vive esta clase

// Clase que demuestra la diferencia entre variables de instancia y variables static
public class Pato {

	// Variable de INSTANCIA: cada objeto Pato tiene su propia copia de 'name'
	String name;
	// Variable STATIC (de clase): existe una sola copia compartida por TODOS los objetos Pato
	// Se inicializa automaticamente en 0 (valor por defecto de int)
	static int contador; //0

	// Constructor: se ejecuta cada vez que se crea un nuevo Pato con 'new Pato(...)'
	Pato(String name){
		// 'this.name' se refiere al campo de la instancia; 'name' al parametro recibido
		this.name = name;
		// Incrementa el contador COMPARTIDO: como es static, TODOS los objetos ven el mismo valor
		// Cada vez que se crea un Pato, el contador global sube en 1
		contador++;
	}

}
