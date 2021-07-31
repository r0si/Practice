#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)
y1 = np.sin(x)
y2 = np.sin(x + 5)
plt.subplot(121)
plt.plot(x, y1, 'b-')
plt.legend(['First s'])
plt.subplot(122)
plt.plot(x, y2, 'g^')
plt.legend(["Second s"])
plt.show()
