def fizzbuzz_conver(param):
    if param % 3 == 0:
        return 'Fizz'
    return param


assert fizzbuzz_conver(1) == 1
assert fizzbuzz_conver(2) == 2
assert fizzbuzz_conver(3) == 'Fizz'
assert fizzbuzz_conver(6) == 1
assert fizzbuzz_conver(5) == 'Buzz'
assert fizzbuzz_conver(10) == 'Fizz'
assert fizzbuzz_conver(15) == 'FizzBuzz'
assert fizzbuzz_conver(30) == 'Fizz'
