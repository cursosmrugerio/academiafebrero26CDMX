package com.curso.v5;

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
		
		Comparator<Empleado> compEdad = new Comparator<>(){ //Anonima
			@Override
			public int compare(Empleado emp1, Empleado emp2) {
				return emp1.edad - emp2.edad;
			}
		};
		
		Comparator<Empleado> compSueldo = new Comparator<>(){ //Anonima
			@Override
			public int compare(Empleado emp1, Empleado emp2) {
				return (int)(emp1.sueldo - emp2.sueldo);
			}
		};
		
		Comparator<Empleado> compNombre = new Comparator<>(){ //Anonima
			@Override
			public int compare(Empleado emp1, Empleado emp2) {
				return emp1.nombre.compareTo(emp2.nombre);
			}
		};

		System.out.println("V5 Clases Anonimas");
		Empleado[] empleados = {
				new Empleado("Patrobas",39,50.0),
				new Empleado("Enepeto",12,30.0),
				new Empleado("Andronico",25,80.0),
				new Empleado("Filologo",29,45.0)
		};	
		
		System.out.println("Ordenar por Edad");
		Arrays.sort(empleados,compEdad); 		
		for (Empleado e: empleados)
			System.out.println(e);
	
		System.out.println("Ordenar por Sueldo");
		Arrays.sort(empleados,compSueldo); 		
		for (Empleado e: empleados)
			System.out.println(e);
		
		System.out.println("Ordenar por Nombre");
		Arrays.sort(empleados,compNombre); 		
		for (Empleado e: empleados)
			System.out.println(e);
	
		
	}

}
