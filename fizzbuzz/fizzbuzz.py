def fizzbuzz(number: int) -> str:
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)

def fizzbuzz_print(upto: int) -> str:
    return ",".join([fizzbuzz(n) for n in range(1, upto+1)])
