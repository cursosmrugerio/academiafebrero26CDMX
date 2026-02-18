package com.curso.v1;

import java.time.LocalDate;

public class Task {
	
	private int id;
	private String name;
	private LocalDate fechaInicio;
	private LocalDate fechaTermino;
	private String responsable;
	private String asignar;
	private boolean completada;
	private double calificacion;
	private String categoria;
	
	public Task(int id, 
			String name, 
			LocalDate fechaInicio, 
			LocalDate fechaTermino, 
			String responsable, 
			String asignar,
			boolean completada, 
			double calificacion, 
			String categoria) {
		
		this.id = id;
		this.name = name;
		this.fechaInicio = fechaInicio;
		this.fechaTermino = fechaTermino;
		this.responsable = responsable;
		this.asignar = asignar;
		this.completada = completada;
		this.calificacion = calificacion;
		this.categoria = categoria;
	}
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public LocalDate getFechaInicio() {
		return fechaInicio;
	}

	public void setFechaInicio(LocalDate fechaInicio) {
		this.fechaInicio = fechaInicio;
	}

	public LocalDate getFechaTermino() {
		return fechaTermino;
	}

	public void setFechaTermino(LocalDate fechaTermino) {
		this.fechaTermino = fechaTermino;
	}

	public String getResponsable() {
		return responsable;
	}

	public void setResponsable(String responsable) {
		this.responsable = responsable;
	}

	public String getAsignar() {
		return asignar;
	}

	public void setAsignar(String asignar) {
		this.asignar = asignar;
	}

	public boolean isCompletada() {
		return completada;
	}

	public void setCompletada(boolean completada) {
		this.completada = completada;
	}

	public double getCalificacion() {
		return calificacion;
	}

	public void setCalificacion(double calificacion) {
		this.calificacion = calificacion;
	}

	public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}

	@Override
	public String toString() {
		return "Task [id=" + id + ", name=" + name + ", fechaInicio=" + fechaInicio + ", fechaTermino=" + fechaTermino
				+ ", responsable=" + responsable + ", asignar=" + asignar + ", completada=" + completada
				+ ", calificacion=" + calificacion + ", categoria=" + categoria + "]";
	}

	

}
