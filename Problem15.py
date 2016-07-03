# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down.
# There are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
import math


# binomial coefficient
def binc(n, k):
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n - k)
    return a / (b * c)


if __name__ == '__main__':
    gridX = 20
    gridY = 20
    print(binc(gridX + gridY, gridX))
    # Drawing it as a Pascal's triangle
