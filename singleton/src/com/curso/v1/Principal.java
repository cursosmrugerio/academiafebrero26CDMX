package com.curso.v1;

public class Principal {

	public static void main(String[] args) {
		
		System.out.println("V1");
		
		ConexionDB con1 = ConexionDB.getInstance();
		ConexionDB con2 = ConexionDB.getInstance();
		ConexionDB con999 = ConexionDB.getInstance();
		
		System.out.println(con1);
		System.out.println(con2);
		System.out.println(con999);
		
	}

}
