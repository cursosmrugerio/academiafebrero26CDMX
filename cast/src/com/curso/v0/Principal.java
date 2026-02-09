package com.curso.v0; // Define el paquete donde vive esta clase

// Clase que demuestra tres formas de trabajar con objetos:
// 1. Uso directo  2. Polimorfismo  3. Downcasting
public class Principal {

	// 'String... patitos' es equivalente a 'String[] args' (varargs)
	public static void main(String... patitos) {
		// --- USO DIRECTO ---
		// Referencia tipo Pato apunta a objeto Pato: acceso completo a todos los metodos
		Pato pato1 = new Pato();
		pato1.volar(); //Pato volar

		// --- POLIMORFISMO ---
		// Referencia tipo Ave apunta a objeto Pato (upcasting automatico)
		// BUENA PRACTICA: programar hacia la interfaz/superclase
		// Pero solo se puede acceder a metodos definidos en Ave (no volarPato)
		Ave pato2 = new Pato(); //BUENISIMA PRACTICA
		pato2.volar(); //Pato volar

		// --- DOWNCASTING ---
		// Referencia tipo Ave apunta a objeto Pato
		Ave pato3 = new Pato();
		// Para acceder a volarPato() se necesita DOWNCAST: convertir Ave -> Pato
		// (Pato)pato3 le dice al compilador: "confia, este objeto ES un Pato"
		// Si el objeto NO fuera Pato, lanzaria ClassCastException en tiempo de ejecucion
		((Pato)pato3).volarPato(); //CAST DOWNCASTING
	}

}
