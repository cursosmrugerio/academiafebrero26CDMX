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
		
		System.out.println("V1");
		
		Empleado emp = new Empleado("Patrobas");
		
		//Supplier<String> sup = () -> emp.getName();
		Supplier<String> sup = emp::getName;
		String nombre = sup.get();
		System.out.println(nombre);
		
		//Consumer<String> con = name -> emp.setName(name);
		Consumer<String> con = emp::setName;
		con.accept("Aristobulo");
		System.out.println(emp);
		
	}

}
