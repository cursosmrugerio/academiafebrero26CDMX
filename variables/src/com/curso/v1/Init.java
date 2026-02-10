package com.curso.v1; // Define el paquete donde vive esta clase

// Clase que demuestra los valores por defecto de variables de instancia y static en Java
public class Init {

	// Variables de INSTANCIA: cada objeto Init tiene su propia copia
	String title;       // Valor por defecto de objetos (String): null
	boolean published;  // Valor por defecto de boolean: false

	// Variables STATIC: una sola copia compartida por todas las instancias
	static int total;       // Valor por defecto de int: 0
	static double maxPrice; // Valor por defecto de double: 0.0

	public static void main(String[] args) {
		// Crea una instancia de Init sin asignar valores a sus campos
		Init initMe = new Init();
		// Variable local: DEBE inicializarse antes de usarse (no tiene valor por defecto)
		double price;
		// La condicion siempre es true, asi que price se inicializa en 100.0
		if (true)
			price = 100.0000;

		// Imprime todos los valores: se observan los valores por defecto de cada tipo
		System.out.println("|" + initMe.title + "|"      // null (String)
				+ initMe.published + "|"                  // false (boolean)
				+ Init.total + "|"                        // 0 (int)
				+ Init.maxPrice + "|"                     // 0.0 (double)
				+ price + "|");                           // 100.0 (asignado manualmente)

		// Resultado: |null|false|0|0.0|100.0|


	}

}