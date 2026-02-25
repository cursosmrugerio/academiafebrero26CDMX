package com.curso.v1;

import java.util.*;

public class Principal {

	public static void main(String[] args) {
		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");
		
		companyNames = null;
		//companyNames.add("OpenIA");
		
		Optional<List<String>> listOptional = 
							Optional.ofNullable(companyNames);

		int tamanio = listOptional
			//.map(List::size) //Function<T,U>
			.map(l -> l.size())
			.orElse(0);
		
		System.out.println("Size: "+tamanio);
	}

}
