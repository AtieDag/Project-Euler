# The sum of the difference of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 ? 385 = 2640. Find the difference between the sum of
# the squares of the first one hundred natural numbers and the square of the sum.
# Done in 0.05 ms...
import time


def sum_minus_square(number_of_numbers):
    steps = range(1, number_of_numbers + 1, 1)
    sum_of_the_squares = 0
    for i in steps:
        sum_of_the_squares += i*i

    square_of_the_sum = pow(sum(steps), 2)

    return abs(sum_of_the_squares-square_of_the_sum)


if __name__ == '__main__':
    tic = time.clock()
    difference = sum_minus_square(100)

    print(difference)
    toc = time.clock()
    print((toc - tic) * 1000)
