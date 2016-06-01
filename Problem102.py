import math
import numpy as np
from numpy import genfromtxt
import time
# import matplotlib.pyplot as plt
# Done in 70 ms

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p2):
        range_x = self.x - p2.x
        range_y = self.y - p2.y
        return math.sqrt(range_x * range_x + range_y * range_y)


class Triangle(object):
    def __init__(self, x_list, y_list):
        self.p1 = Point(x_list[0], y_list[0])
        self.p2 = Point(x_list[1], y_list[1])
        self.p3 = Point(x_list[2], y_list[2])
        self.denominator = ((self.p2.y - self.p3.y) * (self.p1.x - self.p3.x)
                            + (self.p3.x - self.p2.x) * (self.p1.y - self.p3.y))

    def point_in_triangle(self, point):
        a = ((self.p2.y - self.p3.y) * (point.x - self.p3.x)
             + (self.p3.x - self.p2.x) * (point.y - self.p3.y)) / self.denominator
        b = ((self.p3.y - self.p1.y) * (point.x - self.p3.x)
             + (self.p1.x - self.p3.x) * (point.y - self.p3.y)) / self.denominator
        c = 1 - a - b

        return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1


def get_all_triangles(data):
    # plt.figure()
    # plt.gca().set_aspect('equal')
    return_triangles = []
    for i in range(len(data)):
        x = []
        y = []
        index = 0
        for val in np.nditer(data[i]):
            if index % 2 == 0:
                x.append(int(val))
            else:
                y.append(int(val))
            index += 1
        return_triangles.append(Triangle(x, y))
    # plt.triplot(x, y, c=np.random.rand(3, 1))
    #
    # plt.show()
    return return_triangles


if __name__ == '__main__':

    tic = time.clock()
    my_data = genfromtxt('Problem102.csv', delimiter=',')
    my_data_split = np.split(my_data, len(my_data[:, ]))
    all_triangles = get_all_triangles(my_data_split)
    origin = Point(0, 0)
    summa = 0

    for triangle in all_triangles:
        if triangle.point_in_triangle(origin):
            summa += 1
    print(summa)
    toc = time.clock()
    print((toc - tic) * 1000)

'''

# @staticmethod
# def get_area(tri):
#     p0 = tri.points[0]
#     p1 = tri.points[1]
#     p2 = tri.points[2]
#     return 1/2 * (-p1.y * p2.x + p0.y * (-p1.x + p2.x) + p0.x * (p1.y - p2.y) + p1.x * p2.y)
#
# @staticmethod
# def check_if_clockwise(tri):
#     p0 = tri.points[0]
#     p1 = tri.points[1]
#     p2 = tri.points[2]
#     if (-p1.y * p2.x + p0.y * (-p1.x + p2.x) + p0.x * (p1.y - p2.y) + p1.x * p2.y) > 0:
#         return True
#     return False

#
# class Point(object):
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def distance(self, p2):
#         range_x = self.x - p2.x
#         range_y = self.y - p2.y
#         return math.sqrt(range_x * range_x + range_y * range_y)
#
#     @staticmethod
#     def distance(p1, p2):
#         range_x = p1.x - p2.x
#         range_y = p1.y - p2.y
#         return math.sqrt(range_x * range_x + range_y * range_y)
#
#     def between_two_points(self, p1, p2):
#         between_x = p1.x <= self.x <= p2.x
#         between_y = p1.y <= self.y <= p2.y
#         if between_x and between_y:
#             return True
#         return False
#
#     def between_an_interval(self, x_max, x_min, y_max, y_min):
#         between_x = x_min <= self.x <= x_max
#         between_y = y_min <= self.y <= y_max
#         if between_x and between_y:
#             return True
#         return False
'''
