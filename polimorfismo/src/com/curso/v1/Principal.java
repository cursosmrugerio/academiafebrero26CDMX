package com.curso.v1; // Define el paquete donde vive esta clase

// Evolucion de v0: demuestra que una SOLA variable de tipo Ave puede reasignarse
// a diferentes subclases, reutilizando la misma referencia polimorfica
public class Principal {

	public static void main(String[] args) {
		// Se declara UNA sola variable de tipo Ave (sin inicializar)
		Ave ave;

		// Se asigna un objeto Perico a la referencia 'ave'
		ave = new Perico();
		// Se ejecuta volar() de Perico (dispatch dinamico)
		ave.volar();
		// Se REASIGNA la misma variable a un objeto Pinguino
		// El objeto Perico anterior queda sin referencia (elegible para GC)
		ave = new Pinguino();
		// Ahora se ejecuta volar() de Pinguino
		ave.volar();
		// Se reasigna nuevamente a un objeto Pato
		ave = new Pato();
		// Se ejecuta volar() de Pato
		ave.volar();
	}

}
