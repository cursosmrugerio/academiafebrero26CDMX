package com.curso.v2;

import java.util.*;

public class Principal {

	public static void main(String[] args) {		

		Pato pato1 = new Pato("Donald",5);
		Pato pato2 = new Pato("Donald",5);
		Pato pato3 = new Pato("Lucas",8);
		Pato pato4 = new Pato("Lucas",8);
		
		System.out.println(pato1.equals(pato2)); //true
		
		Set<Pato> patos = new HashSet<>();
		
		patos.add(pato1);
		patos.add(pato2);
		patos.add(pato3);
		patos.add(pato4);
		
		for(Pato p: patos) {
			System.out.println(p);
		}
		
	
		
	}

}
