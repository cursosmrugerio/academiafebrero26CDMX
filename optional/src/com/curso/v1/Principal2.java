package com.curso.v1;

import java.util.*;

public class Principal2 {

	public static void main(String[] args) {
		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");
		
		Optional<List<String>> listOptional = 
							Optional.of(companyNames);

		
		//filter estamos pasando una List 
		//listOptional = listOptional.filter(name -> !name.isEmpty());
		listOptional = listOptional.filter(lista -> !lista.isEmpty());
		
		List<String> newList = listOptional.get();
			
		System.out.println(newList);
		
		System.out.println("******");
		
		String cadena = "";
		System.out.println(cadena.isEmpty()); //true
		System.out.println(cadena.isBlank()); //true
		
		String cadena2 = " ";
		System.out.println(cadena2.isEmpty()); //false
		System.out.println(cadena2.isBlank()); //true
		
		System.out.println("******");
		
		String name = "Epeneto";
		name = name.concat(" Andronico");
		System.out.println(name);
	}

}
