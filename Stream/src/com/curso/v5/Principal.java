package com.curso.v5;

import java.util.stream.Stream;
import java.util.TreeSet;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class Principal {

	public static void main(String[] args) {
		
		//      Generis                   T Generic
		//      método                      Stream
		//      <R,A>                       clase
		
		//public <R,A> R collect(Collector<? super T, A,R> collector)
		
		Stream<String> stream = Stream.of("w", "o", "l", "f");
		
		//TreeSet<String> set =
		//		stream.collect(Collectors.toCollection(TreeSet::new));
		
		//Collectors.toCollection(TreeSet::new);
		Collector<String,?,TreeSet<String>> collector = 
				Collectors.toCollection(()->new TreeSet<String>());
		
		TreeSet<String> set = stream.collect(collector);
		
		System.out.println(set);
		
		
		
		

	}

}
