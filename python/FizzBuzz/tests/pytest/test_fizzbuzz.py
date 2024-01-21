from src.fizzbuzz import fizzbuzz


class TestFizzBuzz:
    def test_get_message_case_one_then_return_it(self):
        expected = "1"
        actual = fizzbuzz.get_message(1)

        assert expected == actual

    def test_get_message_case_three_then_return_fizz(self):
        expected = "Fizz"
        actual = fizzbuzz.get_message(3)

        assert expected == actual

    def test_get_message_case_five_then_return_buzz(self):
        expected = "Buzz"
        actual = fizzbuzz.get_message(5)

        assert expected == actual

    def test_get_message_case_fifteen_then_return_fizzbuzz(self):
        expected = "FizzBuzz"
        actual = fizzbuzz.get_message(15)

        assert expected == actual
