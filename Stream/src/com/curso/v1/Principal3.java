package com.curso.v1;

import java.util.*;
import java.util.stream.Stream;

public class Principal3 {

	public static void main(String[] args) {
		
		int[] enteros1 = {1,2,3,4,5,6,7,8,9,10};
		int[] enteros2 = {11,12,13,14,15,16,17,18,19,20};
		int[] enteros3 = {51,52,53,54,55,56,57,58,59,60};
		
		List<Integer> list1 = Arrays.stream(enteros1) //IntStream
								.boxed() //Stream<Integer>
								.toList(); //List<Integer>
		
		List<Integer> list2 = Arrays.stream(enteros2) 
				.boxed() 
				.toList(); 
		
		List<Integer> list3 = Arrays.stream(enteros3) 
				.boxed() 
				.toList(); 
		
		Stream<List<Integer>> stream = Stream.of(list1,list2,list3);
		
		Stream<Integer> streamEnteros = stream.flatMap(l -> l.stream());
		
		streamEnteros.forEach(System.out::println);
							  
		
		
		
		

	}

}
