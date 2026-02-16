package com.tryResourse.v2;

public class Principal {
	
	public static void main(String[] args) {
		
		//Try With Resource
		try (MongoDb conMongoQA = new MongoDb("MongoDB QA")) {
			conMongoQA.open();
		} catch (Exception e) {
			e.printStackTrace();
		} 
		
		System.out.println("Program End");
		
	}

}
