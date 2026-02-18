package com.curso.v3;

public class PatoSilvestre extends Pato {
	
	PatoSilvestre(String nombre){
		super(nombre);
	}
	
	void display() {
		System.out.println("Pato Silvestre " + getName());
	}

}
