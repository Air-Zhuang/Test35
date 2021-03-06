'''
__new__(cls)   用来初始化类,元类编程!!!!(metaclass.py)
__init__(self) 用来初始化对象
'''

class A:
    def __new__(cls, *args, **kwargs):#一般不在这里用，一般在元类编程中用
        print("__new__")
        # 如果没有返回则不会进入到__init__方法中
        # 在普通的类中使用__new__不能返回*args, **kwargs
        return super().__new__(cls)
    def __init__(self,x):
        print("__init__")
        self.x=x

A(1)
print()

'''内置不可变数据类型'''
class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat,cls).__new__(cls,round(val,2))
class BigInt(int):
    def __new__(cls, val):
        return super(BigInt, cls).__new__(cls,val+1)
class BigStr(str):
    def __new__(cls, val):
        return super(BigStr, cls).__new__(cls,val+"a")
class sortDict(dict):       #见下面：内置可变数据类型
    def key(self):
        return sorted(super(sortDict, self).keys())
class sortList(list):       #见下面：内置可变数据类型
    def key(self):
        return super(sortList, self).__len__()+5
class IntTuple(tuple):
    def __new__(cls, iterable):
        g=(x for x in iterable if isinstance(x,int) and x>0)
        # return super().__new__(cls, g)
        return super().__new__(cls,g)   #两句一样

print(RoundFloat(3.1415926))
print(BigInt(1))
print(BigStr("a"))
print(sortDict(a=1,b=2))
print(len(sortList([4,2,45,23,6])))
print(type(len(sortList([4,2,45,23,6]))))
t=IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)
print()

'''内置可变数据类型'''
'''=================UserDict========================================='''
import collections

class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,[value]*2)

dd=DoppelDict2(one=1)
print(dd)
dd['two']=2
print(dd)
dd.update(three=3)
print(dd)
print()

class AnswerDict2(collections.UserDict):
    def __getitem__(self, key):
        return 42
ad=AnswerDict2(a='foo')
print(ad['a'])
d={}
d.update(ad)
d['a']=43
print(d)