package com.curso.v1;

import java.util.Random;

public class Principal {

	public static void main(String[] args) {
		
		Ave ave = getAve();
		
		comportamientoVolar(ave);

	}

	static void comportamientoVolar(Ave ave) {
		ave.volar();
		
		if (ave instanceof Pato)
			((Pato)ave).volarPato();
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
