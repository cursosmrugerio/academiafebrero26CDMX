package com.gen.v1;

public class Suma<T extends Number,U extends Number> 
					implements Operacion<T ,U> {

	@Override
	public Number ejecuta(T t, U u) {
		
		double d1 = t.doubleValue();
		double d2 = u.doubleValue();
		
		return d1 + d2;
	}

	
	

}
