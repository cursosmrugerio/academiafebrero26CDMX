package com.curso.v5;

enum DiaSemana {
	LUNES("Bajo"){
		@Override
		void getVisitantes() {
			System.out.println("Visitantes baja demanda");
		}
	},
	MARTES("Bajo"){
		@Override
		void getVisitantes() {
			System.out.println("Visitantes baja demanda");
		}
	},
	MIERCOLES("Bajo"){
		@Override
		void getVisitantes() {
			System.out.println("Visitantes baja demanda");
		}
	},
	JUEVES("Medio"){
		@Override
		void getVisitantes() {
			System.out.println("Visitantes media demanda");
		}
	},
	VIERNES("Medio"){
		@Override
		void getVisitantes() {
			System.out.println("Visitantes media demanda");
		}
	},
	SABADO("Alto"){
		@Override
		void getVisitantes() {
			System.out.println("Visitantes alta demanda");
		}
	},
	DOMINGO("Alto"){
		@Override
		void getVisitantes() {
			System.out.println("Visitantes alta demanda");
		}
	};
	
	private String visitantes;
	
	DiaSemana(String visitantes) {
		this.visitantes = visitantes;
	}
	
	abstract void getVisitantes();
	
}

public class Principal {

	public static void main(String[] args) {
		
		DiaSemana hoy = DiaSemana.MIERCOLES;
		
		System.out.println(hoy);
		hoy.getVisitantes();

	}

}
