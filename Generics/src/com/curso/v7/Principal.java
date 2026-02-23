package com.curso.v7;

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
		showAnimal(listaPato); 
		List<?> lista1 = listaPato;
		//lista1.add(new Pato()); //DON'T COMPILE
		
		List<Perico> listaPerico= new ArrayList<>();
		listaPerico.add(new Perico());
		listaPerico.add(new Perico());
		showAnimal(listaPerico);
		List<?> lista2 = listaPerico;
		
		List<Object> listaObject= new ArrayList<>();
		listaObject.add(new Object());
		listaObject.add(new Perico());
		listaObject.add(Integer.valueOf(1000));
		showAnimal(listaObject);
		List<?> lista3 = listaObject;
		//lista3.add(new Object()); //DON'T COMPILE
	}
	
	//Unbounded Wildcard
	static void showAnimal(List<?> listaAnimal) {
		
		//Trata al collection solo de LECTURA
		//listaAnimal.add(new Pato()); //DON'T COMPILE
		
		for (Object ani : listaAnimal) {
			System.out.println(ani.getClass().getSimpleName());
			if (ani instanceof Perico)
				((Perico)ani).volarPerico();
			if (ani instanceof Pato)
				((Pato)ani).volarPato();
			((Animal)ani).volar();
		}
		
	}

}
