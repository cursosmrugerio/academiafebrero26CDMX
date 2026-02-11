package com.curso.v1;

import java.util.ArrayList;
import java.util.List;

public class Principal {

	public static void main(String[] args) {

		List<String> listaMaterias = new ArrayList<>();
		listaMaterias.add("Mate");
		listaMaterias.add("Fisica");
		listaMaterias.add("Quimica");
		
		String nombre = "Patrobas";
		int edad = 20;
		StringBuilder matricula = new StringBuilder("XYZ777");

		Estudiante est1 = new Estudiante(nombre,edad,matricula,listaMaterias);
		
		System.out.println(est1);
		
		matricula.append(" 999");
		
		est1.getMatricula().append(" 888");
		
		
		
		System.out.println(est1);
		
		est1.getNombre().concat(" Andronico");
		
		int otraEdad = est1.getEdad();
		
		
		
		
		
		
	}

}
