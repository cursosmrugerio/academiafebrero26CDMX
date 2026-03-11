package com.curso.v0;

public class Question17 {

	public static void main(String[] args) {
		
		int a = 2;   // 010 Binario
		int b = ~a;  // b = -3
		int c = a^b; // c = -1   //0  //1
		
		boolean d = a < b & a > c++;
		//          false   true
		//false
		
		System.out.println(d + " " + c); //false 0
		
		boolean e = a > b && a > c++;
		//          true     true
		
		System.out.println(e + " " + c); //true 1

	}

}
