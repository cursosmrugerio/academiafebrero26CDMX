package com.curso.v0;

import static org.junit.jupiter.api.Assertions.*;
//import org.junit.jupiter.api.Assertions;
import java.util.*;

import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

class TestOptional {

	@Test
	@Disabled
	void test() {
		fail("Not yet implemented");
	}
	
	@Test
	public void whenCreatesEmptyOptional_thenCorrect() {
	    Optional<String> empty = Optional.empty();
	    assertFalse(empty.isPresent());
	}
	
	@Test
	public void givenNonNull_whenCreatesNonNullable_thenCorrect() {
	    String name = "baeldung";
	    Optional<String> opt = Optional.of(name);
	    assertTrue(opt.isPresent());
	}
	
	@Test
    void givenNull_whenThrowsErrorOnCreate_thenCorrect() {
        String name = null;
        assertThrows(NullPointerException.class, 
        		() ->  Optional.of(name) );
    }
	
	@Test
	public void givenNonNull_whenCreatesNullable_thenCorrect() {
	    String name = "baeldung";
	    Optional<String> opt = Optional.ofNullable(name);
	    assertTrue(opt.isPresent());
	}
	
	@Test
	public void givenNull_whenCreatesNullable_thenCorrect() {
	    String name = null;
	    Optional<String> opt = Optional.ofNullable(name);
	    assertFalse(opt.isPresent());
	}
	
	@Test
	@Disabled
	public void givenOptional_whenIfPresentWorks_thenCorrect() {
	    Optional<String> opt = Optional.of("baeldung");
	    opt.ifPresent(name -> System.out.println(name.length()));
	}
	
	@Test
	public void givenOptional_whenIfPresentWorks_thenCorrectNull() {
	    Optional<String> opt = Optional.ofNullable(null);
	    opt.ifPresent(name -> System.out.println(name.length()));
	}
	
	@Test
	public void givenOptional_whenMapWorks_thenCorrect() {
	    List<String> companyNames = Arrays.asList(
	    		"paypal", 
	    		"oracle", 
	    		"", 
	    		"microsoft", 
	    		"", 
	    		"apple");
	    
	    companyNames = null;
	    
	    Optional<List<String>> listOptional = 
	    		Optional.ofNullable(companyNames);
	    
	    int size = listOptional
	      .map(List::size) //Function
	      .orElse(0);
	    
	    assertEquals(0, size);
	}
	
}
