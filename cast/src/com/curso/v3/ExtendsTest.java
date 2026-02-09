package com.curso.v3; // Define el paquete donde vive esta clase

// Clase padre (superclase) generica para demostrar reglas de asignacion de tipos
class B {
}

// Subclase 1: B1 hereda de B (B1 IS-A B)
class B1 extends B {
}

// Subclase 2: B2 hereda de B (B2 IS-A B)
// B1 y B2 son "hermanas" (misma clase padre) pero NO son compatibles entre si
class B2 extends B {
}

// Clase que demuestra las reglas de asignacion entre superclases y subclases
public class ExtendsTest {
	public static void main(String args[]) {
		// Se crean objetos de cada tipo
		B b = new B();     // Referencia B apunta a objeto B
		B1 b1 = new B1();  // Referencia B1 apunta a objeto B1
		B2 b2 = new B2();  // Referencia B2 apunta a objeto B2

		// DOWNCAST INSEGURO: b apunta a un objeto B (no B1)
		// El cast (B1) compila, pero en tiempo de ejecucion lanza ClassCastException
		// porque el objeto real es B, no B1
		// La linea comentada 'if (b instanceof B1)' muestra como hacerlo seguro
		//if (b instanceof B1)
		b1 = (B1) b; //ClassCastException

		// REGLA FUNDAMENTAL DE ASIGNACION:
		// SUPERCLASE = SUBCLASE  -> SIEMPRE VALIDO (upcasting automatico)
		// SUBCLASE = SUPERCLASE  -> REQUIERE CAST EXPLICITO (y puede fallar)
		//PAPAS = HIJOS
		//SUPERCLASES = SUBCLASES
		b = b1; // VALIDO: B (padre) = B1 (hijo) - upcasting automatico, siempre seguro

		// Esto NO compila sin cast: B2 no es padre ni hija de B1, son hermanas
		// b2 = b; // Error de compilacion: B no es B2 (requeriria cast y podria fallar)

	}
}
