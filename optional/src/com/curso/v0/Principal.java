package com.curso.v0;

import java.util.Optional;

public class Principal {

	public static void main(String[] args) {

		Optional<String> empty = Optional.empty();
		System.out.println(empty);
		boolean res = empty.isPresent();
		System.out.println(res);
		
		String name = "baeldung";
	    Optional<String> opt = Optional.of(name);
	    res = opt.isPresent();
	    System.out.println(res);
	    
	    name = null;
	    //Optional.of(name); //NullPointerException
	    opt = Optional.ofNullable(name);
	    res = opt.isPresent();
	    System.out.println(res);
	    
	    opt = Optional.of("baeldung");
	    opt.ifPresent(nombre -> System.out.println(nombre.length()));
	}

}
