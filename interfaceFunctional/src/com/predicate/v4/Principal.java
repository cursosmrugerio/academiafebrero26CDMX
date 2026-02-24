package com.predicate.v4;

public class Principal {
	
	public static void main(String[] args) {

		System.out.println(Predicado.<Double>and(
			    d -> d > 5.0
  			  , d -> d > 100.0
  			 ).probar(50.0));
	
	}
	

}
