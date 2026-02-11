package com.curso.v4;

public abstract class Operacion  {
	
	int x;
	int y;
	
	static int contador;
	
	Operacion(int x, int y){
		this.x = x;
		this.y = y;
		contador++;
	}
	
	abstract int ejecuta();
	
	public String toString() {
		return this.getClass().getName()+" x:"+x+", y:"+y;
	}
	
	static void showContador() {
		System.out.println("Contador: "+contador);
	}
	
}
