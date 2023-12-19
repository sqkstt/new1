# -*- coding: utf-8 -*-
name = str(input('请输入您的名字：'))
s1 = int(input('请输入您上次成绩:'))
s2 = int(input('请输入您这次成绩:'))
r = (s2-s1)/s1
if s2>s1:
    print('您的成绩上升了：%.1f %%' % r)
    print('您的成绩上升了：{0:.1f} %%'.format(r))
    print(f'您的成绩上升l:{r} %%')
elif s2<s1:
    print('您的成绩下降了：%.1f %%' % -r)
    print('您的成绩下降了：{0:.1f} %'.format(-r))
    print(f'您的成绩下降l:{-r:.1f} %')
else:
    print('再接再厉')        