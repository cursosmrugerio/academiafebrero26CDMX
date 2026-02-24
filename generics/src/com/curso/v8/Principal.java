package com.curso.v8;

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
		//showAnimal(listaPato); 
		
		List<Perico> listaPerico= new ArrayList<>();
		listaPerico.add(new Perico());
		listaPerico.add(new Perico());
		//showAnimal(listaPerico);
		
		List<Object> listaObject= new ArrayList<>();
		listaObject.add(new Object());
		listaObject.add(new Perico());
		listaObject.add(Integer.valueOf(1000));
		listaObject.add("Patrobas");
		showAnimal(listaObject);

	}
	
	//                     Animal o cualquier Superclase de Animal
	static void showAnimal(List<? super Animal> listaAnimal) {
		
		//Write allowed
		//Animal o cualquier subclase Animal
		
		System.out.println("************");
				
		for (Object ani : listaAnimal) {
			
			System.out.println(ani.getClass().getSimpleName());
			if (ani instanceof Perico)
				((Perico)ani).volarPerico();
			if (ani instanceof Pato p) //Pattern Matching Java 14
				p.volarPato();
			if (ani instanceof Animal)
				((Animal)ani).volar();
		}
		
	}

}
