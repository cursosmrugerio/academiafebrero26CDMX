package com.curso.v0;

enum DiaSemana {
	LUNES,
	MARTES,
	MIERCOLES,
	JUEVES,
	VIERNES,
	SABADO,
	DOMINGO
}

public class Principal {

	public static void main(String[] args) {
		
		DiaSemana hoy = DiaSemana.MARTES;
		
		System.out.println(hoy);

	}

}
