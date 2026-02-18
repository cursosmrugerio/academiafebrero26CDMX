package com.curso.v0;

public class Principal {

	public static void main(String[] args) {
		
		Pato pato1 = new PatoDummy("Yellow");
		pato1.display();
		pato1.volar();
		
		Pato pato2 = new PatoSilvestre("Lucas");
		pato2.display();
		pato2.volar();

	}

}
