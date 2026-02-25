package com.curso.v0;

import java.util.Arrays;
import java.util.List;
import java.util.stream.*;

public class Principal2 {

	public static void main(String[] args) {
		
		System.out.println("Principal2");

		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");

		List<Integer> listNames = companyNames.stream()
				.filter(name -> !name.isBlank()) //Predicate
				//.map(x -> x.length()) //Function
				.map(String::length) //Function
				.collect(Collectors.toList());
		
		System.out.println(listNames);
		
	}

}
