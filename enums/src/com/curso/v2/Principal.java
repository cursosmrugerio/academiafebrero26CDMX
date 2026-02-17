package com.curso.v2;

enum DiaSemana {
	LUNES,MARTES,MIERCOLES,JUEVES,VIERNES,
	SABADO,DOMINGO
}

public class Principal {

	public static void main(String[] args) {
		
		for(DiaSemana ds : DiaSemana.values()) {
			System.out.print(ds); //enum
			System.out.print(" "+ds.ordinal());
			System.out.println(" "+ds.name()); //string
		}

	}

}
