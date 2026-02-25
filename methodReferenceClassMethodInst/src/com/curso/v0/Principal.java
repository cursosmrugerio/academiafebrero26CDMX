package com.curso.v0;

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
		System.out.println("Class::methodInstance");
		
		Empleado emp = new Empleado("Filologo");
		
		Function<Empleado,String> sup = (employee) -> employee.getName();
		String nombre = sup.apply(emp);
		System.out.println(nombre);
		
		BiConsumer<Empleado,String> con = (employee,name) -> employee.setName(name);
		con.accept(emp,"Aristobulo");
		System.out.println(emp);
		
	}

}
