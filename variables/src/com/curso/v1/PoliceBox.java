package com.curso.v1; // Define el paquete donde vive esta clase

// Clase que demuestra un error comun con constructores y la semantica de referencias en Java
public class PoliceBox {
    String color; // Variable de instancia, valor por defecto: null
    long age;     // Variable de instancia, valor por defecto: 0

    // CUIDADO: esto NO es un constructor, es un METODO comun
    // El 'void' lo convierte en metodo. Un constructor real seria: public PoliceBox() { ... }
    // Por lo tanto, color y age NUNCA se asignan con "blue" y 1200
    public void PoliceBox() {
        color = "blue";
        age = 1200;
    }

    public static void main(String []time) {
        // 'var' infiere el tipo automaticamente (Java 10+), equivale a: PoliceBox p = new PoliceBox();
        var p = new PoliceBox(); // p apunta al Objeto1 (color=null, age=0)
        var q = new PoliceBox(); // q apunta al Objeto2 (color=null, age=0)
        p.color = "green";      // Objeto1: color="green"
        p.age = 1400;           // Objeto1: age=1400
        p = q;                  // p AHORA apunta al Objeto2 (igual que q). Objeto1 se pierde
        System.out.println("Q1="+q.color); // null  - q siempre apunto a Objeto2
        System.out.println("Q2="+q.age);   // 0     - Objeto2 nunca fue modificado
        System.out.println("P1="+p.color); // null  - p ahora apunta a Objeto2 (mismo que q)
        System.out.println("P2="+p.age);   // 0     - Objeto2 tiene valores por defecto
    }
}