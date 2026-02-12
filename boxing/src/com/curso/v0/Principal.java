package com.curso.v0;

public class Principal {
	
	public static void main(String[] args) {
		
		int x = 1;
		int y = 010; //OCTAL 
		
		System.out.println(x+y); //9
		
		//BINARIO, OCTAL, DECIMAL, HEXADECIMAL
		//0B,0b  , 0    ,        , 0X 0x 
		
		int int1 = 129;
		int int2 = 129;
		
		System.out.println(int1 == int2); //true
		
		Integer integer1 = 129; //Autoboxing
		Integer integer2 = 129; //Autoboxing
		
		System.out.println(integer1 == integer2); //false
		
		Integer integer3 = 127; //Autoboxing
		Integer integer4 = 127; //Autoboxing
		
		//-128 a 127 //Cache Integers
		
		System.out.println(integer3 == integer4); //true
		
		byte b1 = 5;
		byte b2 = 4;
		
		byte b3 = (byte)(b1 + b2);
		
		System.out.println(b3);
		
		System.out.println(b2+=b1);
		
		
		
	}

}
