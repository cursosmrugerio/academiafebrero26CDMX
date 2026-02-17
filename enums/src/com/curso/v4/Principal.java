package com.curso.v4;

enum DiaSemana {
	LUNES("Bajo"),
	MARTES("Bajo"),
	MIERCOLES("Bajo"),
	JUEVES("Medio"),
	VIERNES("Medio"),
	SABADO("Alto"),
	DOMINGO("Alto");
	
	String visitantes;
	
	DiaSemana(String visitantes) {
		this.visitantes = visitantes;
	}
}

public class Principal {

	public static void main(String[] args) {
		
		DiaSemana hoy = DiaSemana.SABADO;
		
		System.out.println(hoy);
		System.out.println(hoy.visitantes);

	}

}
