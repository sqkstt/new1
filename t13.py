# -*- coding: utf-8 -*-
def trim(s):
    t = len(s) - 1
    a = 0
    x = len(s) * ' '
    if x == s:
        return ''    
    while t >= 0:
        if s[t] ==' ':
            t -= 1
            continue
        else:
           s = s[0:t+1]
           break
    while a < t:
        if s[a] ==' ':
            a += 1
            continue
        else:
           s = s[a:]
           break         
    return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')