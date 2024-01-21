package org.fizzbuzz;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    @Test 
    void getMessageCaseOneThenReturnValue() {
        App klass = new App();

        String expected = "1";
        String actual = klass.getMessage(1);

        assertEquals(expected, actual);
    }

    @Test 
    void getMessageCaseThreeThenReturnFizz() {
        App klass = new App();

        String expected = "Fizz";
        String actual = klass.getMessage(3);

        assertEquals(expected, actual);
    }

    @Test 
    void getMessageCaseFiveThenReturnBuzz() {
        App klass = new App();

        String expected = "Buzz";
        String actual = klass.getMessage(5);

        assertEquals(expected, actual);
    }

    @Test 
    void getMessageCaseFifteenThenReturnFizzBuzz () {
        App klass = new App();

        String expected = "FizzBuzz";
        String actual = klass.getMessage(15);

        assertEquals(expected, actual);
    }
}
