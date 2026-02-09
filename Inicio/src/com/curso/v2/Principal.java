package com.curso.v2;

public class Principal {

	public static void main(String[] args) {
		
		int x = 10;
		String cadena = "Hello";
		StringBuilder sb = new StringBuilder("Hola");
		
		cadena = show(x,cadena, sb);
		
		System.out.println(x);  //10 
		System.out.println(cadena); //Hello World
		System.out.println(sb); //Hola Mundo
			
	}
	
	static String show(int x, String cadena, StringBuilder sb) {
		x+=10;
		sb.append(" Mundo"); //MUTABLE
		return cadena.concat(" World"); //INMUTABLE 
	}

}
