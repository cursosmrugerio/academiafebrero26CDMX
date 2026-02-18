package com.curso.v3;

import java.util.*;
import java.util.function.BinaryOperator;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("V3 BinaryOperator");
		
		BinaryOperator<Integer> biFunSuma = (y,z)-> y+z;
		BinaryOperator<Integer> biFunMulti = (pato1,pato2)->pato1*pato2;
		
		List<BinaryOperator<Integer>> operaciones = 
									new ArrayList<>();
		
		operaciones.add(biFunSuma);
		operaciones.add((int1,int2)-> int1/int2);
		operaciones.add(biFunMulti);
		operaciones.add((x,y)->x-y);
		operaciones.add((data1,data2)-> (int)Math.pow(data1, data2));

		show(operaciones);
		
	}
	
	
	static void show(List<BinaryOperator<Integer>> operaciones) {
		for (BinaryOperator<Integer> o : operaciones) {
			System.out.println(o.apply(9, 3));
		}	
	}

}
