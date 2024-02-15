def fizzbuzz(number: int, divisors: dict = {"Fizz": 3, "Buzz": 5, "FizzBuzz": 15}) -> str:
    if number == 0:
        raise ValueError()
    for name, divisor in sorted(divisors.items(), key=lambda x: x[1], reverse=True):
        if is_divisible(number, divisor):
            return name
    return str(number)


def fizzbuzz_print(upto: int, sep: str = ",") -> str:
    return sep.join([fizzbuzz(n) for n in range(1, upto+1)])


def is_divisible(number: int, divisor: int) -> bool:
    return number % divisor == 0