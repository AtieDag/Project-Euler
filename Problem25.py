# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


def fib():
    a, b = 0, 1
    while True:  # First iteration:
        yield a  # yield 0 to start with and then
        a, b = b, a + b  # a will now be 1, and b will also be 1, (0 + 1)


if __name__ == "__main__":
    for index, fibonacci_number in enumerate(fib()):
        if len(str(fibonacci_number)) == 1000:
            print('Index: {i:3}'.format(i=index))
            break
