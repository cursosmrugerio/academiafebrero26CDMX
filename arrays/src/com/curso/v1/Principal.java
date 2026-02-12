package com.curso.v1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Principal {
	
	public static void main(String[] args) {
		
		int[] arreglo1 = new int[3];
		int[] arreglo2 = {0,1,2};
		int[] arreglo3 = new int[]{0,1,2};
		
		System.out.println(Arrays.toString(arreglo2));
		System.out.println(arreglo3);
		
		List<int[]> lista1 = Arrays.asList(arreglo3);
		List<int[]> lista2 = List.of(arreglo2);
		
		
	}

}
