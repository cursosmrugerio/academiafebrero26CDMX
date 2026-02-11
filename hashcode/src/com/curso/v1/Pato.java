package com.curso.v1;

import java.util.Objects;

public class Pato extends Object {
	
	String name;
	int age;
	
	public Pato(String name, int age) {
		this.name = name;
		this.age = age;
	}

	@Override
	public boolean equals(Object obj) {
		Pato other = (Pato) obj;
		return age == other.age && Objects.equals(name, other.name);
	}
	
	@Override
	public String toString() {
		return "Pato [name=" + name + ", age=" + age + "]";
	}
	
	
	
	

}
