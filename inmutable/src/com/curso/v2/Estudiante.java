package com.curso.v2;

import java.util.List;

final public class Estudiante {
	
	final private String nombre;
	final private int edad;
	final private StringBuilder matricula;
	final private List<String> materias;
	
	public Estudiante(String nombre, 
			int edad,
			StringBuilder matricula, 
			List<String> materias) {
		
		super();
		this.nombre = nombre;
		this.edad = edad;
		this.matricula = matricula;
		this.materias = materias;
	}

	public String getNombre() {
		return nombre;
	}

	public int getEdad() {
		return edad;
	}

	public StringBuilder getMatricula() {
		return matricula;
	}

	public List<String> getMaterias() {
		return materias;
	}

	@Override
	public String toString() {
		return "Estudiante [nombre=" + nombre + ", edad=" + edad + ", matricula=" + matricula + ", materias=" + materias
				+ "]";
	}


	


}
