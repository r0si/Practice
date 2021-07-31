#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input('请输入一个非负整数:'))
for i in range(2, n):
    if n % i == 0:
        print("%d不是素数" % n)
        break
else:
    print("%d是素数" % n)
