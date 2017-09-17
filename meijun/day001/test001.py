"""

题目描述:

计算字符串最后一个单词的长度，单词以空格隔开。

输入描述:
一行字符串，非空，长度小于5000。
输出描述:
整数N，最后一个单词的长度。

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

str = "hello world, nice too meet you"



st = str.split(' ')

s = st[len(st)-1]

print(len(s))
print(len(s))
print(len(s))