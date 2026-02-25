package com.curso.v0;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.stream.*;

public class Principal5 {

	public static void main(String[] args) {
		
		System.out.println("Principal3");

		List<String> companyNames = Arrays.asList(
				"paypal", 
				"oracle", 
				"", 
				"microsoft", 
				"", 
				"apple");
		
		//companyNames = new ArrayList<>();

		int max = companyNames.stream()
				.filter(name -> !name.isBlank()) //Predicate
				//.map(x -> x.length()) //Function
				.map(String::length) //Function
				.peek(System.out::println) //Consumer
				//.max((t,u) -> t-u) //Comparator //return Optional<Integer>
				.max(Comparator.naturalOrder()) //Comparator //return Optional<Integer>
				.orElseGet(()->0); //Supplier

		
		System.out.println("Valor Maximo: "+max);
		
		
	}

}
