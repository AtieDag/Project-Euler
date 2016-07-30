# Highly divisible triangular number
import math


def number_of_factors(n):
    count = 0
    for number in range(1, int(math.sqrt(n) + 1)):
        if n % number == 0:
            count += 2
    return count



number = 1
triangle_number = 0
while True:
    triangle_number += number
    divisors = number_of_factors(triangle_number)
    print(triangle_number, divisors)
    if divisors > 500:
        print(triangle_number)
        break
    number += 1
