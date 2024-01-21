export const fizzBuzz = (value) => {
  let result = '';

  if (value % 3 === 0) {
    result = result + 'Fizz';
  }

  if (value % 5 === 0) {
    result = result + 'Buzz';
  }

  if (result === '') {
    result = `${value}`;
  }

  return result;
};
