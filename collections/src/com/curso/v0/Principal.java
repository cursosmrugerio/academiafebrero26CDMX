package com.curso.v0;

import java.util.*;

public class Principal {

	public static void main(String[] args) {

		Collection<String> names = new ArrayList<>();
		
		names.add("Patrobas");
		names.add("Herodion");
		names.add("Estaquis");
		names.add("Trifosa");
		names.add("Asincrito");
		names.add("Jason");
		
		//Predicate<String>
		names.removeIf(z -> z.contains("a"));
		
		//Consumer<String>
		names.forEach(name -> System.out.println(name));
		
		//Method Reference
		//names.forEach(System.out::println);
		
	}

}
