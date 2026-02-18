package com.curso.v1;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("V1 Interface Functional");
		List<Operacion> operaciones = new ArrayList<>();
		
		operaciones.add((y,z)-> y+z);
		operaciones.add((int1,int2)-> int1/int2);
		operaciones.add((pato1,pato2)->pato1*pato2);
		operaciones.add((x,y)->x-y);
		operaciones.add((data1,data2)-> (int)Math.pow(data1, data2));

		show(operaciones);
		
	}
	
	
	static void show(List<Operacion> operaciones) {
		for (Operacion o : operaciones) {
			System.out.println(o.ejecuta(8, 4));
		}	
	}

}
