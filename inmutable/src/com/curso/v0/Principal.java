package com.curso.v0;

import java.util.ArrayList;
import java.util.List;

public class Principal {

	public static void main(String[] args) {

		List<String> listaMaterias = new ArrayList<>();
		listaMaterias.add("Mate");
		listaMaterias.add("Fisica");
		listaMaterias.add("Quimica");

		Estudiante est1 = new Estudiante("Patrobas",20,listaMaterias);
		
		System.out.println(est1);
		
		
	}

}
