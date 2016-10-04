# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120. {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
import math


def limit(x, y, limit_value):
    if x + y + math.sqrt(x * x + y * y) == limit_value:
        return True
    return False


if __name__ == '__main__':
    p = 1001
    solutions = {}
    for p in range(1, p):
        end = round(p / 2)
        for a in range(1, end):
            for b in range(a, end):
                if limit(a, b, p):
                    if p not in solutions:
                        solutions[p] = 1
                    else:
                        solutions[p] += 1

    print(max(solutions, key=solutions.get))
