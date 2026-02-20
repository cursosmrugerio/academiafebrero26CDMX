package com.curso.v0.main;

import com.curso.v0.ChicagoPizzaStore;
import com.curso.v0.NYPizzaStore;
import com.curso.v0.PizzaStore;
import com.curso.v0.pizza.ChicagoStyleCheesePizza;
import com.curso.v0.pizza.ChicagoStyleClamPizza;
import com.curso.v0.pizza.NYStyleCheesePizza;
import com.curso.v0.pizza.NYStyleClamPizza;
import com.curso.v0.pizza.Pizza;

public class PizzaTestDrive {
 
	public static void main(String[] args) {
		
		System.out.println("***Inversion of Control***");
		PizzaStore nyStore = new NYPizzaStore();
		PizzaStore chicagoStore = new ChicagoPizzaStore();
 
		System.out.println("****** QUESO *******");

		nyStore.setPizza(new NYStyleCheesePizza()); //Inyección Dedpendencia Setter
		Pizza pizza = nyStore.orderPizza();
		System.out.println("Ethan ordered a " + pizza.getName() + "\n");

		chicagoStore.setPizza(new ChicagoStyleCheesePizza()); //Inyección Dedpendencia Setter
		pizza = chicagoStore.orderPizza();
		System.out.println("Joel ordered a " + pizza.getName() + "\n");
		
		System.out.println("****** CALAMAR *******");

		nyStore.setPizza(new NYStyleClamPizza());
		pizza = nyStore.orderPizza();
		System.out.println("Ethan ordered a " + pizza.getName() + "\n");
 
		chicagoStore.setPizza(new ChicagoStyleClamPizza());
		pizza = chicagoStore.orderPizza();
		System.out.println("Joel ordered a " + pizza.getName() + "\n");
//
//		pizza = nyStore.orderPizza("pepperoni");
//		System.out.println("Ethan ordered a " + pizza.getName() + "\n");
// 
//		pizza = chicagoStore.orderPizza("pepperoni");
//		System.out.println("Joel ordered a " + pizza.getName() + "\n");
//
//		pizza = nyStore.orderPizza("veggie");
//		System.out.println("Ethan ordered a " + pizza.getName() + "\n");
// 
//		pizza = chicagoStore.orderPizza("veggie");
//		System.out.println("Joel ordered a " + pizza.getName() + "\n");
	}
}
