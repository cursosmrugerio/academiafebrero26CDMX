package com.curso.v3;

import java.util.Arrays;
import java.util.Comparator;

class Empleado{
	private String nombre;
	private int edad;
	private double sueldo;
	
	static class ComparatorEdad implements Comparator<Empleado>{ //static Nested Class
		@Override
		public int compare(Empleado emp1, Empleado emp2) {
			return emp1.edad - emp2.edad;
		}
	}
	
	static class ComparatorSueldo implements Comparator<Empleado>{ //static Nested  Class
		@Override
		public int compare(Empleado emp1, Empleado emp2) {
			return (int)(emp1.sueldo - emp2.sueldo);
		}
	}
	
	static class ComparatorNombre implements Comparator<Empleado>{ //static Nested  Class
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

		System.out.println("V3 static Nested Class");
		Empleado[] empleados = {
				new Empleado("Patrobas",39,50.0),
				new Empleado("Enepeto",12,30.0),
				new Empleado("Andronico",25,80.0),
				new Empleado("Filologo",29,45.0)
		};	
		
		Comparator<Empleado> compEdad = new Empleado.ComparatorEdad();
		System.out.println("Ordenar por Edad");
		Arrays.sort(empleados,compEdad); 		
		for (Empleado e: empleados)
			System.out.println(e);
	
		Comparator<Empleado> compSueldo = new Empleado.ComparatorSueldo();
		System.out.println("Ordenar por Sueldo");
		Arrays.sort(empleados,compSueldo); 		
		for (Empleado e: empleados)
			System.out.println(e);
		
		Comparator<Empleado> compNombre = new Empleado.ComparatorNombre();
		System.out.println("Ordenar por Nombre");
		Arrays.sort(empleados,compNombre); 		
		for (Empleado e: empleados)
			System.out.println(e);
	
		
	}

}
