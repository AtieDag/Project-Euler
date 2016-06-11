import timeit


def start():
    return collatz_sequence(13)


def start2(n=13):
    if not n in memo:
        memo[n] = collatz_sequence(n)
    return memo[n]


def collatz_sequence(n, terms=0):
    terms += 1
    if n == 1:
        return terms
    # n is even
    if n % 2 == 0:
        return collatz_sequence(n / 2, terms)
    # n is odd
    return collatz_sequence(3 * n + 1, terms)


memo = {1: 1}


def collatz_sequence2(n, terms=0):
    if not n in memo:
        terms += 1
        if n == 1:
            return terms
        # n is even
        if n % 2 == 0:
            return collatz_sequence(n / 2, terms)
        # n is odd
        return collatz_sequence(3 * n + 1, terms)
    return memo[n] + terms


timer1 = timeit.timeit(start, number=10000)
print(timer1)
timer2 = timeit.timeit(start2, number=10000)
print(timer2)
print(memo)
