package com.curso.v0;

import com.curso.v0.pizza.NYStyleCheesePizza;
import com.curso.v0.pizza.NYStyleClamPizza;
import com.curso.v0.pizza.NYStylePepperoniPizza;
import com.curso.v0.pizza.NYStyleVeggiePizza;
import com.curso.v0.pizza.Pizza;

public class NYPizzaStore extends PizzaStore {

	@Override
	Pizza createPizza(String item) {
		if (item.equals("cheese")) {
			return new NYStyleCheesePizza();
		} else if (item.equals("veggie")) {
			return new NYStyleVeggiePizza();
		} else if (item.equals("clam")) {
			return new NYStyleClamPizza();
		} else if (item.equals("pepperoni")) {
			return new NYStylePepperoniPizza();
		} else return null;
	}
}
