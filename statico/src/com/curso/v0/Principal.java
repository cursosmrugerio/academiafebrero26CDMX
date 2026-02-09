package com.curso.v0;

public class Principal {

	public static void main(String[] args) {

		Pato pato1 = new Pato("Donald");
		Pato pato2 = new Pato("Lucas");
		Pato pato3 = new Pato("Feo");
		
		System.out.println(Pato.contador); //3
		System.out.println(Pato.contador); //3
		System.out.println(Pato.contador); //3

	}

}
