package com.curso.v2;

public class Principal {

	public static void main(String[] args) {
		
		ComportamientoVolar cv1 = new VolarSi();
		ComportamientoVolar cv2 = new VolarNo();
		ComportamientoVolar cv3 = new VolarAleatorio();
		
		Pato pato = new PatoSilvestre("Donald");
		pato.display();
		pato.cv = cv3; //Aleatorio Volar
		pato.volar();
		
		pato.display();
		pato.cv = cv2; //No Volar
		pato.volar();
		
		pato.display();
		pato.cv = cv1; //Si Volar
		pato.volar();

	}

}
