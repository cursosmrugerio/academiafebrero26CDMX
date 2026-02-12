package com.curso.v0;

import java.time.*;

public class Principal2 {

	public static void main(String[] args) {
		LocalDate date = LocalDate.of(2022, Month.JANUARY, 20);
		date = date.plusDays(8);
		System.out.println(date); 
		
		
		String name = "Andronico";
		name = name.concat(" Patrobas");
		System.out.println(name);  
		
		date = LocalDate.of(2024, Month.JANUARY, 20); 
		LocalTime time = LocalTime.of(5, 15); 
		
		LocalDateTime dateTime = LocalDateTime.of(date, time) 
				.minusDays(1)
				.minusHours(10)
				.minusSeconds(30);
		
		System.out.println(dateTime);
		
		
	}

}
