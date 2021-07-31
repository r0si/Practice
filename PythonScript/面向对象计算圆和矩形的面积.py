#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


class Shape:
    def area(self):
        return 0.0


class Circle(Shape):
    def __init__(self, r=0.0):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def area(self):
        return self.a * self.b


if __name__ == '__main__':
    c = Circle(5)
    print('半径=', c.r, ' 面积=', c.area())
    r = Rectangle(12.5, 5.6)
    print('矩形的边长分别是:', r.a, ',', r.b, ' 面积是:', r.area())
