# A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n. The
# following is an example of a hexagonal orchard of order 5: Highlighted in green are the points which are hidden
# from the center by a point closer to it. It can be seen that for a hexagonal orchard of order 5, 30 points are
# hidden from the center.

# Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.
# H(5) = 30. H(10) = 138. H(1 000) = 1177848.
# Find H(100 000 000).
import numpy as np

step = 10
n = step * 2
n_len = n * 2


def check_next(add_x: int, add_y: int, x: int = 0, y: int = 0) -> int:
    x += add_x
    y += add_y
    print(n_len, x * 2 + y)
    if x * 2 + y > n_len:
        return 0
    return check_next(add_x, add_y, x, y) + 1


def count_real_points(n):
    if n == 1:
        return 1
    else:
        return n + count_real_points(n - 1)


x_start = 3
y_start = 1
x_end = int(n / 2)
y_end = int(n / 4)
count = (1 + x_end - x_start) / 2
count = int(count_real_points(count))

x_pos = np.zeros(count)
y_pos = np.zeros(count)
i = 0
for i_y in range(y_start, y_end):
    for i_x in range(x_start, x_end):
        print(i_x, i_y)
        i += 1

    x_start += 1
print(i)
for i in zip(x_pos, y_pos):
    print(i)
# H(5)
# (3, 1) -> 2 -1

#  H(10)
# (7, 6) -> 2 - 1
# (3, 1) -> 5 - 1
# print(check_next(3, 1))
for i in range(10):
    print(2 * i - 2)
