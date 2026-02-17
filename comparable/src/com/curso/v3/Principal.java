package com.curso.v3;

class Empleado implements Comparable<Empleado> {
	private String nombre;
	private int edad;
	public Empleado(String nombre, int edad) {
		this.nombre = nombre;
		this.edad = edad;
	}
	@Override
	public String toString() {
		return "Empleado [nombre=" + nombre + ", edad=" + edad + "]";
	}
	@Override
	public int compareTo(Empleado o) { //POR EDAD
		return edad - o.edad;
	}

}

public class Principal {

	public static void main(String[] args) {

		System.out.println("V3");
		Empleado[] empleados = {
				new Empleado("Patrobas",39),
				new Empleado("Enepeto",12),
				new Empleado("Andronico",25),
				new Empleado("Filologo",29)
		};		
		
		//Arrays.sort(empleados); 
		
		for (Empleado e: empleados)
			System.out.println(e);
		
		
	}

}
