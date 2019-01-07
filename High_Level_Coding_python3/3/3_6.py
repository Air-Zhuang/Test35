'''
在一个for语句中迭代多个可迭代对象
'''

from random import randint
from itertools import chain

#并行
chinese=[randint(60,100) for _ in range(10)]
math=[randint(60,100) for _ in range(10)]
english=[randint(60,100) for _ in range(10)]
print(chinese);print(math);print(english)
total=[]
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
print(total)
print([sum(s) for s in zip(chinese,math,english)])
print(list(map(sum,zip(chinese,math,english))))
# print(list(map(lambda a,b,c:a+b+c,chinese,math,english))) #麻烦
print()

#串行:使用itertools.chain()方法：
#连接多个可迭代对象，返回一个可迭代对象
c1=[randint(60,100) for i in range(5)]
c2=[randint(60,100) for i in range(4)]
c3=[randint(60,100) for i in range(3)]
c4=[randint(60,100) for i in range(6)]
print(len([i for i in chain(c1,c2,c3,c4) if i>=90]))
print()

l=[['abc'],[12],["fff"],["567","sdf"]]
print(*l)
print(list(chain(*l)))
d=[{'abc':111},{12:222},{"fff":333},{"567":444},{"567":444}]
print(list(chain(*d)))