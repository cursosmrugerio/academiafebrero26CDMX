package com.tryResourse.v0;

public class Principal {
	
	public static void main(String[] args) {
		
		MongoDb conMongoQA = new MongoDb("MongoDB QA");
		
		try {
			conMongoQA.open();
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		//PROBLEMA ES QUE NO CERRAMOS LA CONEXION MONGODB
		
		System.out.println("Program End");
		
	}

}
