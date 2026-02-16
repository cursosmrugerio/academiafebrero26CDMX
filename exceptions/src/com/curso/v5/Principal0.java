package com.curso.v5;

public class Principal0 {

	public static void main(String[] args) {
		int x = 1025;
		int y = 5;

		int resultado = 0;

		try {
			resultado = dividir(x, y);
		} catch (DivisorNoNegativo | DividirEntreCero | UnsupportedOperationException e) {
			e.printStackTrace();
		} 

		System.out.println("Resultado: " + resultado);
		System.out.println("End Program");

	}

	private static int dividir(int x, int y) 
			throws DividirEntreCero, DivisorNoNegativo  {

		if (y == 0)
			throw new DividirEntreCero("No se puede dividir entre cero!!!");
		if (y < 0)
			throw new DivisorNoNegativo("No se puede dividir con negativo");
		if (x >= 1000)
			throw new UnsupportedOperationException("Dividendo no puede ser mayor a 1000");
		return x / y;
	}

}
