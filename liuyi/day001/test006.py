"""

题目描述

写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
输入描述:
输入一个正浮点数值
输出描述:
输出该数值的近似整数值

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
fNum = float(input('输入一个正浮点数值:'))
yuShu = fNum % 1
ZhShu = fNum / 1
if yuShu >= 0.5:
    fNum = ZhShu + 1
else:
    fNum = ZhShu
print('近似整数值:%d' % fNum)

