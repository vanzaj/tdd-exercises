# Basic FizzBuzz:
# create output following the pattern:
# "1, 2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16" up to given number.
#
# Extended FizzBuzz:
# pass divisor arguments: FizzBuzzExtended(100, {"fizz": 3, "buzz": 4})
# pass any number of divisor arguments: FizzBuzzExtended(100, {"fizz": 3, "buzz": 4, "foo": 8, "bar": 9})

# unittest or pytest? pytest
import pytest
from fizzbuzz import fizzbuzz, fizzbuzz_print

@pytest.mark.parametrize("number, expected", [
    (1, "1"),
    (2, "2"),
    (4, "4"),
    (7, "7"),
])
def test_fizzbuzz_for_normal_numbers(number, expected):
    assert fizzbuzz(number) == expected


@pytest.mark.parametrize("number, expected", [
    (3, "Fizz"),
    (6, "Fizz"),
    (9, "Fizz"),
    (5, "Buzz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
])
def test_fizzbuzz_for_fizz_and_buzz(number, expected):
    assert fizzbuzz(number) == expected

def test_printing_fizzbuzz():
    expected = "1,2,Fizz"
    assert fizzbuzz_print(3) == expected