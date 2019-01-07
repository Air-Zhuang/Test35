from random import randint,sample
from functools import reduce

'''
如何快速找到多个字典中的公共键
'''
#第一种方式：for循环或使用map()
first={k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
second={k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
third={k:randint(1,4) for k in sample('abcdefgh',randint(3,6))}
print("三轮进球数:")
print(first);print(second);print(third)
res=[]
for i in first:
    if i in second and i in third:
        res.append(i)
print("使用for循环找到公共键:",res)

dl=[first,second,third]
print("也可改为用map()方法:",[k for k in dl[0] if all(map(lambda d:k in d,dl[1:]))])

#第二种方式:取键的交集
print("取键的交集:",first.keys() & second.keys() & third.keys())

#第三种方式:reduce()+map()
res2=map(dict.keys,[first,second,third])
print(res2)
print("使用reduce():",reduce(lambda a,b:a & b,res2))


