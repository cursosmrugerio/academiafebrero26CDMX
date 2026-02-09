package com.curso.v0; // Define el paquete donde vive esta clase

// Clase que demuestra como funciona el Garbage Collector (GC) de Java
// y la relacion de composicion HAS-A (tiene un)
public class NewClass {

	// Campo de tipo Object: relacion HAS-A (NewClass "tiene un" Object)
	// Es una referencia a otro objeto almacenado en el heap
	private Object o; //HAS-A

	// Metodo que asigna una referencia externa al campo interno 'o'
	void doSomething(Object s) {
		o = s; // El campo 'o' ahora apunta al mismo objeto que 's'
	}

	public static void main(String args[]) {
		// Paso 1: Se crea un Object en el heap. 'obj' apunta a ese objeto (llamemoslo ObjA)
		Object obj = new Object(); // 1  //GARBAGE COLLECTOR

		// Paso 2: Se crea una instancia de NewClass en el heap. 'tc' apunta a ella
		NewClass tc = new NewClass(); // 2
		// Paso 3: tc.o ahora apunta a ObjA (el mismo objeto que 'obj')
		// ObjA tiene 2 referencias: 'obj' y 'tc.o'
		tc.doSomething(obj); // 3
		// Paso 4: Se crea un NUEVO Object (ObjB). 'obj' ahora apunta a ObjB
		// ObjA aun NO es elegible para GC porque tc.o sigue apuntando a el
		obj = new Object(); // 4
		// Paso 5: 'obj' ahora es null. ObjB ya no tiene referencias -> elegible para GC
		// ObjA sigue vivo porque tc.o lo referencia
		obj = null; // 5
		// Paso 6: tc.o ahora apunta a null (el valor de obj)
		// ObjA ya NO tiene ninguna referencia -> elegible para GC
		tc.doSomething(obj); // 6
	}
}
