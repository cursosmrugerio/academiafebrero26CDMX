package com.curso.v1;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Principal {

	public static void main(String[] args) {
		
		int[] enteros = {1,2,3,4,5,6,7,8,9,0};
		
		IntStream stream = Arrays.stream(enteros);
		
		long l = stream.filter(n -> n%2==0)
			  .peek(System.out::println) 
			  .map(x -> x*10)
			  .count();
		
		System.out.println("Count: "+l);

	}

}
