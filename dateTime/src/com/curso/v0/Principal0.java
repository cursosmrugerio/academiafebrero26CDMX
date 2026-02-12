package com.curso.v0;

import java.time.*;

public class Principal0 {

	public static void main(String[] args) {

		LocalDate date = LocalDate.of(2024, Month.JANUARY, 20);
		LocalTime time = LocalTime.of(5, 15);
		
		LocalDateTime dateTime0 = LocalDateTime.of(date, time);
		System.out.println(dateTime0);

		LocalDateTime dateTime = LocalDateTime.of(date, time) //Crea Objeto
				.minusDays(1)
				.minusHours(10)
				.minusSeconds(30);
		
		System.out.println(dateTime);
		
		System.out.println("****PERIOD*****");
		
		LocalDate date1 = LocalDate.of(2024, Month.JANUARY, 20);
		LocalDate date2 = date1.plus(Period.ofYears(1).ofWeeks(1));
		System.out.println(date2);

	}

}
