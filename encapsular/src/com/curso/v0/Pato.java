package com.curso.v0;

public class Pato {
	
	String name;
	int age;
	
	public Pato(String name, int age) {
		this.name = name;
		this.age = age;
	}

	@Override
	public String toString() {
		return "Pato [name=" + name + ", age=" + age + "]";
	}
	
}
