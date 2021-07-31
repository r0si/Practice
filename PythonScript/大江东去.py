#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {}
with open('大江东去.txt', encoding='utf-8') as src:
    for line in src:
        for c in line:
            d[c] = d.get(c, 0) + 1
del d[' ']
del d['\n']
with open('字数统计.csv', 'w', encoding='utf-8') as dest:
    for key in d:
        dest.write('{},{}\n'.format(key, d[key]))
