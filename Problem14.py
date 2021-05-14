# The following iterative sequence is defined for the set of positive integers:
from functools import lru_cache


@lru_cache(maxsize=100)
def collatz_sequence(n, terms=0):
    terms += 1
    if n == 1:
        return terms
    # n is even
    if n % 2 == 0:
        return collatz_sequence(n / 2, terms)
    # n is odd
    return collatz_sequence(3 * n + 1, terms)


if __name__ == '__main__':
    memo = {1: 1}
    steps = 1000000
    for number in range(1, steps):
        count = collatz_sequence(number)
        memo[number] = count
    print(max(memo, key=memo.get))
