package com.curso.v1;

public class Init {

	String title;
	boolean published;

	static int total;
	static double maxPrice;

	public static void main(String[] args) {
		Init initMe = new Init();
		double price;
		if (true)
			price = 100.0000;
		
		System.out.println("|" + initMe.title + "|" 
				+ initMe.published + "|" 
				+ Init.total + "|" 
				+ Init.maxPrice + "|"
				+ price + "|");
		
		// null | false | 0 | 0.0 | 100.0
		

	}

}