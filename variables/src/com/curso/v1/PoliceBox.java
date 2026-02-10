package com.curso.v1;

public class PoliceBox {
    String color;
    long age;
    
    public void PoliceBox() { 
        color = "blue";
        age = 1200;
    }
    
    public static void main(String []time) {
        var p = new PoliceBox();
        var q = new PoliceBox();
        p.color = "green";
        p.age = 1400;
        p = q;
        System.out.println("Q1="+q.color); //null
        System.out.println("Q2="+q.age); //0
        System.out.println("P1="+p.color); //null
        System.out.println("P2="+p.age); //0
    }
}