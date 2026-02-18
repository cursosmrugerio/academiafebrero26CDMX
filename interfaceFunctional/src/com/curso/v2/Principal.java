package com.curso.v2;

import java.util.*;
import java.util.function.BiFunction;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("V2 Interface Functional");
		
		BiFunction<Integer,Integer,Integer> biFunSuma = (y,z)-> y+z;
		BiFunction<Integer,Integer,Integer> biFunMulti = (pato1,pato2)->pato1*pato2;
		
		List<BiFunction<Integer,Integer,Integer>> operaciones = 
									new ArrayList<>();
		
		operaciones.add(biFunSuma);
		operaciones.add((int1,int2)-> int1/int2);
		operaciones.add(biFunMulti);
		operaciones.add((x,y)->x-y);
		operaciones.add((data1,data2)-> (int)Math.pow(data1, data2));

		show(operaciones);
		
	}
	
	
	static void show(List<BiFunction<Integer,Integer,Integer>> operaciones) {
		for (BiFunction<Integer,Integer,Integer> o : operaciones) {
			System.out.println(o.apply(9, 3));
		}	
	}

}
