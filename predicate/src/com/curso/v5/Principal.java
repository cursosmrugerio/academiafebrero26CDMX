package com.curso.v5;

import java.util.function.Predicate;
import java.math.BigDecimal;

public class Principal {
	
	static String len0 = "C++"; //Static
	String len1 = "Java"; //Instancia

	public static void main(String[] args) {
		
		Principal prin = new Principal();
		
		//Effective Final
		String len2 = "Phyton"; //Local
		//len2 = "Javascript";
		
		boolean res = false;

		//En tu lambdas puedes usar variables locales
		//pero DEBEN SER efective final
		Predicate<String> pre1 = x -> x.equals(len2); //Uso local
		System.out.println(pre1.test("Java")); //false
		
		prin.len1 = "Rust";
		
		Predicate<String> pre2 = x -> x.equals(prin.len1);
		System.out.println(pre2.test("Java")); //true //false
		
		len0 = "PHP";
		
		Predicate<String> pre3 = x -> x.equals(len0);
		System.out.println(pre3.test("Java")); //true //false
		
		
	}

}
