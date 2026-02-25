package com.curso.v0;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.*;

public class Principal3 {

	public static void main(String[] args) {
		
		System.out.println("Principal3");

		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");

		Optional<Integer> valorMaximo = companyNames.stream()
				.filter(name -> !name.isBlank()) //Predicate
				//.map(x -> x.length()) //Function
				.map(String::length) //Function
				.max((t,u) -> t-u); //Comparator
		
		System.out.println(valorMaximo);
		
		int max = valorMaximo.get();
		
		System.out.println(max);
		
		
	}

}
