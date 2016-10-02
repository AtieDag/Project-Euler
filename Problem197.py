# https://projecteuler.net/problem=197
import math


def f(x):
    return math.floor(2 ** (30.403243784 - x ** 2)) * 10 ** -9


if __name__ == '__main__':
    u = f(-1)
    i = 0
    diff = 10 ** -10
    D1 = []
    while True:
        u = f(u)
        i += 1
        if i % 2 == 0:
            D1.append(u)
            if diff > math.fabs(D1[len(D1) - 1] - D1[len(D1) - 2]) and i > 2:
                break

    print(D1[len(D1) - 1] + f(D1[len(D1) - 1]))
