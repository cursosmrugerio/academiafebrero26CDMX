package com.curso.v3;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("V3 Interface");
		List<Operacion> operaciones = new ArrayList<>();
		
		operaciones.add(new Suma());
		operaciones.add(new Division());
		operaciones.add(new Multiplicacion());
		operaciones.add(new Resta());
		operaciones.add(new Potencia());

		show(operaciones);
		
	}
	
	
	static void show(List<Operacion> operaciones) {
		for (Operacion o : operaciones) {
			System.out.println(o.getClass().getSimpleName());
			System.out.println(o.ejecuta(8, 4));
		}	
	}

}
