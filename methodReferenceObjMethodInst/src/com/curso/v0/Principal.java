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
		
		//Effective Final
		Empleado emp = new Empleado("Filologo");
		
		Supplier<String> sup = () -> emp.getName();
		String nombre = sup.get();
		System.out.println(nombre);
		
		Consumer<String> con = name -> emp.setName(name);
		con.accept("Aristobulo");
		System.out.println(emp);
		
	}

}
