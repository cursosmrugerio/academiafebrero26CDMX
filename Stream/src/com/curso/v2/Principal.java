package com.curso.v2;

import java.util.stream.Stream;

public class Principal {

	public static void main(String[] args) {
		Stream<Integer> oddNumberUnder100 = 
				Stream.iterate(
						1, // seed
						n -> n < 100, // Predicate to specify when done
						n -> n + 2); // UnaryOperator to get next value
		
		oddNumberUnder100.forEach(System.out::println);
		
		System.out.println("*************");
		
		oddNumberUnder100 = 
				Stream.iterate(
						0, // seed
						n -> n < 50, // Predicate to specify when done
						n -> n + 3);
		
		oddNumberUnder100.forEach(System.out::println);

				
	}
	
	
}
