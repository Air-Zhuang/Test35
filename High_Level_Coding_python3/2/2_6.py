'''
如何让字典保持有序
python3.6以后dict默认有序
'''

from random import shuffle
from collections import OrderedDict

players=list('ABCDEFGH')
shuffle(players)
d=OrderedDict()     #声明OrderedDict
for i,p in enumerate(players,1):
    d[p]=i          #给OrderedDict赋值

print(d)
for i in d:
    print(i,d[i])

import itertools

'''islice为可迭代对象支持切片操作'''

print(list(itertools.islice(range(10),3,6)))
print()

#因为OrderedDict本身不支持切片操作，所以用islice将其变为可切片操作
def query_by_order(d,a,b=None):
    a-=1
    if b is None:
        b=a+1
    return list(itertools.islice(d,a,b))

print(query_by_order(d,4))
print(query_by_order(d,3,6))



