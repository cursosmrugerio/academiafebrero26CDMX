package com.simple.factory;

import com.simple.factory.pizza.CheesePizza;
import com.simple.factory.pizza.ClamPizza;
import com.simple.factory.pizza.PepperoniPizza;
import com.simple.factory.pizza.Pizza;
import com.simple.factory.pizza.VeggiePizza;

public class SimplePizzaFactory {

	public Pizza createPizza(String type) {
		Pizza pizza = null;

		if (type.equals("cheese")) {
			pizza = new CheesePizza();
		} else if (type.equals("pepperoni")) {
			pizza = new PepperoniPizza();
		} else if (type.equals("clam")) {
			pizza = new ClamPizza();
		} else if (type.equals("veggie")) {
			pizza = new VeggiePizza();
		}
		return pizza;
	}
}
