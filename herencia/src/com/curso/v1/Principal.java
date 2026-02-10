package com.curso.v1;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		List<Operacion> operaciones = new ArrayList<>();
		
		Operacion ope1 = new Suma();
		Operacion ope2 = new Division();
		Operacion ope3 = new Multiplicacion();
		
		operaciones.add(ope3);
		operaciones.add(ope1);
		operaciones.add(ope2);

		show(operaciones);
		
	}
	
	
	static void show(List<Operacion> operaciones) {
		for (Operacion o : operaciones) {
			System.out.println(o.getClass().getSimpleName());
			System.out.println(o.ejecuta(8, 4));
		}	
	}

}
