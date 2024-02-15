# Basic FizzBuzz:
# create output following the pattern:
# "1, 2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16" up to given number.
#
# Extended FizzBuzz:
# pass divisor arguments: FizzBuzzExtended(100, {"fizz": 3, "buzz": 4})
# pass any number of divisor arguments: FizzBuzzExtended(100, {"fizz": 3, "buzz": 4, "foo": 8, "bar": 9})

# unittest or pytest? pytest


from fizzbuzz import fizzbuzz

def test_sanity():
    assert isinstance(fizzbuzz, object)
