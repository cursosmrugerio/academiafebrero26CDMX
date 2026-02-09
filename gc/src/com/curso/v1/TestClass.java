package com.curso.v1; // Define el paquete donde vive esta clase

// Clase Node: nodo con referencia al siguiente - relacion HAS-A
class Node{
    // Campo que apunta al siguiente nodo - composicion HAS-A (Node "tiene un" Node)
    Node next; //HAS A

    // Constructor por defecto: nodo sin enlace
    public Node(){
        next = null;
    }

    // Constructor parametrizado: nodo que apunta a otro nodo
    public Node(Node next){
        this.next = next;
    }
}

// Clase que demuestra referencias circulares e igualdad de referencias (==)
class TestClass{

    public static void main(String[] args) {
        // Se crea n1: nodo sin enlace (next = null)
        Node n1 = new Node();
        // Se crea n2: su next apunta a n1   -> n2.next = n1
        Node n2 = new Node(n1);
        // Se crea n3: su next apunta a n2   -> n3.next = n2
        Node n3 = new Node(n2);
        // Se enlaza n1 a n3, creando un CICLO: n1 -> n3 -> n2 -> n1 -> n3 -> ...
        n1.next = n3;

        // Se evalua si recorrer la cadena desde n3 nos regresa a n1:
        // n3.next       = n2    (por el constructor)
        // n3.next.next  = n1    (porque n2.next = n1)
        // Entonces: (n1 == n3.next.next) compara si ambas referencias apuntan al MISMO objeto
        boolean r = (n1 == n3.next.next);

        // Imprime true: la referencia es la misma, confirmando el ciclo
        // Nota: en Java, el GC puede recolectar ciclos (a diferencia de reference counting)
        System.out.println(r); //true

    }
}
