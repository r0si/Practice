#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {"数学": 101, "语文": 202, "英语": 203, "物理": 204, "生物": 206}
d['化学'] = 205
d['数学'] = 201
del d['生物']
for key in d:
    print('{}:{}'.format(d[key], key))
