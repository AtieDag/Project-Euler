# n! means n x (n − 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


def fac(n, total=1):
    total *= n
    if n == 1:
        return total
    else:
        return fac(n - 1, total)


if __name__ == '__main__':
    sum_t = 0
    facstr = str(fac(100))
    for num in facstr:
        sum_t += int(num)
    print(sum_t)
