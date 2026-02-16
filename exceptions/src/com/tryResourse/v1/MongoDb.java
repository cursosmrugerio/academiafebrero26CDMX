package com.tryResourse.v1;

public class MongoDb {
	private String name;
	
	MongoDb(String name){
		this.name = name;
	}
	
	boolean open() throws Exception {
		System.out.println("Abrir Conexion MongoDb");
		//......
		throw new Exception("Exception al abrir MongoDb...");
		//return true;
	}
	
	boolean close() throws Exception {
		System.out.println("Cerrar Conexion MongoDb");
		//......
		//throw new Exception("Exception al cerrar MongoDb...");
		return true;
	}

}
