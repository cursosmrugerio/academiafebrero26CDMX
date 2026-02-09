package com.curso.v0; // Define el paquete donde vive esta clase

// Clase que demuestra el polimorfismo basico: una referencia de tipo padre
// puede apuntar a cualquier objeto hijo, y el metodo ejecutado es el del objeto real
public class Principal {

	public static void main(String[] args) {

		// Referencia tipo Pato apunta a objeto Pato - uso directo, sin polimorfismo
		Pato ave1 = new Pato();
		ave1.volar(); //Volar Pato

		// POLIMORFISMO: referencia tipo Ave apunta a objeto Pato
		// El compilador ve 'Ave', pero en tiempo de ejecucion se ejecuta el metodo de Pato
		Ave ave2 = new Pato();
		ave2.volar(); //Volar Pato

		// Polimorfismo: referencia Ave apunta a Pinguino
		// Se ejecuta el volar() de Pinguino aunque la variable es tipo Ave
		Ave ave3 = new Pinguino();
		ave3.volar(); //No vuelar Pinguino

		// Polimorfismo: referencia Ave apunta a Perico
		Ave ave4 = new Perico();
		ave4.volar(); //Volar Perico

	}

}
