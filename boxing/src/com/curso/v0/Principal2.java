package com.curso.v0;

import java.math.BigDecimal;

public class Principal2 {
	
	public static void main(String[] args) {
		
		double a = 0.02;
		double b = 0.03;
		double c = b - a;
		System.out.println(c); //0.01
		
		BigDecimal bd1 = BigDecimal.valueOf(0.02);
		BigDecimal bd2 = BigDecimal.valueOf(0.03);
		System.out.println(bd1.subtract(bd2)); //0.01
		
	    double d1 = 0.3;
	    double d2 = 0.2;
	    System.out.println("Double:\t 0,3 - 0,2 = " + (d1 - d2)); //0.1

	    float f1 = 0.3f;
	    float f2 = 0.2f;
	    System.out.println("Float:\t 0,3 - 0,2 = " + (f1 - f2)); //0.1
	    
	    double d3 = 0.3;
	    double d4 = 0.2;
	    
	    double d5 = (d3*1000 - d4*1000)/1000;
	    
	    System.out.println("Double:\t 0,3 - 0,2 = " + d5); //0.1
		
		
	}

}
