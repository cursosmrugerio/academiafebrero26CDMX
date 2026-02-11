package com.curso.v2;

import java.util.Objects;

public class Pato extends Object {
	
	String name;
	int age;
	
	public Pato(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	@Override
	public int hashCode() {
		return Objects.hash(age, name);
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Pato other = (Pato) obj;
		return age == other.age && Objects.equals(name, other.name);
	}




	@Override
	public String toString() {
		return "Pato [name=" + name + ", age=" + age + "]";
	}
	
	
	
	

}
