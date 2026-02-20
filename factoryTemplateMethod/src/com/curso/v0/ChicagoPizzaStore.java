package com.curso.v0;

import com.curso.v0.pizza.ChicagoStyleCheesePizza;
import com.curso.v0.pizza.ChicagoStyleClamPizza;
import com.curso.v0.pizza.ChicagoStylePepperoniPizza;
import com.curso.v0.pizza.ChicagoStyleVeggiePizza;
import com.curso.v0.pizza.Pizza;

public class ChicagoPizzaStore extends PizzaStore {

	Pizza createPizza(String item) {
        	if (item.equals("cheese")) {
        			//ALTO ACOPLAMIENTO
            		return new ChicagoStyleCheesePizza();
        	} else if (item.equals("veggie")) {
        			//ALTO ACOPLAMIENTO
        	    	return new ChicagoStyleVeggiePizza();
        	} else if (item.equals("clam")) {
        			//ALTO ACOPLAMIENTO
        	    	return new ChicagoStyleClamPizza();
        	} else if (item.equals("pepperoni")) {
        			//ALTO ACOPLAMIENTO
            		return new ChicagoStylePepperoniPizza();
        	} else return null;
	}
}
