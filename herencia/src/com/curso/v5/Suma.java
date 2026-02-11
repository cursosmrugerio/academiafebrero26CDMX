package com.curso.v5;

public class Suma implements Operacion {
	
	int x;
	int y;
	
	Suma(int x, int y){
		this.x = x;
		this.y = y;
	}
	
	public int ejecuta() {
		return x+y;
	}


}
