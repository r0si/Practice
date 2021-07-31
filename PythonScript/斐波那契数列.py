#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(100)
