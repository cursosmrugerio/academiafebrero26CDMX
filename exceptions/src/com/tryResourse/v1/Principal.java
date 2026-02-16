package com.tryResourse.v1;

public class Principal {
	
	public static void main(String[] args) {
		
		MongoDb conMongoQA = new MongoDb("MongoDB QA");
		
		try {
			conMongoQA.open();
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				conMongoQA.close();
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		System.out.println("Program End");
		
	}

}
