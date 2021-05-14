# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Done in 153 ms...
import math

a = 1
total = 0

while a < 1000:
    j = 1
    while total < 1000:
        c = a * a + pow(a + j, 2)
        total = a + (a + j) + math.sqrt(c)
        if total == 1000:
            print("Total ", total)
            print("a: ", a, " b: ", (a + j), " c:", math.sqrt(c))
            print("Product of abc: ", a*(a + j)*math.sqrt(c))
            break
        j += 1
    total = 0
    a += 1

