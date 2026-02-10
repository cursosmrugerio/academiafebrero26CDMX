package com.curso.v1;

import com.curso.v0.Aguila;

public class Principal extends Aguila {

	public static void main(String[] args) {

		Principal aguila = new Principal();
		
		System.out.println(aguila.name); //public
		System.out.println(aguila.real); //protected
		
		//System.out.println(aguila.tipo); //default
		//System.out.println(aguila.age); //private
		
		
	}

}
