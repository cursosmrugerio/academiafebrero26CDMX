package com.curso.v0;

public class Principal0 {
	
	public static void main(String[] args) {
		int x = 9;
		int y = 0;
		
		int resultado = dividir(x,y);
		
		System.out.println("Resultado: "+resultado);
		
		System.out.println("Fin de Programa");
	}

	private static int dividir(int x, int y) {
		return x/y;
	}

}
