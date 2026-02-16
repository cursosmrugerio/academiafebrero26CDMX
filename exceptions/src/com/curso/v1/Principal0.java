package com.curso.v1;

public class Principal0 {
	
	public static void main(String[] args) {
		int x = 9;
		int y = 0;
		
		int resultado=0;
		
		try {
			resultado = dividir(x,y);
		} catch (DividirEntreCero e) {
			e.printStackTrace();
		}
		
		System.out.println("Resultado: "+ resultado);
		System.out.println("End Program");
		
	}

	private static int dividir(int x, int y) throws DividirEntreCero{
		
		if (y == 0)
			throw new DividirEntreCero("No se puede dividir entre cero!!!");
		
		return x/y;
	}

}
