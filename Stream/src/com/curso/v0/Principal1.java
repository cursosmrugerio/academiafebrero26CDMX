package com.curso.v0;

import java.util.Arrays;
import java.util.List;
import java.util.stream.*;

public class Principal1 {

	public static void main(String[] args) {
		
		System.out.println("Principal1");

		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");

		List<String> listNames = companyNames.stream()
				.filter(name -> !name.isBlank()) //Predicate
				.collect(Collectors.toList());
		
		System.out.println(listNames);
		
	}

}
