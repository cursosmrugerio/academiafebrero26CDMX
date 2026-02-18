package com.curso.v1;

import java.time.LocalDate;

public class TaskBuilder {
	
	private int id;
	private String name;
	private LocalDate fechaInicio;
	private LocalDate fechaTermino;
	private String responsable;
	private String asignar;
	private boolean completada;
	private double calificacion;
	private String categoria;
	
	public TaskBuilder(int id) {
		this.id = id;
	}

	public TaskBuilder setName(String name) {
		this.name = name;
		return this;
	}

	public TaskBuilder setFechaInicio(LocalDate fechaInicio) {
		this.fechaInicio = fechaInicio;
		return this;
	}

	public TaskBuilder setFechaTermino(LocalDate fechaTermino) {
		this.fechaTermino = fechaTermino;
		return this;
	}

	public TaskBuilder setResponsable(String responsable) {
		this.responsable = responsable;
		return this;
	}

	public TaskBuilder setAsignar(String asignar) {
		this.asignar = asignar;
		return this;
	}

	public TaskBuilder setCompletada(boolean completada) {
		this.completada = completada;
		return this;
	}

	public TaskBuilder setCalificacion(double calificacion) {
		this.calificacion = calificacion;
		return this;
	}

	public TaskBuilder setCategoria(String categoria) {
		this.categoria = categoria;
		return this;
	}
	
	Task build() {
		return new Task(id,
				name,
				fechaInicio,
				fechaTermino,
				responsable,
				asignar,
				completada,
				calificacion,
				categoria);
	}

}
