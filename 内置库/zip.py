print(zip(range(3),'ABC'))
print(list(zip(range(3),'ABC')))
print(list(zip(range(3),'ABC',[0.0,1.1,2.2,3.3])))

'''itertools.zip_longest
    使用可选的fillvalue(默认值为None)填充缺失的值
    因此可以继续产出，直到最长的可迭代对象耗尽'''
from itertools import zip_longest
print(list(zip_longest(range(3),'ABC',[0.0,1.1,2.2,3.3],fillvalue=-1)))
