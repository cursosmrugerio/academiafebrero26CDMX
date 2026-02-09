package com.curso.v0;

public class Principal {
	
	public static void main(String... patitos) {
		Pato pato1 = new Pato();
		pato1.volar(); //Pato volar
		
		//POLIMORFISMO
		Ave pato2 = new Pato(); //BUENISIMA PRACTICA
		pato2.volar(); //Pato volar
		
		Ave pato3 = new Pato();
		((Pato)pato3).volarPato(); //CAST DOWNCASTING
	}

}
