package com.curso.v0;

public class Principal {

	public static void main(String[] args) {		

		Pato pato1 = new Pato("Donald",5);
		Pato pato2 = new Pato("Donald",5);
		
		System.out.println(pato1 == pato2); //false
		System.out.println(pato1.equals(pato2)); //true
		
		String name1 = new String("Donald");
		String name2 = new String("Donald");
		
		System.out.println(name1 == name2); //false
		System.out.println(name1.equals(name2)); //true
		
		
		
		 
	}

}
