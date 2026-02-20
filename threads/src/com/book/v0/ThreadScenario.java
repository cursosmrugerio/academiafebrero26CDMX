package com.book.v0;

//Objeto Mutable
class Student {
	int id;
	String name;
}

public class ThreadScenario {
	public static void main(String[] args) throws InterruptedException {
		Student s = new Student();
		// Estado inicial: id=0, name=null

		Thread t1 = new Thread(() -> {
			s.id = 1;
			// Simula trabajo antes de asignar el nombre
			try {
				Thread.sleep(200);
			} catch (InterruptedException e) {
			}
			s.name = "Amy"; //<<name
		});

		Thread t2 = new Thread(() -> {
			s.id = 2;
			s.name = "Bob";
		});

		t1.start();
		t2.start();

		Thread.sleep(5000); // main espera a que ambos hilos terminen

		System.out.println("id = " + s.id + ", name = " + s.name);
		// Resultado probable: id=2, name=Amy
	}
}