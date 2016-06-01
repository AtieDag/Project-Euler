# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Done in 232792561 ms...
import time


def divisible(number, number_length):
    for i in range(1, number_length, 1):
        if number % i != 0:
            return False
    return True


if __name__ == '__main__':
    tic = time.clock()
    match = False
    start = 1
    while not match:
        match = divisible(start, 20)
        start += 1
    print(start-1)
    toc = time.clock()
    print((toc - tic) * 1000)
