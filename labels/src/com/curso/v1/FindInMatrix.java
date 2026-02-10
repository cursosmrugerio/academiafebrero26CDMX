package com.curso.v1;

public class FindInMatrix {
	
	public static void main(String[] args) {
		
		System.out.println("VERSION return");
		
		int[][] list = { { 1, 13 }, { 5, 2 }, { 2, 2 } };

		int searchValue = 2;

		int[] arregloCoordenadas = findCoordenadas(list, searchValue);
		
		if (arregloCoordenadas[0] == -1 || 
				arregloCoordenadas[1] == -1) {
			System.out.println("Value " + searchValue + " not found");
		} else {
			System.out.println("Value " + searchValue + " found at: " + 
					"(" + arregloCoordenadas[0] + "," + arregloCoordenadas[1] + ")");
		}

	}
	
	static int[] findCoordenadas(int[][] list, int searchValue){
		
		int positionX = -1;
		int positionY = -1;
		
		int[] res = {positionX,positionY};
		
		for (int i = 0; i < list.length; i++) {
			for (int j = 0; j < list[i].length; j++) {
				if (list[i][j] == searchValue) {
					res[0] = i;
					res[1] = j;
					System.out.println("("+i+","+j+")");
					return res;
				}
			}
		}
		
		return res;

	}
	

}
