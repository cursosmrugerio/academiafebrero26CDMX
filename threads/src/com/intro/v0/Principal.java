package com.intro.v0;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("main: Inicio Programa");
		
		MiHilo hilo1 = new MiHilo("Hilo1",5);
		hilo1.run();
		
		MiHilo hilo2 = new MiHilo("Hilo2",8);
		hilo2.run();
		
		System.out.println("main: Fin de Programa");
	}

}
