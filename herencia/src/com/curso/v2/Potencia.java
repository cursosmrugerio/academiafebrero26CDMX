package com.curso.v2;

public class Potencia extends Operacion {

	@Override
	int ejecuta(int x, int y) {
		return (int)Math.pow(x, y) ;
	}

}
