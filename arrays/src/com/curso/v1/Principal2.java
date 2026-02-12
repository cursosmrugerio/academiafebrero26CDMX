package com.curso.v1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Principal2 {
	
	public static void main(String[] args) {
		
		Integer[] arreglo1 = new Integer[3];
		Integer[] arreglo2 = {0,1,2};
		Integer[] arreglo3 = new Integer[]{0,1,2};
		
		List<Integer> lista1 = Arrays.asList(arreglo3);
		List<Integer> lista2 = List.of(arreglo2);
		List<Integer> lista3 = 
				new ArrayList<>(Arrays.asList(arreglo1));
		
		Integer[] arreglo4 = (Integer[])lista3.toArray();
		
	}

}
