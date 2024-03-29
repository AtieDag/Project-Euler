# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?
# Done in 1.64 s...
from numba import jit


@jit(nopython=True)
def is_prime(number):
    if number < 1:
        return False

    for j in range(2, number):
        if number % j == 0:
            return False
    return True


if __name__ == '__main__':
    nr = 0
    i = 0
    while nr != 10002:
        i += 1
        if is_prime(i):
            nr += 1
    print(i)
