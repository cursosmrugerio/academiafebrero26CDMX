package com.inner.v1;

public class B {
	
	String c="B";
	int cc=5;
	
	
	class A {
		
		String c="A";
		int cc=10;
		
		void show() {
			System.out.println(B.this.c);
			System.out.println(B.this.cc);
		}

	}
	
	public static void main(String[] args) {
		//B b = new B();
		A a = new B().new A();
		a.show(); //B //5
	}

}
