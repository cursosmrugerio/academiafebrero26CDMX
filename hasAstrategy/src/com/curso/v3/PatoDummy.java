package com.curso.v3;

public class PatoDummy extends Pato {
	
	PatoDummy(String nombre){
		super(nombre);
		setCv(new VolarNo());
	}
	
	void display() {
		System.out.println("Pato Dummy "+ getName());
	}

}
