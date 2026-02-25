package com.curso.v2;

import java.util.function.*;

class Empleado{
	String nombre;
	int edad;
	
	public Empleado(){}

	public Empleado(String nombre) {
		this.nombre = nombre;
	}

	public Empleado(String nombre, int edad) {
		this.nombre = nombre;
		this.edad = edad;
	}

	@Override
	public String toString() {
		return "Empleado [nombre=" + nombre + ", edad=" + edad + "]";
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
		
		BiFunction<String,Integer,Empleado> bifun =
								(t,v) -> new Empleado(t,v);
		Empleado emp3 = bifun.apply("Epeneto", 10);
		System.out.println(emp3);
		
		
		
	}
}
