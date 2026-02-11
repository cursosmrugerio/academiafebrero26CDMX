package com.curso.v1;

public class Cliente1 {
	
	public static void main(String[] args) {
		Pato pato = new Pato("Donald",5);
		
		pato.setName("Lucas");
		pato.setAge(20);
		
		System.out.println(pato.getName());
	}

}
