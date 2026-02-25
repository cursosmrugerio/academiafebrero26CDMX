package com.curso.v4;

import java.util.function.Predicate;
import java.math.BigDecimal;

public class Principal {
	
	static String len0 = "C++"; //Static
	String len1 = "Java"; //Instancia

	public static void main(String[] args) {
		
		//Effective Final
		String len2 = "Phyton"; //Local
		//len2 = "Javascript";
		
		boolean res = false;

		//En tu lambdas puedes usar variables locales
		//pero DEBEN SER efective final
		Predicate<String> pre1 = x -> x.equals(len2); //Uso local
		
		System.out.println(pre1.test("Java")); //false
		
		
	}

}
