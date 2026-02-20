package com.curso.v0;

import com.curso.v0.pizza.Pizza;

public abstract class PizzaStore {
	
	private Pizza pizza; //Abstract
 
	//The Factory Method Pattern
	abstract Pizza createPizza(); 
 
	final public Pizza orderPizza() {
		Pizza pizza = createPizza(); //<== Subclass quien decide
		System.out.println("--- Making a " + pizza.getName() + " ---");
		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();
		return pizza;
	}

	public Pizza getPizza() {
		return pizza;
	}

	public void setPizza(Pizza pizza) {
		this.pizza = pizza;
	}
	
}
