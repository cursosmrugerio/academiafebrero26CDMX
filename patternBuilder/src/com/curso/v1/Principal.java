package com.curso.v1;

import java.time.LocalDate;

public class Principal {

	public static void main(String[] args) {

		Task tarea1 = new TaskBuilder(1)
						.build();
		System.out.println(tarea1);
		
		Task tarea2 = new TaskBuilder(2)
						.setName("Investigar POO")
						.setFechaInicio(LocalDate.now())
						.build();
		System.out.println(tarea2);
		
		Task tarea3 = new TaskBuilder(3) //UN SOLO OBJETO TaskBuilder
				.setCompletada(true)
				.setResponsable("Patrobas")
				.setName("Investigar POO")
				.setCategoria("OO")
				.setAsignar("Filologo")
				.setFechaInicio(LocalDate.now())
				.setCalificacion(100.0)
				.setFechaTermino(LocalDate.now())
				.build();
		System.out.println(tarea3);
		
	}

}
