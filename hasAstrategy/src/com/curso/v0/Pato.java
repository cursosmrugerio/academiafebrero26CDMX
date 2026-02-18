package com.curso.v0;

public abstract class Pato {
	
	private String name;

	public Pato(String name) {
		this.name = name;
	}

	abstract void display();
	
	void volar() {
		System.out.println("Pato volar");
	}

}
