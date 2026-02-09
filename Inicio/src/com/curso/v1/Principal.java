package com.curso.v1;

public class Principal {

	public static void main(String[] args) {
		
		int x = 10;
		String cadena = "Hello";
		StringBuilder sb = new StringBuilder("Hola");
		
		show(x,cadena, sb);
		
		System.out.println(x);  //10 
		System.out.println(cadena); //Hello World
		System.out.println(sb); //Hola Mundo
			
	}
	
	static void  show(int x, String cadena, StringBuilder sb) {
		x+=10;
		cadena.concat(" World"); //INMUTABLE 
		sb.append(" Mundo"); //MUTABLE
	}

}
