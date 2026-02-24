package com.predicate.v2;

public class Principal {
	
	public static void main(String[] args) {
		
		boolean res;
		
		Predicado<Double> pre1 = d -> {
										System.out.println("paso1");
										return d > 5.0;
									  };
										
		Predicado<Double> pre2 = d -> {
										System.out.println("paso2");
										return d > 100.0;
									  };
		
		Predicado<Double> pre3 = Predicado.and(pre1,pre2);
		
		//res = pre3.probar(50.0);
		res = pre3.probar(500.0);
		System.out.println(res);
		
		//Double d = 5;
		
		
	
	}
	

}
