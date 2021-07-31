#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = ["Source Han Serif CN"]
x = np.random.rand(10) * 20
plt.subplot(221)
plt.plot(x, "r--")

plt.subplot(222)
x = np.arange(-3, 3, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, "m:", label="sin")
plt.plot(x, y2, "c--", label="cos")
plt.legend()

plt.subplot(223)
plt.plot([100, 104, 106, 95, 103, 105, 115, 100])
plt.xlabel("季度")
plt.ylabel("销售额（万元）")
plt.xticks(
    np.arange(0, 8),
    [
        "2018年一季度",
        "2018年二季度",
        "2018年三季度",
        "2018年四季度",
        "2019年一季度",
        "2019年二季度",
        "2019年三季度",
        "2019年四季度",
    ],
    rotation=45,
)

plt.subplot((224))
x = np.arange(0, 1.2, 0.1)
y1 = x ** 2
y2 = x ** 3
plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x^3")
plt.legend()
plt.show()
'''
x = np.random.rand(10) * 20
plt.subplot(221)
plt.plot(x, "r--")
plt.subplot(222)
x = np.arange(-3,3,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, "m:", label="sin")
plt.plot(x, y2, "c--", label="cos")
plt.legend()

plt.subplot(223)
plt.plot([100, 104, 106, 95, 103, 105, 115, 100])
plt.xlabel("季度")
plt.ylabel("销售额（万元）")
plt.xticks(
    np.arange(0, 8),
    [
        "2018年一季度",
        "2018年二季度",
        "2018年三季度",
        "2018年四季度",
        "2019年一季度",
        "2019年二季度",
        "2019年三季度",
        "2019年四季度",
    ],
    rotation=45,
)
plt.subplot(224)
x = np.arange(0,1.2,0.1)
y1 = x ** 2
y2 = x ** 3
plt.plot(x, y1, label="x^2")
plt.plot(x, y2, label="x^3")
plt.legend()
plt.show()
'''
