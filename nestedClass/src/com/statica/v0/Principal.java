package com.statica.v0;

class Animal{
	static int contador;
	static class Pato{} //Static nested Class
	//Static nested Class, le pertenece a la clase.
}

public class Principal {

	public static void main(String[] args) {
		
		Animal.Pato pato1 = new Animal.Pato();
		
		System.out.println(pato1);

	}

}
