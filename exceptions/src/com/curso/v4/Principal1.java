package com.curso.v4;

public class Principal1 {

	public static void main(String[] args) {
		int x = 1001;
		int y = 2;

		int resultado = 0;

		try {
			resultado = dividir(x, y);
		} catch (DividirEntreCero e) {
			e.printStackTrace();
		} catch (DivisorNoNegativo e) {
			e.printStackTrace();
		} catch (UnsupportedOperationException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		} 

		System.out.println("Resultado: " + resultado);
		System.out.println("End Program");

	}

	private static int dividir(int x, int y) throws Exception  {

		if (y == 0)
			throw new DividirEntreCero("No se puede dividir entre cero!!!");
		if (y < 0)
			throw new DivisorNoNegativo("No se puede dividir con negativo");
		if (x >= 1000)
			throw new UnsupportedOperationException("Dividendo no puede ser mayor a 1000");
		return x / y;
		
	}

}
