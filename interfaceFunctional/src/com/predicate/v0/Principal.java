package com.predicate.v0;

public class Principal {
	
	public static void main(String[] args) {
		
		Predicado.and();
		
		Predicado<Integer> pre = i -> true;
		
		pre.or();
	
	}
	

}
