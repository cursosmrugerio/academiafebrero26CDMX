package com.curso.v1;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		List lista= new ArrayList();
		
		lista.add("Patrobas");
		lista.add(new StringBuilder("Patrobas"));
		lista.add(Integer.valueOf(1000));
		lista.add(new Object());
		lista.add(88.88);
		
		for( Object  o : lista) {
			System.out.println("--------");
			System.out.println(o.getClass().getSimpleName());
			if (o instanceof StringBuilder)
				((StringBuilder)o).append(" Tercio");
			System.out.println(o);
		}
	}

}
