package com.curso.v1;

import java.util.function.*;

class Empleado{
	String nombre;
	
	public Empleado(){}

	public Empleado(String nombre) {
		this.nombre = nombre;
	}
	
}

public class Principal {
	public static void main(String[] args) {
		Supplier<Empleado> sup = ()->new Empleado();
		Empleado emp1 = sup.get();
		System.out.println(emp1);
		
		Function<String,Empleado> fun = n->new Empleado(n);
		Empleado emp2 = fun.apply("Patrobas");
		System.out.println(emp2);
		
		
		
		
	}
}
