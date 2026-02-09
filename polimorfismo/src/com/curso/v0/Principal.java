package com.curso.v0;

public class Principal {

	public static void main(String[] args) {

		Pato ave1 = new Pato();
		ave1.volar(); //Volar Pato
		
		Ave ave2 = new Pato();
		ave2.volar(); //Volar Pato
		
		Ave ave3 = new Pinguino();
		ave3.volar(); //No vuelar Pinguino
		
		Ave ave4 = new Perico();
		ave4.volar(); //Volar Perico
		
		
		
		
	}

}
