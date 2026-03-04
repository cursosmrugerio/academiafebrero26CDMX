package com.inner.v2;

public class B {
	
	String c="B";
	int cc=5;
	
	public static void main(String[] args) {
		A a = new A();
		a.show(); //A //10
		          //B //5
	}

}

class A extends B {
	
	String c="A";
	int cc=10;
	
	void show() {
		System.out.println(super.c);
		System.out.println(super.cc);
	}

}
