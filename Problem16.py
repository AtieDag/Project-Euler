# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?


def sum_of_digits(A):
    sum0 = 0
    for i in str(A):
        sum0 += int(i)
    print(sum0)


if __name__ == "__main__":
    sum_of_digits(2 ** 1000)
