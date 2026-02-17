package com.curso.v0;

public class Principal {

	public static void main(String[] args) {
		
		ConexionDB con1 = ConexionDB.getInstance();
		ConexionDB con2 = ConexionDB.getInstance();
		ConexionDB con999 = ConexionDB.getInstance();
		
		System.out.println(con1);
		System.out.println(con2);
		System.out.println(con999);
		
	}

}
