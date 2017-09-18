"""

题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
最后一个数后面也要有空格

详细描述：

函数接口说明：
public String getResult(long ulDataInput)
输入参数：
long ulDataInput：输入的正整数
返回值：
String


输入描述:
输入一个long型整数
输出描述:
按照从小到大的顺序输出它的所有（质数）   的因子，以空格隔开。最后一个数后面也要有空格。

"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
def fact(ll):
    i = 1
    list = []
    while i * i <= ll:
        if ll % i == 0 and i != 1:
            list.append(i)
        if i * i == ll and i != 1:
            list.append(i)
        i = i + 1
    if len(list) == 0:
        flag = 0    # 质数
    else:
        flag = 1    # 非质数
    return flag


ll1 = input('输入一个long型正整数')
list1 = []
i1 = 1
while i1 * i1 <= int(ll1):
    if int(ll1) % i1 == 0 and i1 != 1:
        if fact(i1) == 1:
            i1 = i1 + 1
        else:
            list1.append(i1)
            i1 = i1 + 1
    else:
        i1 = i1 + 1
print('%s 的质数因子有：%s' % (ll1, sorted(list1)))




