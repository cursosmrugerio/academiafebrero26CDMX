package com.curso.v0;

public class NewClass {
	
	private Object o; //HAS-A

	void doSomething(Object s) {
		o = s;
	}

	public static void main(String args[]) {
		Object obj = new Object(); // 1  //GARBAGE COLLECTOR
		
		
		NewClass tc = new NewClass(); // 2
		tc.doSomething(obj); // 3 
		obj = new Object(); // 4 
		obj = null; // 5  
		tc.doSomething(obj); // 6  
	}
}
