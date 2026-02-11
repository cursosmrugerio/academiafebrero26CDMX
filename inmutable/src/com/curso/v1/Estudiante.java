package com.curso.v1;

import java.util.List;

final public class Estudiante {
	
	final private String nombre; //INMUTABLE
	final private int edad; //PRIMITIVO
	final private StringBuilder matricula; //MUTABLE
	final private List<String> materias; //INMUTABLE
	
	public Estudiante(String nombre, 
			int edad,
			StringBuilder matricula, 
			List<String> materias) {
		
		super();
		this.nombre = nombre;
		this.edad = edad;
		this.matricula = new StringBuilder(matricula);
		this.materias = materias;
	}

	public String getNombre() {
		return nombre;
	}

	public int getEdad() {
		return edad;
	}

	public StringBuilder getMatricula() {
		return new StringBuilder(matricula);
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
