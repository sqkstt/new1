# -*- coding: utf-8 -*-

import math
def quadratic(a, b, c):
    p = -b/(2*a)
    q = b*b-4*a*c
    if q > 0:
        s1 = p+math.sqrt(q)/(2*a)
        s2 = p-math.sqrt(q)/(2*a)
        return s1, s2
    elif q == 0:
        s1 = p
        s2 = p
        return s1, s2
    else :
        return 0
a = int(input('请输入系数a'))
b = int(input('请输入系数b'))
c = int(input('请输入系数c'))
r = quadratic(a,b,c)
print(r)