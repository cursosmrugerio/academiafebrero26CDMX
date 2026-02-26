package com.curso.v6;

import java.util.IntSummaryStatistics;
import java.util.stream.IntStream;

public class Principal {

	public static void main(String[] args) {

		IntStream ints = IntStream.of(51,2,8,0,23,32);
		
		IntSummaryStatistics stats = ints.summaryStatistics();
		
		System.out.println("Average: "+stats.getAverage());
		System.out.println("Count: "+stats.getCount());
		System.out.println("Max: "+stats.getMax());
		System.out.println("Min: "+stats.getMin());
		System.out.println("Sum: "+stats.getSum());

		
	}

}
