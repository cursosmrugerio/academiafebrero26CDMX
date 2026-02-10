package com.curso.v0; // Define el paquete donde vive esta clase

// Clase que demuestra la busqueda en una matriz 2D usando etiquetas (labels) con break y continue
public class FindInMatrix {
	public static void main(String[] args) {

		// Matriz 2D de 3 filas x 2 columnas
		int[][] list = { { 1, 13 }, { 5, 2 }, { 2, 2 } };

		int searchValue = 2;  // Valor a buscar en la matriz
		int positionX = -1;   // Fila donde se encontro (-1 = no encontrado)
		int positionY = -1;   // Columna donde se encontro (-1 = no encontrado)

		// PATITO es una ETIQUETA (label) que identifica al ciclo externo
		// Permite que break/continue se refieran al ciclo externo y no solo al interno
		PATITO: for (int i = 0; i < list.length; i++) {
			for (int j = 0; j < list[i].length; j++) {
				if (list[i][j] == searchValue) {
					positionX = i;
					positionY = j;
					System.out.println("("+i+","+j+")");
					// Cada opcion produce un resultado diferente (descomentar una a la vez):
					//continue;         // Salta a la siguiente iteracion del ciclo INTERNO - encuentra (1,1)(2,0)(2,1)
					//break;            // Sale del ciclo INTERNO, sigue con el externo - encuentra (1,1)(2,0)
					//continue PATITO;  // Salta a la siguiente iteracion del ciclo EXTERNO - encuentra (1,1)(2,0)
					//break PATITO;     // Sale de AMBOS ciclos completamente - encuentra solo (1,1)
				}
			}
		}

		// Verifica si se encontro el valor e imprime el resultado
		if (positionX == -1 || positionY == -1) {
			System.out.println("Value " + searchValue + " not found");
		} else {
			System.out.println("Value " + searchValue + " found at: " + "(" + positionX + "," + positionY + ")");
		}

	}

}
