package com.curso.v0;

public class ConexionDB {
	
	static private ConexionDB conexion;
	
	private ConexionDB(){
		System.out.println("PASO POR CONSTRUCTOR!");
	}
	
	//Los métodos static NO PUEDEN usar 
	//atributos y métodos de instancia.
	static public ConexionDB getInstance() {
		
		if (conexion == null)
			conexion = new ConexionDB() ;
		
		return conexion;
	}

}
