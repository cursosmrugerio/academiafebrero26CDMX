package com.sim.v2;

public class TestClass {
	public static void main(String args[]) {
		try {
			//throw null;
			
			RuntimeException re = null;
			//Exception re = null;
			throw re;
			
		} catch (Exception e) {
			System.out.println(e);
		}
		
		System.out.println("Fin de Programa");
	}
}