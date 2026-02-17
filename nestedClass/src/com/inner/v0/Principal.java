package com.inner.v0;

class Animal{
	String name;
	class Pato{} //Inner Class
	//Inner Class, se necesita el objeto de quien la contiene.
}

public class Principal {

	public static void main(String[] args) {
		
		Animal.Pato pato1 = new Animal().new Pato();
		
		Animal animal = new Animal();
		Animal.Pato pato2 = animal.new Pato();
		
		System.out.println(pato1);
		System.out.println(pato2);

	}

}
