package com.curso.v0;

import java.util.function.Predicate;
import java.math.BigDecimal;

public class Principal {

	public static void main(String[] args) {
		
		boolean res = false;

		Predicate<String> pre1 = w -> w.contains("v");
		
		res = pre1.test("Phyton");
		System.out.println(res);
		
		res = pre1.test("Java");
		System.out.println(res);
		
		Predicate<BigDecimal> pre2 = x -> x.equals(new BigDecimal(4.0));
		res = pre2.test(new BigDecimal(4.0));
		System.out.println("BigDecimal: "+res);
		
	}

}
