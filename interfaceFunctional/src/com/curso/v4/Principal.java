package com.curso.v4;

import java.util.*;
import java.util.function.IntBinaryOperator;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("V4 IntBinaryOperator");
		
		IntBinaryOperator biFunSuma = (y,z)-> y+z;
		IntBinaryOperator biFunMulti = (pato1,pato2)->pato1*pato2;
		
		List<IntBinaryOperator> operaciones = 
									new ArrayList<>();
		
		operaciones.add(biFunSuma);
		operaciones.add((int1,int2)-> int1/int2);
		operaciones.add(biFunMulti);
		operaciones.add((x,y)->x-y);
		operaciones.add((data1,data2)-> (int)Math.pow(data1, data2));

		show(operaciones);
		
	}
	
	
	static void show(List<IntBinaryOperator> operaciones) {
		for (IntBinaryOperator o : operaciones) {
			System.out.println(o.applyAsInt(9, 3));
		}	
	}

}
