# Consider the fraction, n/d, where n and d are positive integers.
# If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
# By listing the set of reduced proper fractions for d ≤ 1000000 in ascending order of size, find
# the numerator of the fraction immediately to the left of 3/7.


def HCF(n_, d_):
    if n_ % 2 == 0:
        if d_ % 2 == 0:
            return False
    return True


if __name__ == '__main__':
    value = 1000000
    below = 3 / 7
    max_n = 0
    near = 0
    for d in range(1, value + 1):
        a = int(d * below)
        for n in range(a, a + 1):
            now = (n / d)
            if HCF(n, d) and now < below:
                if now > near:
                    near = now
                    max_n = n

    print("The numerator: " + str(max_n))
