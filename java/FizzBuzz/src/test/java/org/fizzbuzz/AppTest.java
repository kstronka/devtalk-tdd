package org.fizzbuzz;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;

class AppTest {
    public App klass;

    @BeforeEach
    void initClass() {
        klass = new App();
    }

    @AfterEach
    void resetClass() {
        klass = null;
    }

    @Test 
    void getMessageCaseOneThenReturnValue() {
        String expected = "1";
        String actual = klass.getMessage(1);
        assertEquals(expected, actual);
    }

    @Test 
    void getMessageCaseThreeThenReturnFizz() {
        String expected = "Fizz";
        String actual = klass.getMessage(3);
        assertEquals(expected, actual);
    }

    @Test 
    void getMessageCaseFiveThenReturnBuzz() {
        String expected = "Buzz";
        String actual = klass.getMessage(5);
        assertEquals(expected, actual);
    }

    @Test 
    void getMessageCaseFifteenThenReturnFizzBuzz () {
        String expected = "FizzBuzz";
        String actual = klass.getMessage(15);
        assertEquals(expected, actual);
    }
}
