package com.curso.v0;

class Node{
    Node next;
    public Node(){ 
        next = null; 
    }
    public Node(Node next){
        this.next = next;
    }
    public String dump(){
        return "from dump";
    }
}

class TestClass{
    
    public static void main(String[] args) {
        Node n1 = new Node();
        Node n2 = new Node(n1);
        Node n3 = new Node();
        n1 = null;
        System.out.println(n2.dump()); // 0
    }
}
