package com.curso.v3;

public abstract class Pato {
	
	private String name;
	private ComportamientoVolar cv; //Has a - Interface
	
	public Pato(String name) {
		this.name = name;
		cv = new VolarSi();
	}

	abstract void display();
	
	void volar() {
		cv.ejecutaVuelo();
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public ComportamientoVolar getCv() {
		return cv;
	}

	public void setCv(ComportamientoVolar cv) {
		this.cv = cv;
	}



}
