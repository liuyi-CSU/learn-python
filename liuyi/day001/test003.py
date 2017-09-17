"""

明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），
对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，
按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作。


Input Param
     n               输入随机数的个数
 inputArray      n个随机整数组成的数组

Return Value
     OutputArray    输出处理后的随机整数

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
shuZu=[]
for i in range(random.randrange(10)):
    randNum=random.randrange(1, 20)
    if randNum not in shuZu:
        shuZu.append(randNum)
print(shuZu)

