package com.curso.v0;

import java.time.*;

public class Principal3 {

	public static void main(String[] args) {

		LocalDate start = LocalDate.of(2022, Month.JANUARY, 1);
		
		//Period period = Period.ofWeeks(4);
		Period period = Period.of(1,2,15);
		
		LocalDate end = start.plus(period);
		
		System.out.println(end);
		
		System.out.println("*********");
		
		Period period2 = Period.ofYears(1)
							   .ofWeeks(1);
		
		LocalDate start2 = LocalDate.of(2022, Month.JANUARY, 1);
		
		start2 = start2.plus(period2);
		
		System.out.println(start2); //2022 01 08
		
		
	}

}
