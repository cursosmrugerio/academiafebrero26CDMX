package com.curso.v2;

import java.util.Arrays;
import java.util.Comparator;

class Empleado{
	private String nombre;
	private int edad;
	private double sueldo;
	
	class ComparatorEdad implements Comparator<Empleado>{ //Inner Class
		@Override
		public int compare(Empleado emp1, Empleado emp2) {
			return emp1.edad - emp2.edad;
		}
	}
	
	class ComparatorSueldo implements Comparator<Empleado>{ //Inner Class
		@Override
		public int compare(Empleado emp1, Empleado emp2) {
			return (int)(emp1.sueldo - emp2.sueldo);
		}
	}
	
	class ComparatorNombre implements Comparator<Empleado>{ //Inner Class
		@Override
		public int compare(Empleado emp1, Empleado emp2) {
			return emp1.nombre.compareTo(emp2.nombre);
		}
	}
	
	public Empleado(){}
	
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

		System.out.println("V2");
		Empleado[] empleados = {
				new Empleado("Patrobas",39,50.0),
				new Empleado("Enepeto",12,30.0),
				new Empleado("Andronico",25,80.0),
				new Empleado("Filologo",29,45.0)
		};	
		
		Empleado emp = new Empleado();
		
		Comparator<Empleado> compEdad = emp.new ComparatorEdad();
		System.out.println("Ordenar por Edad");
		Arrays.sort(empleados,compEdad); 		
		for (Empleado e: empleados)
			System.out.println(e);
	
		Comparator<Empleado> compSueldo = emp.new ComparatorSueldo();
		System.out.println("Ordenar por Sueldo");
		Arrays.sort(empleados,compSueldo); 		
		for (Empleado e: empleados)
			System.out.println(e);
		
		Comparator<Empleado> compNombre = emp.new ComparatorNombre();
		System.out.println("Ordenar por Nombre");
		Arrays.sort(empleados,compNombre); 		
		for (Empleado e: empleados)
			System.out.println(e);
	
		
	}

}
