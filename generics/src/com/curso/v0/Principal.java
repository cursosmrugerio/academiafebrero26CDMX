package com.curso.v0;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		List lista= new ArrayList();
		
		lista.add("Patrobas");
		lista.add(new StringBuilder("Epeneto"));
		lista.add(Integer.valueOf(1000));
		lista.add(new Object());
		lista.add(88.88);
		
		for( Object  o : lista) {
			System.out.println("--------");
			System.out.println(o.getClass().getSimpleName());
			System.out.println(o);
		}
	}

}
