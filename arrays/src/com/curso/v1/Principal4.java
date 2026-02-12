package com.curso.v1;

import java.util.ArrayList;
import java.util.List;

public class Principal4 {
	
	
	public static void main(String[] args) {
		
		List<Integer> lista = List.of(1,2,3,4);
//		List<Integer> lista = new ArrayList<>();
//		lista.add(1);
//		lista.add(2);
//		lista.add(3);
//		lista.add(4);
		
		lista.add(5);
		lista.remove(0);
		lista.set(1, 22);
		
		for (Integer i:lista)
			System.out.println(i);
		
	}

}
