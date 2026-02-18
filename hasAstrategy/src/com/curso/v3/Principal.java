package com.curso.v3;

public class Principal {

	public static void main(String[] args) {
		
		System.out.println("V3");
		
		Pato pato1 = new PatoDummy("Yellow");
		pato1.display();
		pato1.volar(); //No Volar
		
		Pato pato2 = new PatoSilvestre("Lucas");
		pato2.display();
		pato2.volar(); //Si Volar
		
		System.out.println("*************");
		
		Pato pato3 = new PatoSilvestre("Donald");
		pato3.display();
		pato3.volar(); //Si Volar
		
		pato3.display();
		pato3.setCv(new VolarAleatorio());
		pato3.volar(); //Si Quiere Vuela
		
		pato3.display();
		pato3.setCv(new VolarNo());
		pato3.volar(); //No Vuela

	}

}
