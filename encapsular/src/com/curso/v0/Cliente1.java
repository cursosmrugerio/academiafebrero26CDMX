package com.curso.v0;

public class Cliente1 {
	
	public static void main(String[] args) {
		Pato pato = new Pato("Donald",5);
		
		pato.name = "Lucas";
		pato.age = 20;
		
		System.out.println(pato);
	}

}
