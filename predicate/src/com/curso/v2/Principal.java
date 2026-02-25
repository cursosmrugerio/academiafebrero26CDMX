package com.curso.v2;

import java.util.function.Predicate;
import java.math.BigDecimal;

public class Principal {
	
	String lenjuage = "Java"; //Instancia

	public static void main(String[] args) {
		
		String lenjuage = "Phyton"; //Local
		
		boolean res = false;

		Predicate<String> pre1 = pato -> pato.contains("v");
		
		res = pre1.test(lenjuage);
		System.out.println(res);
		
		res = pre1.test(new Principal().lenjuage);
		System.out.println(res);
		
	}

}
