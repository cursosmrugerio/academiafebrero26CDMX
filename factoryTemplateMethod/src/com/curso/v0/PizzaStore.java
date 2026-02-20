package com.curso.v0;

import com.curso.v0.pizza.Pizza;

public abstract class PizzaStore {
 
	//The Factory Method Pattern
	abstract Pizza createPizza(String item); 
 
	final public Pizza orderPizza(String type) {
		Pizza pizza = createPizza(type); //<== Subclass quien decide
		System.out.println("--- Making a " + pizza.getName() + " ---");
		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();
		return pizza;
	}
}
