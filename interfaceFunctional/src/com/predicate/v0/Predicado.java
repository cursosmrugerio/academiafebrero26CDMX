package com.predicate.v0;

@FunctionalInterface
public interface Predicado <T> {
	
	boolean probar(T t);
	
	static void and() {
		System.out.println("Método and()");
	}
	
	default void or() {
		System.out.println("Método or()");
	}

}
