package com.curso.v3;

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
		System.out.println("Method Reference");
		Supplier<Empleado> sup = Empleado::new;
		Empleado emp1 = sup.get();
		System.out.println(emp1);
		
		Function<String,Empleado> fun = Empleado::new;
		Empleado emp2 = fun.apply("Patrobas");
		System.out.println(emp2);
		
		BiFunction<String,Integer,Empleado> bifun = Empleado::new;
		Empleado emp3 = bifun.apply("Epeneto", 10);
		System.out.println(emp3);
		
	}
}
