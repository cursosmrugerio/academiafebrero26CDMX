package com.list.v0;

import java.util.*;

public class Principal {

	public static void main(String[] args) {
		
		String[] names = {"Erasto", "Rufo", "Andronico","Epeneto"};
		
		List<String> listNames = Arrays.asList(names);
		
		System.out.println(listNames.getClass().getName());
		
		listNames.set(2, "Filologo");
		//listNames.removeIf(z -> z.contains("a"));
		
		listNames.replaceAll(n -> n.concat("-"+n.length()));
		
		Comparator<String> comp = (u,v) -> u.length() - v.length();
		listNames.sort(comp);
		
		listNames.forEach(System.out::println);

	}

}
