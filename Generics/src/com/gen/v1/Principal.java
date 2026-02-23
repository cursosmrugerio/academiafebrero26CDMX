package com.gen.v1;

public class Principal {
	
	public static void main(String[] args) {
		System.out.println("Generics V1");
		
		Suma<Integer,Float> suma1 = new Suma<>();
		Suma<Long,Byte> suma2 = new Suma<>();
		Suma<Double,Short> suma3 = new Suma<>();
		
		System.out.println(suma1.ejecuta(4,3.0f));
		System.out.println(suma2.ejecuta(8L,(byte)127));
		System.out.println(suma3.ejecuta(4.0,(short)5));
		
		Byte byte1 = 127;
		Short short1 = 5;
		long long0 = 5;
		Long long1 = (long)5;
		
	}
}
