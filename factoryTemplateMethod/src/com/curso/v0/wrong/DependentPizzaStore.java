package com.curso.v0.wrong;

import com.curso.v0.pizza.ChicagoStyleCheesePizza;
import com.curso.v0.pizza.ChicagoStyleClamPizza;
import com.curso.v0.pizza.ChicagoStylePepperoniPizza;
import com.curso.v0.pizza.ChicagoStyleVeggiePizza;
import com.curso.v0.pizza.NYStyleCheesePizza;
import com.curso.v0.pizza.NYStyleClamPizza;
import com.curso.v0.pizza.NYStylePepperoniPizza;
import com.curso.v0.pizza.NYStyleVeggiePizza;
import com.curso.v0.pizza.Pizza;

public class DependentPizzaStore {
	
	//SOLUCION SIN APLICAR EL Factory Template Method
	//MAL DISEÑO
 
	public Pizza createPizza(String style, String type) {
		Pizza pizza = null;
		if (style.equals("NY")) {
			if (type.equals("cheese")) {
				pizza = new NYStyleCheesePizza();
			} else if (type.equals("veggie")) {
				pizza = new NYStyleVeggiePizza();
			} else if (type.equals("clam")) {
				pizza = new NYStyleClamPizza();
			} else if (type.equals("pepperoni")) {
				pizza = new NYStylePepperoniPizza();
			}
		} else if (style.equals("Chicago")) {
			if (type.equals("cheese")) {
				pizza = new ChicagoStyleCheesePizza();
			} else if (type.equals("veggie")) {
				pizza = new ChicagoStyleVeggiePizza();
			} else if (type.equals("clam")) {
				pizza = new ChicagoStyleClamPizza();
			} else if (type.equals("pepperoni")) {
				pizza = new ChicagoStylePepperoniPizza();
			}
		} else {
			System.out.println("Error: invalid type of pizza");
			return null;
		}
		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();
		return pizza;
	}
}
