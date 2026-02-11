package com.curso.v0;

import java.util.*;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("VO Anonimas");
		List<Operacion> operaciones = new ArrayList<>();
		
		Operacion ope1 = new Operacion() {
			@Override
			public int ejecuta(int x, int y) {
				System.out.println("Suma");
				return x + y;
			}
		};
		
		Operacion ope2 = new Operacion() {
			@Override
			public int ejecuta(int x, int y) {
				System.out.println("Potencia");
				return (int)Math.pow(x, y);
			}
		};
		
		operaciones.add(ope1);
		operaciones.add(ope2);
		
		operaciones.add(new Operacion() {
			@Override
			public int ejecuta(int x, int y) {
				System.out.println("Multi");
				return x*y;
			}
		});

		show(operaciones);
		
	}
	
	
	static void show(List<Operacion> operaciones) {
		for (Operacion o : operaciones) {
			System.out.println(o.ejecuta(8, 4));
		}	
	}

}
