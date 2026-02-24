package com.gen.v0;

public class Suma implements Operacion<Integer,Float,Double> {

	@Override
	public Double ejecuta(Integer x, Float y) {
		double d = x + y;
		return d ;
	}

}
