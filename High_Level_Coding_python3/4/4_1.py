'''
如何拆分含有多种分隔符的字符串
'''

import re

s='ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
print(s)
print()

#传统方法split
res=s.split(';')
print(res)
print([ss.split('|') for ss in res])
print(list(map(lambda x:x.split('|'),res)))

t=[]
list(map(t.extend,[ss.split('|') for ss in res]))
print(t)
print()

#使用sum：sum中第二个函数为初始值，传入[]则可实现列表相加
print(sum([ss.split('|') for ss in res],[]))
print()

#传统方法split使用循环
def my_split(s,seps):
    res=[s]
    for sep in seps:
        t=[]
        list(map(lambda ss:t.extend(ss.split(sep)),res))
        res=t
    return res
print(my_split(s,';|,\t'))
print()

#使用reduce
from functools import reduce
r=reduce(lambda l,sep:sum(map(lambda ss:ss.split(sep),l),[]),',;|\t',[s])   #reduce第三个参数为初始值
print(r)
my_split2=lambda s,seqs:reduce(lambda l,sep:sum(map(lambda ss:ss.split(sep),l),[]),',;|\t',[s])
print(my_split2(s,',;|\t'))
print()

#使用re.split()
print(re.split(r'[;|,\t]+',s))
print(re.split('[;|,\t]+',s))















