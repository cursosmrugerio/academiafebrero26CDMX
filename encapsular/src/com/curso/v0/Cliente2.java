package com.curso.v0;

public class Cliente2 {
	
	public static void main(String[] args) {
		Pato pato = new Pato("Donald",5);
		
		pato.name = "Feo";
		pato.age = -10;
		
		System.out.println(pato);
	}

}
