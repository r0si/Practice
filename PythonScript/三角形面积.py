#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
a = float(input("请输入三角形的第一条边:"))
b = float(input("请输入三角形的第二条边:"))
c = float(input("请输入三角形的第三条边:"))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("三角形的面积是:%f" % area)
