package com.curso.v7;

import java.util.Map;
import java.util.TreeMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Principal {

	public static void main(String[] args) {

		Stream<String> ohMy = Stream.of("lions", "tigers",  "bears");
		
		Map<String, Integer> map1 = ohMy.collect(
							Collectors.toMap(s -> s, String::length));
		
		System.out.println(map1); // {lions=5, bears=5, tigers=6}
		
		System.out.println("*******************");
		
		ohMy = Stream.of("lions", "tigers",  "bears","lions","pato");
		
		Map<Integer, String> map2 = ohMy.collect(
				Collectors.toMap(
					String::length,
					k -> k,
					(s1, s2) -> s1 + "," + s2));// {5=lions,bears,lions, 6=tigers}

				System.out.println(map2.getClass()); //HashMap
				System.out.println(map2);
				
		System.out.println("*******************");		
		
		ohMy = Stream.of("lions", "tigers",  "bears","lions","pato");
		
		TreeMap<Integer, String> map = ohMy.collect(
				Collectors.toMap(
					String::length,
					k -> k,
					(s1, s2) -> s1 + "," + s2,
					TreeMap::new)); 
		
		System.out.println(map.getClass());
		System.out.println(map); 
	
	}

}
