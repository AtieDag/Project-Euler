# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import numpy as np


class SumOFNumbers:
    def __init__(self):
        self.matrix = []
        self.grid = []


def load_numbers(file_name):
    b = []
    a = np.ones(10, dtype=np.int) - 1
    with open(file_name) as file:
        for index, line in enumerate(file):
            line = line.replace("\n", "")
            print(line)
            for j, number in enumerate(line):
                b.append(int(number))
                if (j + 1) % 10 == 0:
                    a = a + b
                    print(b)
                    print(a)
                    b = []

    return a


if __name__ == '__main__':
    all_su = load_numbers('Problem13.txt')
