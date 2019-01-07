'''
对迭代器做切片操作
'''

'''可切片是因为实现了__getitem__方法'''

import os
from itertools import islice
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#传统方法，耗内存
f=open(path+"\\test\\test.txt")
lines=f.readlines()
print(lines)
print(lines[2:5])
print()

#使用迭代器:itertools.islice()
# f.seek(0)#使文件指针回到头部
# for i in f:
#     print(i)

f.seek(0)
for i in islice(f,2,4):
    print(i)
'''------------------------------------------'''
'''islice的内部实现原理'''
def my_islice(iterable,start,end,step=1):
    tmp=0
    for i,x in enumerate(iterable):
        if i>=end:
            break
        if i>=start:
            if tmp==0:
                tmp=step
                yield x
            tmp-=1
'''------------------------------------------'''
l=range(10)
print(l)
t=iter(l)
for i in islice(range(10),2,5):
    print(i)
print()
