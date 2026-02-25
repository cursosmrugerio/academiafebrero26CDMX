package com.curso.v3;

import java.util.function.Predicate;
import java.math.BigDecimal;

public class Principal {
	
	String lenjuage = "Java"; //Instancia

	public static void main(String[] args) {
		
		String len = "Phyton"; //Local
		
		boolean res = false;

		Predicate<String> pre1 = lenjuage -> lenjuage.contains("v");
		
		res = pre1.test(len);
		System.out.println(res);
		
		res = pre1.test(new Principal().lenjuage);
		System.out.println(res);
		
	}

}
