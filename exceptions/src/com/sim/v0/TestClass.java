package com.sim.v0;


public class TestClass {
    
    public static void doStuff() throws Exception{
        System.out.println("Doing stuff...");
        //Math.random() Valores 0.0 y 0.99
        if(Math.random()>0.4){
            throw new Exception("Too high!");
        }
        System.out.println("Done stuff.");
    }
    // <= 0.4
    //Doing stuff...
    //Done stuff.
    //Over
    
    // > 0.4
    // Doing stuff...
    // Lanza la Exception "Too high!"
    
    
    public static void main(String[] args) throws Exception  { 
		doStuff();
        System.out.println("Over");	
    }
}
