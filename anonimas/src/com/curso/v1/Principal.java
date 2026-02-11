package com.curso.v1;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("V1 Labdas");
		List<Operacion> operaciones = new ArrayList<>();
		
		Operacion ope1 = (x,y) -> x + y;
		
		Operacion ope2 = (w,q) -> (int)Math.pow(w, q);
			
		operaciones.add(ope1);
		operaciones.add(ope2);
		
		operaciones.add((pato1, pato2) -> pato1 * pato2);

		show(operaciones);
		
	}
	
	
	static void show(List<Operacion> operaciones) {
		for (Operacion o : operaciones) {
			System.out.println(o.ejecuta(9, 3));
		}	
	}

}
