package com.curso.v0;

public class Bees {
	public static void main(String[] args) {
		try {
			new Bees().go();
		} catch (Exception e) {
			System.out.println(e);
		}
	}
	
	synchronized void go() throws InterruptedException  {
		Thread t1 = new Thread();
		t1.start();
		System.out.print("1 "); 
		t1.wait(5000);
		System.out.print("2 "); 
	}
}