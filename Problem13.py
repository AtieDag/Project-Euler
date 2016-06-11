# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import numpy as np


def load_numbers(file_name):
    x_numbers = 50
    index = 0
    b = []
    a = np.ones(x_numbers, dtype=np.int) - 1
    with open(file_name) as file:
        for line in file:
            line = line.replace("\n", "")
            for num in line:
                b.append(int(num))
                if (index + 1) % x_numbers == 0:
                    a = a + b
                    b = []
                index += 1

    return a


if __name__ == '__main__':
    all_numbers = load_numbers('Problem13.txt')
    c = []
    rest = 0
    for i, number in enumerate(reversed(all_numbers)):

        number += rest
        extract = number % 10
        rest = int((number - extract) / 10)
        c.append(extract)
    c.append(rest)

    for number in reversed(c):
        print(number,end="")

