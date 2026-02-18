package com.curso.v1;

public abstract class Pato {
	
	String name;
	ComportamientoVolar cv; //Has a - Interface

	public Pato(String name) {
		this.name = name;
	}

	abstract void display();
	
	void volar() {
		cv.ejecutaVuelo();
	}

}
