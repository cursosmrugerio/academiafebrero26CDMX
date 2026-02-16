package com.sim.v1;

class SomeException extends Exception {
}

class OtherException extends SomeException{
}

//in file A.java
class A {
	protected void m() throws SomeException {
	}
}

//in file B.java
class B extends A {
	@Override
	public void m() { //Override method elimina la exception
	//public void m() throws SomeException { //Misma exception
	//public void m() throws OtherException { //Subclase de la exception
	}
}

//in file TestClass.java
public class TestClass {
	public static void main(String[] args) {
		// insert code here. //1
		
		A a = new B(); 
		((B)a).m();
		
		Object o = new B(); 
		((B)o).m();
		
		// A a = new B(); 
		// a.m(); //NO COMPILA
		
		// Superclase - Subclase //DEBER SER
		// B b = new A(); //NOT COMPILE 
		// b.m();
		
		A aa = new B(); 
		try {
			aa.m();
		} catch (SomeException e) {
			e.printStackTrace();
		}
	}
}
