package com.curso.v2;

public class Principal0 {

	public static void main(String[] args) {
		int x = 12;
		int y = 0;

		int resultado = 0;

		resultado = dividir(x, y);

		System.out.println("Resultado: " + resultado);
		System.out.println("End Program");

	}

	private static int dividir(int x, int y) {

		if (y == 0)
			throw new DividirEntreCero("No se puede dividir entre cero!!!");

		return x / y;
	}

}
