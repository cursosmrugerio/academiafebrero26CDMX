package com.gen.v3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Principal {
	
	public static void main (String... args) {

		String[] names = {"Patrobas","Andronico","Filologo","Epeneto"};
//		List<String> listaNombres = new ArrayList<>(Arrays.asList(names));
//		List<Object> lista = listaNombres;
		List<Object> lista = new ArrayList<>(Arrays.asList(names));
		System.out.println(lista);
		
		
		List<String> listaNames = new ArrayList<>();
		listaNames.add("Patrobas");
		listaNames.add("Andronico");
		listaNames.add("Filologo");
		listaNames.add("Epeneto");
		//List<Object> listaObject = listaNames;
		
		//List<?> list = new ArrayList<?>(Arrays.asList(names));
		
		//List<> list = new ArrayList<String>(Arrays.asList(names));
		
		
	}

}
