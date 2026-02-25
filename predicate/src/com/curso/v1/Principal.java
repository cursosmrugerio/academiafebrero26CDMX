package com.curso.v1;

import java.util.function.Predicate;
import java.math.BigDecimal;

public class Principal {

	public static void main(String[] args) {
		
		String lenjuage = "Phyton";
		
		boolean res = false;

		Predicate<String> pre1 = pato -> pato.contains("v");
		
		res = pre1.test(lenjuage);
		
		System.out.println(res);
		
	}

}
