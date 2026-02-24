package com.predicate.v1;

public class Principal {
	
	public static void main(String[] args) {
		
		Predicado.and();
		
		Predicado<Integer> pre = i -> true;
		
		pre.or();
	
	}
	

}
