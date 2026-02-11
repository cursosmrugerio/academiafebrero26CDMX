package com.curso.v1;

public class Pato {
	
	private String name;
	private int age;
	
	public Pato(String name, int age) {
		this.name = name;
		this.age = age;
	}


	public String getName() {
		//if (user.rol == "ADMIN")
			return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		if (age<0)
			throw new UnsupportedOperationException("Edad invalida");
		this.age = age;
	}
	
	@Override
	public String toString() {
		return "Pato [name=" + name + ", age=" + age + "]";
	}

	
	
	
}
