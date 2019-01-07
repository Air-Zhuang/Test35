'''
为每个元祖命名，提高程序可读性
'''

#使用元组存储
'''优点：存储相同的数据，元组更节省空间 缺点：访问时，需要使用索引，降低程序的可读性'''

#拆包
a,b,c,d =range(4)
print(a)
print(b)
print(c)
print(d)
print()

#使用枚举的方式
s=('Jim',16,'male','jim897@gmail.com')
from enum import IntEnum

class StudentEnum(IntEnum):
    NAME=0
    AGE=1
    SEX=2
    EMAIL=3
print(StudentEnum.NAME) #StudentEnum.NAME是数字，是int子类的一个实例
print(isinstance(StudentEnum.NAME,int))
print(StudentEnum.NAME==0)
print(s[StudentEnum.NAME],s[StudentEnum.AGE],s[StudentEnum.SEX],s[StudentEnum.EMAIL])
print()

#使用namedtuple
from collections import namedtuple

Stuent=namedtuple('StudentTuple',['name','age','sex'])
s1=Stuent('xiaoming',16,'male')
print(isinstance(s1,tuple))
print(s1)
s2=Stuent(name='xiaohong',age=18,sex='female')
print(s2)
print(s2.name)