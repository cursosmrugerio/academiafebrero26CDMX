package com.curso.v2;

import java.util.*;

class Animal{
	void volar(){
		System.out.println("Volar Animal");
	}
}

class Pato extends Animal{
	void volarPato(){
		System.out.println("Volar Pato");
	}
}

class Perico extends Animal{
	void volarPerico(){
		System.out.println("Volar Perico");
	}
}

public class Principal {
	
	public static void main(String[] args) {
		List lista= new ArrayList();
		
		lista.add(new Pato());
		lista.add(new Pato());
		lista.add(new Pato());
		lista.add(new Perico());

		for( Object pato : lista) {
			((Pato)pato).volarPato();
		}
	}

}
