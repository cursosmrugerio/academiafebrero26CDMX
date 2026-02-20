package com.curso.v0.spring;

import com.curso.v0.*;
import com.curso.v0.pizza.*;

public class Inyector {
	
	public static void inyecta(PizzaStore store,String item) {
		
		if (store instanceof NYPizzaStore) {
			if (item.equals("cheese")) {
				store.setPizza(new NYStyleCheesePizza());
			} else if (item.equals("veggie")) {
				store.setPizza(new NYStyleVeggiePizza());
			} else if (item.equals("clam")) {
				store.setPizza(new NYStyleClamPizza());
			} else if (item.equals("pepperoni")) {
				store.setPizza(new NYStylePepperoniPizza());
			} 
			
		} else if (store instanceof ChicagoPizzaStore){
			if (item.equals("cheese")) {
				store.setPizza(new ChicagoStyleCheesePizza());
			} else if (item.equals("veggie")) {
				store.setPizza(new ChicagoStyleVeggiePizza());
			} else if (item.equals("clam")) {
				store.setPizza(new ChicagoStyleClamPizza());
			} else if (item.equals("pepperoni")) {
				store.setPizza(new ChicagoStylePepperoniPizza());
			} 
		}
		
	}

}
