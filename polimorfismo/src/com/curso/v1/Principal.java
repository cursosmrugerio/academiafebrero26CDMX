package com.curso.v1;

public class Principal {

	public static void main(String[] args) {
		Ave ave;
		
		ave = new Perico();
		ave.volar();
		ave = new Pinguino();
		ave.volar(); 
		ave = new Pato();
		ave.volar();
	}

}
