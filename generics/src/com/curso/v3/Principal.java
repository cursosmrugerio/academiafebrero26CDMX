package com.curso.v3;

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
		List<Pato> lista= new ArrayList<>();
		
		lista.add(new Pato());
		lista.add(new Pato());
		lista.add(new Pato());
		//lista.add(new Perico());

		for(Pato pato : lista) {
			pato.volarPato();
		}
		
		System.out.println("********");
		
		List<Perico> listaPerico= new ArrayList<>();
		
		listaPerico.add(new Perico());
		listaPerico.add(new Perico());
		listaPerico.add(new Perico());
		//listaPerico.add(new Pato()); 
		
		for(Perico per : listaPerico) {
			per.volarPerico();
		}
		System.out.println("********");
		
		List<Animal> listaAnimal = new ArrayList<>();
		
		listaAnimal.add(new Perico());
		listaAnimal.add(new Pato());
		listaAnimal.add(new Animal());
		
		for(Animal ani : listaAnimal) {
			if (ani instanceof Perico)
				((Perico)ani).volarPerico();
			
			if (ani instanceof Pato p) //Pattern Match Java 14
				p.volarPato();
			
			if (ani instanceof Animal a)
				a.volar();
		}
	}

}
