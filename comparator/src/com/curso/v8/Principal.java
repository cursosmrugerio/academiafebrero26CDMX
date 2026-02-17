package com.curso.v8;

import java.util.Arrays;
import java.util.Comparator;

class Empleado{
	private String nombre;
	private int edad;
	private double sueldo;
	
	public Empleado(String nombre, int edad, double sueldo) {
		this.nombre = nombre;
		this.edad = edad;
		this.sueldo = sueldo;
	}

	@Override
	public String toString() {
		return "Empleado [nombre=" + nombre + ", edad=" + edad + ", sueldo=" + sueldo + "]";
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public int getEdad() {
		return edad;
	}
	public void setEdad(int edad) {
		this.edad = edad;
	}
	public double getSueldo() {
		return sueldo;
	}
	public void setSueldo(double sueldo) {
		this.sueldo = sueldo;
	}
}

public class Principal {

	public static void main(String[] args) {

		System.out.println("V8 Functional");
		Empleado[] empleados = {
				new Empleado("Patrobas",39,50.0),
				new Empleado("Enepeto",39,50.0),
				new Empleado("Andronico",39,30.0),
				new Empleado("Filologo",29,45.0)
		};	
		
		Comparator<Empleado> comp = 
				Comparator.comparingInt(Empleado::getEdad)
				.thenComparingDouble(Empleado::getSueldo)
				.thenComparing(Empleado::getNombre)
				.reversed();
		
		//Filologo , Andronico , Epeneto , Patrobas
		//Patrobas, Epeneto, Andronico, Filologo
		
		Arrays.sort(empleados, comp);
		
		for (Empleado e: empleados)
			System.out.println(e);
	
		
	}

}
