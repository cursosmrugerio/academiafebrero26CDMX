package com.curso.v2;

public class Principal {

	public static void main(String[] args) {
		
		comportamientoVolar(new Pato());
		comportamientoVolar(new Pinguino());
		comportamientoVolar(new Ave());
		comportamientoVolar(new Perico());
	
	}
	
	static void comportamientoVolar(Ave ave) {
		ave.volar();
	}

}
