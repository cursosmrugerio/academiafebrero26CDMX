package com.curso.v3;

public class Principal0 {

	public static void main(String[] args) {
		int x = 12;
		int y = -2;

		int resultado = 0;

		try {
			resultado = dividir(x, y);
		} catch (DividirEntreCero e) {
			e.printStackTrace();
		} catch (DivisorNoNegativo e) {
			e.printStackTrace();
		}

		System.out.println("Resultado: " + resultado);
		System.out.println("End Program");

	}

	private static int dividir(int x, int y) throws DividirEntreCero, DivisorNoNegativo {

		if (y == 0)
			throw new DividirEntreCero("No se puede dividir entre cero!!!");
		if (y < 0)
			throw new DivisorNoNegativo("No se puede dividir con negativo");
		return x / y;
	}

}
