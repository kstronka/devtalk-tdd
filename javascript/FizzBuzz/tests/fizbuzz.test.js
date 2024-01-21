import { describe, expect, test } from '@jest/globals';
import { fizzBuzz } from '../src/fizzbuzz.js';

describe('FizzBuzz', () => {
  test('case 1 then return 1', () => {
    const expected = '1';
    const actual = fizzBuzz(1);

    expect(actual).toBe(expected);
  });

  test('case 3 then return Fizz', () => {
    const expected = 'Fizz';
    const actual = fizzBuzz(3);

    expect(actual).toBe(expected);
  });

  test('case 5 then return Buzz', () => {
    const expected = 'Buzz';
    const actual = fizzBuzz(5);

    expect(actual).toBe(expected);
  });

  test('case 15 then return FizzBuzz', () => {
    const expected = 'FizzBuzz';
    const actual = fizzBuzz(15);

    expect(actual).toBe(expected);
  });
});
