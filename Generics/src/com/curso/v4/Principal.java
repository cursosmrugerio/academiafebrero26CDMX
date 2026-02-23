package com.curso.v4;

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
		
		List<Animal> listaAnimal = new ArrayList<>();
		listaAnimal.add(new Perico());
		listaAnimal.add(new Pato());
		listaAnimal.add(new Animal());
		showAnimal(listaAnimal);

		List<Pato> listaPato= new ArrayList<>();
		listaPato.add(new Pato());
		listaPato.add(new Pato());
		//showAnimal(listaPato); // DON'T COMPILE
		//List<Animal> listaAnimal2 = listaPato; // DON'T COMPILE

		List<Perico> listaPerico= new ArrayList<>();
		listaPerico.add(new Perico());
		listaPerico.add(new Perico());
		//showAnimal(listaPerico); // DON'T COMPILE
		//List<Animal> listaAnimal2 = listaPerico; // DON'T COMPILE
	}
	
	static void showAnimal(List<Animal> listaAnimal) {
		for (Animal ani : listaAnimal) {
			System.out.println(ani.getClass().getSimpleName());
			if (ani instanceof Perico)
				((Perico)ani).volarPerico();
			if (ani instanceof Pato)
				((Pato)ani).volarPato();
			ani.volar();
		}
	}

}
