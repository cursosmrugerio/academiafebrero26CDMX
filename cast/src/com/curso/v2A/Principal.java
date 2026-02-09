package com.curso.v2A;

import java.util.Random;

public class Principal {

	public static void main(String[] args) {
		
		Ave ave = getAve();
		
		comportamientoVolar(ave);

	}

	static void comportamientoVolar(Ave ave) {
		ave.volar();
		((Pato)ave).volarPato(); //ClassCastExcpetion
	}
	
	private static Ave getAve() {
		
		Ave[] aves = {new Pato(), 
					  new Ave(), 
					  new Murcielago(),
					  new Perico(),
					  new Pinguino()
		};
		
		int aleatorio = new Random().nextInt(aves.length);
		
		return aves[aleatorio];
	}

}
