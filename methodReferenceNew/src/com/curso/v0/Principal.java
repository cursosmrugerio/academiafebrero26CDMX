package com.curso.v0;

import java.util.function.Supplier;

class Empleado{
	
}

public class Principal {
	public static void main(String[] args) {
		Supplier<Empleado> sup = ()->new Empleado();
		Empleado emp1 = sup.get();
		System.out.println(emp1);
		
		
	}
}
