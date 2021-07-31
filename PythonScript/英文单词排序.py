#!/usr/bin/env python
# -*- coding: utf-8 -*-

words=[]
while True:
    str = input('请输入单词,以-1作为结束:')
    if str == '-1':
        break
    else:
        words.append(str)
print('排序前:')
print(words)
words.sort(reverse=False)
print('排序后:')
print(words)
