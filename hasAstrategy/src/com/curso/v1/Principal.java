package com.curso.v1;

public class Principal {

	public static void main(String[] args) {
		
		ComportamientoVolar cv1 = new VolarSi();
		ComportamientoVolar cv2 = new VolarNo();
		ComportamientoVolar cv3 = new VolarAleatorio();
		
		Pato pato1 = new PatoDummy("Yellow");
		pato1.display();
		pato1.cv = cv2; //No Volar
		pato1.volar();
		
		Pato pato2 = new PatoSilvestre("Lucas");
		pato2.display();
		pato2.cv = cv1; //Si Volar
		pato2.volar();
		
		Pato pato3 = new PatoSilvestre("Donald");
		pato3.display();
		pato3.cv = cv3; //Aleatorio Volar
		pato3.volar();

	}

}
