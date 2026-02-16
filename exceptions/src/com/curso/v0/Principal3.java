package com.curso.v0;

public class Principal3 {
	
	public static void main(String[] args) {
		int x = 9;
		int y = 0;
		int resultado = 0;
		
		try {
			resultado = dividir(x,y);
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}

		System.out.println("Resultado: "+resultado);
		
		System.out.println("Fin de Programa");
	}

	private static int dividir(int x, int y) throws Exception {
		if (y==0)
			throw new Exception("No se puede dividir entre Cero!!!");
		return x/y;
	}

}
