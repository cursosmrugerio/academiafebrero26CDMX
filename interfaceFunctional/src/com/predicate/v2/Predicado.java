package com.predicate.v2;

@FunctionalInterface
public interface Predicado <T> {
	
	boolean probar(T t);
	
	static <W> Predicado<W> and(Predicado<W> pre1, Predicado<W> pre2) {
		System.out.println("Método static and()");
		//Predicado<W> pre = x -> pre1.probar(x) && pre2.probar(x);
		return x -> pre1.probar(x) && pre2.probar(x);
	}

}
