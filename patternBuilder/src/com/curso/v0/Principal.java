package com.curso.v0;

public class Principal {

	public static void main(String[] args) {
		
		
		String resultado1 = "" //1 Objeto
				.concat("Hola") //2 Objeto
				.concat(" ") //3 Objeto
				.concat("mundo"); //4 Objeto
				
		String resultado2 = new StringBuilder()
			    .append("Hola")
			    .append(" ")
			    .append("mundo") //1 Objeto
			    .toString(); 
		
		System.out.println(resultado1);
		System.out.println(resultado2);

	}

}
