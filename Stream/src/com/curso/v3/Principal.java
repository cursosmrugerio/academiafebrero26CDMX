package com.curso.v3;

import java.util.Arrays;
import java.util.Optional;
import java.util.stream.Stream;

public class Principal {
	
	public static void main(String[] args) {
		
		int arreglo[] = {1,2,3,4,5};
		
		arreglo = new int[]{};
		
		//arreglo = null; //nullPointerException
		
		Stream<Integer> stream1 = Arrays.stream(arreglo) //IntStream
								 .boxed(); //Stream<Integer>
		
		Optional<Integer> opt = stream1.reduce((x,y)->x*y); 
		opt.ifPresent(System.out::println);
		System.out.println(opt.orElseGet(()->1));
		
		
	}

}
