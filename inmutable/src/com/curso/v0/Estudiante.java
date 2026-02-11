package com.curso.v0;

import java.util.List;

public class Estudiante {
	
	private String nombre;
	private int edad;
	private List<String> materias;
	
	public Estudiante(String nombre, int edad, List<String> materias) {
		super();
		this.nombre = nombre;
		this.edad = edad;
		this.materias = materias;
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

	public List<String> getMaterias() {
		return materias;
	}

	public void setMaterias(List<String> materias) {
		this.materias = materias;
	}

	@Override
	public String toString() {
		return "Estudiante [nombre=" + nombre + ", edad=" + edad + ", materias=" + materias + "]";
	}
	
	
	

}
