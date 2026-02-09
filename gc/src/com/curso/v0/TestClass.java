package com.curso.v0; // Define el paquete donde vive esta clase

// Clase Node: estructura tipo nodo de lista enlazada
// Demuestra la composicion HAS-A y como el GC rastrea cadenas de referencias
class Node{
    // Campo que apunta al siguiente nodo - relacion HAS-A (Node "tiene un" Node)
    Node next;

    // Constructor por defecto: crea un nodo sin enlace (next = null)
    public Node(){
        next = null;
    }

    // Constructor parametrizado: crea un nodo que apunta a otro nodo existente
    public Node(Node next){
        this.next = next; // Este nodo queda enlazado al nodo recibido
    }

    // Metodo de utilidad que retorna un mensaje (para demostrar que el objeto sigue vivo)
    public String dump(){
        return "from dump";
    }
}

// Clase principal que demuestra la recoleccion de basura con nodos enlazados
class TestClass{

    public static void main(String[] args) {
        // Se crea n1: un nodo sin enlace (next = null)
        Node n1 = new Node();
        // Se crea n2: un nodo cuyo 'next' apunta a n1
        // Cadena de referencias: n2 -> n1
        Node n2 = new Node(n1);
        // Se crea n3: un nodo sin enlace (independiente)
        Node n3 = new Node();
        // Se anula la variable n1: la referencia local desaparece
        // PERO el objeto n1 NO es elegible para GC porque n2.next aun lo referencia
        n1 = null;
        // n2.dump() funciona correctamente, demostrando que n2 sigue vivo
        // Tambien n2.next (el antiguo n1) sigue vivo por la referencia desde n2
        System.out.println(n2.dump()); // 0
    }
}
