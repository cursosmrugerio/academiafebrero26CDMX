package com.curso.v1;

import java.util.*;
import java.util.function.Function;

public class Principal3 {

	public static void main(String[] args) {
		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");
		
		companyNames = new ArrayList<>(companyNames);
		
		companyNames.removeIf(n -> n.isEmpty());
		
		Optional<List<String>> listOptional = 
							Optional.ofNullable(companyNames);
		
		List<String> companyNamesOther = listOptional.get();
		
		System.out.println(companyNamesOther);
		
		
		
		
	}

}
