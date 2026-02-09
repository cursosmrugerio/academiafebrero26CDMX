package com.curso.v1;

class Node{
    Node next; //HAS A
    public Node(){ 
        next = null; 
    }
    public Node(Node next){
        this.next = next;
    }
}

class TestClass{
    
    public static void main(String[] args) {
        Node n1 = new Node();
        Node n2 = new Node(n1);
        Node n3 = new Node(n2);
        n1.next = n3;
        
        boolean r = (n1 == n3.next.next);
        
        System.out.println(r); //true
       
    }
}
