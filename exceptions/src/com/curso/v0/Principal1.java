package com.curso.v0;

public class Principal1 {
	
	public static void main(String[] args) {
		int x = 9;
		int y = 0;
		int resultado = 0;
		
		try{
			resultado = dividir(x,y);
		}catch(ArithmeticException e ) {
			System.out.println("Exception!!!");
		}
		
		System.out.println("Resultado: "+resultado);
		
		System.out.println("Fin de Programa");
	}

	private static int dividir(int x, int y) {
		return x/y;
	}

}
