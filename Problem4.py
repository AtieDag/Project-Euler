# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91x99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time


def is_palindromic(number):
    str_number = str(number)
    rev_str_number = str_number[::-1]
    if str_number == rev_str_number:
        return True
    return False


if __name__ == '__main__':
    tic = time.clock()
    max_value = 0
    for i in range(999, 900, -1):
        for j in range(999, 900, -1):
            if is_palindromic(i * j):
                if i * j > max_value:
                    max_value = i * j
    print(max_value)

    toc = time.clock()
    print(toc - tic)
