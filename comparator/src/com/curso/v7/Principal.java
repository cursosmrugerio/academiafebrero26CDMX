package com.curso.v7;

import java.util.Arrays;
import java.util.Comparator;

class Empleado{
	String nombre;
	int edad;
	double sueldo;
	
	public Empleado(String nombre, int edad, double sueldo) {
		this.nombre = nombre;
		this.edad = edad;
		this.sueldo = sueldo;
	}

	@Override
	public String toString() {
		return "Empleado [nombre=" + nombre + ", edad=" + edad + ", sueldo=" + sueldo + "]";
	}
}

public class Principal {

	public static void main(String[] args) {

		System.out.println("V7 Lambdas");
		Empleado[] empleados = {
				new Empleado("Patrobas",39,50.0),
				new Empleado("Enepeto",12,30.0),
				new Empleado("Andronico",25,80.0),
				new Empleado("Filologo",29,45.0)
		};	
		
		System.out.println("Ordenar por Edad");
		Arrays.sort(empleados, (emp1,emp2) -> emp1.edad-emp2.edad); 
		
		for (Empleado e: empleados)
			System.out.println(e);
	
		System.out.println("Ordenar por Sueldo");
		Arrays.sort(empleados, (x,y) -> (int)(x.sueldo-y.sueldo)); 		
		
		for (Empleado e: empleados)
			System.out.println(e);
		
		System.out.println("Ordenar por Nombre");
		Arrays.sort(empleados, (pato1,pato2) -> pato1.nombre.compareTo(pato2.nombre)); 		
		for (Empleado e: empleados)
			System.out.println(e);
	
		
	}

}
