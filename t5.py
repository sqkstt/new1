# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bmi =   weight//(height**2)
if bmi<18.5:
    printf('过轻',bmi)
elif bmi>=18.5 and bmi<25:
    print('正常',bmi)
elif bmi<=28 and bmi>=25:
    print('过重',bmi)
elif bmi>28 and bmi<=32:
    print('肥胖',bmi)
else :
    print('严重肥胖',bmi)