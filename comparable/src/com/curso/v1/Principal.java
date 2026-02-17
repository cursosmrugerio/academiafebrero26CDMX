package com.curso.v1;

import java.util.Arrays;

class Empleado{
	private String nombre;
	public Empleado(String nombre) {
		this.nombre = nombre;
	}
	@Override
	public String toString() {
		return nombre;
	}
}

public class Principal {

	public static void main(String[] args) {

		Empleado[] empleados = {
				new Empleado("Patrobas"),
				new Empleado("Enepeto"),
				new Empleado("Andronico"),
				new Empleado("Filologo")
		};		
		
		Arrays.sort(empleados); //RuntimeException
		
		System.out.println(Arrays.toString(empleados));
		
		
	}

}
