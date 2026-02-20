package com.simple.factory;

import com.simple.factory.pizza.Pizza;

public class PizzaStore {
	SimplePizzaFactory factory; //HAS-A
 
	public PizzaStore(SimplePizzaFactory factory) { 
		this.factory = factory;
	}
 
	public Pizza orderPizza(String type) {
		Pizza pizza;
 
		pizza = factory.createPizza(type); //DELEGACION
 
		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();

		return pizza;
	}

}
