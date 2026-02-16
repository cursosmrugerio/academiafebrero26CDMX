package com.curso.v0;

public class Principal4 {
	
	public static void main(String[] args) throws Exception {
		int x = 9;
		int y = 0;
		int resultado = 0;
		
		resultado = dividir(x,y);

		System.out.println("Resultado: "+resultado);
		
		System.out.println("Fin de Programa");
	}

	private static int dividir(int x, int y) throws Exception {
		if (y==0)
			throw new Exception("No se puede dividir entre Cero!!!");
		return x/y;
	}

}
