package com.curso.v4;

import java.util.Arrays;
import java.util.Optional;
import java.util.stream.Stream;

public class Principal {
	
	public static void main(String[] args) {
		
		int arreglo[] = {1,2,3,4,5};
		
		arreglo = new int[]{};
		
		Stream<Integer> stream1 = Arrays.stream(arreglo) //IntStream
								 .boxed(); //Stream<Integer>
		
		int r = stream1.reduce( 1 , (x,y)->x*y); 
		
		System.out.println(r);
		
		
		
	}

}
