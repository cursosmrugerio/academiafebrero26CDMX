package com.curso.v1;

public class ConexionDB {
	
	static private ConexionDB conexion = new ConexionDB() ;
	
	private ConexionDB(){
		System.out.println("PASO POR CONSTRUCTOR!");
	}
	
	static public ConexionDB getInstance() {
		return conexion;
	}

}
