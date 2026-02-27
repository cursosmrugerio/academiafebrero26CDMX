package com.curso.v1A;

class Pato{}

public class Bees {
    public static void main(String[] args) {
        try {
            new Bees().go();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    void go() throws InterruptedException   {
    	
    	Pato pato = new Pato();
    	
        Thread t1 = new Thread();
        t1.start();
        System.out.println("1 ");
        synchronized(pato) {
        	pato.wait(5000); 
        }
        System.out.println("2 ");
    }
}