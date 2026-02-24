package com.predicate.v3;

public class Principal {
	
	public static void main(String[] args) {

		System.out.println(Predicado.<Double>and(
			    d -> {
				System.out.println("paso1");
				return d > 5.0;
  			 }, d -> {
  				System.out.println("paso2");
  				return d > 100.0;
  			 }).probar(50.0));
	
	}
	

}
