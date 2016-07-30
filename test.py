import math


def number_of_factors(n):
    count = 0
    for number in range(1, int(math.sqrt(n) + 1)):
        if n % number == 0:
            count += 2
            print(number, n / number)
    return count


print("count ", number_of_factors(28))
