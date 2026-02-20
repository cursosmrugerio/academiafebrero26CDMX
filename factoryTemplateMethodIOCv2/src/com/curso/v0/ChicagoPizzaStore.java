package com.curso.v0;

import com.curso.v0.pizza.Pizza;

public class ChicagoPizzaStore extends PizzaStore {

	@Override
	Pizza createPizza() {
		return getPizza();
	}
	

}
