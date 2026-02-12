package com.curso.v1;

class Ave extends Object{}

class Pato extends Ave{}

public class TestClass2 {
	public void method(Object o) {
		System.out.println("Object Version");
	}

	public void method(Ave s) {
		System.out.println("Ave Version");
	}

	public void method(Pato s) {
		System.out.println("Pato Version");
	}
	
//	public void method(String string) {
//		System.out.println("String Version");
//	}

	public static void main(String args[]) {
		TestClass2 tc = new TestClass2();
		tc.method(null);
	}
}