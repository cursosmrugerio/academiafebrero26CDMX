package com.curso.v1; // Define el paquete donde vive esta clase

// Version mejorada de FindInMatrix: usa un metodo con 'return' en lugar de labels
// Demuestra como extraer logica a un metodo para salir de ciclos anidados de forma limpia
public class FindInMatrix {

	public static void main(String[] args) {

		System.out.println("VERSION return");

		// Misma matriz 2D que en v0
		int[][] list = { { 1, 13 }, { 5, 2 }, { 2, 2 } };

		int searchValue = 2;

		// Delega la busqueda a un metodo que retorna las coordenadas como arreglo [x, y]
		int[] arregloCoordenadas = findCoordenadas(list, searchValue);

		// Verifica si se encontro el valor (-1 significa no encontrado)
		if (arregloCoordenadas[0] == -1 ||
				arregloCoordenadas[1] == -1) {
			System.out.println("Value " + searchValue + " not found");
		} else {
			System.out.println("Value " + searchValue + " found at: " +
					"(" + arregloCoordenadas[0] + "," + arregloCoordenadas[1] + ")");
		}

	}

	// Metodo que busca un valor en la matriz y retorna sus coordenadas [fila, columna]
	// Ventaja sobre v0: al usar 'return', sale de TODOS los ciclos de inmediato sin necesitar labels
	static int[] findCoordenadas(int[][] list, int searchValue){

		int positionX = -1; // Valor inicial: no encontrado
		int positionY = -1;

		// Arreglo para almacenar las coordenadas del resultado
		int[] res = {positionX,positionY};

		// Recorre la matriz fila por fila, columna por columna
		for (int i = 0; i < list.length; i++) {
			for (int j = 0; j < list[i].length; j++) {
				if (list[i][j] == searchValue) {
					res[0] = i; // Guarda la fila
					res[1] = j; // Guarda la columna
					System.out.println("("+i+","+j+")");
					return res; // Sale del metodo inmediatamente (no necesita labels)
				}
			}
		}

		// Si no encontro el valor, retorna [-1, -1]
		return res;

	}


}
