package com.curso.v5;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("V5 Interface");
		List<Operacion> operaciones = new ArrayList<>();
		
		operaciones.add(new Suma(8,4));
		operaciones.add(new Suma(6,3));

		show(operaciones);
		
	}
	
	
	static void show(List<Operacion> operaciones) {
		for (Operacion o : operaciones) {
			System.out.println(o.getClass().getSimpleName());
			System.out.println(o.ejecuta());
		}	
	}

}
