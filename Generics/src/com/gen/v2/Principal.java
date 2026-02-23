package com.gen.v2;


class Alumno {
	
	static public <V> V getMatricula(V v) {
		System.out.println("Mostrar matricula: "+v);
		return v;
	}
}

public class Principal {
	
	public static void main (String... args) {
		Alumno.getMatricula("XYZ100");
		
		Alumno.<StringBuilder>getMatricula(new StringBuilder("WER890"));
		
		Alumno.getMatricula(new Object());
		
		Alumno.<Double>getMatricula(Math.random());
	}

}
