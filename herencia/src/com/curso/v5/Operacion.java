package com.curso.v5;

public interface Operacion {
	
	//public static final
	int contador = 0;
	
	//public abstract
	int ejecuta();
	
	default public String show() {
		return "Operacion";
	}
	
	static void showContador() {
		System.out.println("Contador: "+contador);
	}
	
}
