# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)


def palindromes(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    total_sum = 0
    to = 1000000
    for i in range(to):
        bin = "{0:b}".format(i)
        if palindromes(bin) and palindromes(i):
            total_sum += i

    print(total_sum)
