package com.curso.v0;

public class Alumno {
	
	String nombre;

	public Alumno(String nombre) {
		this.nombre = nombre;
	}
	
	//Overloading
	
//	void getPromedio(int x, int y) {
//		System.out.println("int,int");
//		System.out.println((x+y)/2);
//	}
	
	void getPromedio(int... xs) {
		System.out.println("varargs...");
		int suma = 0;
		for (int x: xs) {
			suma += x;
		}
		System.out.println(suma/xs.length);
	}
	
//	void getPromedio(double x, double y) {
//		System.out.println("double,double");
//		System.out.println((x+y)/2);
//	}
	
//	void getPromedio(Integer x, Integer y) {
//		System.out.println("Integer,Integer");
//		System.out.println((x+y)/2);
//	}
	
	void getPromedio(Double x, Double y) {
		System.out.println((x+y)/2);
	}
	

}
