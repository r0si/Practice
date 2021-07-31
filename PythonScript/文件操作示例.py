#!/usr/bin/env python
# -*- coding: utf-8 -*-

m = []
while True:
    name = input('请输入姓名:')
    score = input('请输入成绩:')
    if name == '-1':
        break
    else:
        m.append(name, score)
with open('math.csv', 'w') as f:
    for item in m:
        f.write(item[0] + ',' + item[1] + '\n')
