#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(int('0xf',16)) #十六进制 转 十进制
print(int('1010',2))  #二进制 转 十进制
print(int('17',8))  #八进制 转 十进制

print(hex(1033))  #十进制 转 十六进制
print(hex(int('101010',2)))  #二进制 转 十六进制
print(hex(int('17',8)))  #八进制 转 十六进制

print(bin(10))  #十进制 转 二进制
print(bin(int('0xff',16))) #十六进制 转 二进制
print(bin(int('17',8)))   #八进制 转 二进制

print(oct(0b1010)) # 二进制 转 八进制
print(oct(11))   #十进制 转 八进制
print(oct(0xf))  #十六进制 转 八进制



