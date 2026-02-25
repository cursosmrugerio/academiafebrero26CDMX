package com.curso.v1;

import java.util.function.*;


class Empleado{
	
	private String name;

	public Empleado(String name) {
		this.name = name;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return "Empleado [name=" + name + "]";
	}
	
}

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("Class::methodInstance V2");
		
		Empleado emp = new Empleado("Filologo");
		
		Function<Empleado,String> sup = Empleado::getName;
		String nombre = sup.apply(emp);
		System.out.println(nombre);
		
		BiConsumer<Empleado,String> con = Empleado::setName;
		con.accept(emp,"Aristobulo");
		System.out.println(emp);
		
	}

}
