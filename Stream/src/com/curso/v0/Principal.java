package com.curso.v0;

import java.util.Arrays;
import java.util.List;
import java.util.stream.*;

public class Principal {

	public static void main(String[] args) {

		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");
		
		//Stream Source
		Stream<String> stream1 = companyNames.stream();
		
		//Intermediate
		Stream<String> stream2 = stream1.filter(name -> !name.isBlank());
		
		//Terminal
		List<String> listNames = stream2.collect(Collectors.toList());
		
		System.out.println(listNames);
		
	}

}
