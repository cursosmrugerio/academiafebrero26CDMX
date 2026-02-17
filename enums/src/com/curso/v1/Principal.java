package com.curso.v1;

enum DiaSemana {
	LUNES,MARTES,MIERCOLES,JUEVES,VIERNES,
	SABADO,DOMINGO
}

public class Principal {

	public static void main(String[] args) {
		
		DiaSemana hoy = DiaSemana.DOMINGO;
		
		switch(hoy) {
		
		case LUNES: System.out.println("lunes");
			break;
		case MARTES: System.out.println("martes");
			break;
		case MIERCOLES,JUEVES: System.out.println("miercoles,jueves");
			break;
		default: System.out.println("otro dia");
		}

	}

}
