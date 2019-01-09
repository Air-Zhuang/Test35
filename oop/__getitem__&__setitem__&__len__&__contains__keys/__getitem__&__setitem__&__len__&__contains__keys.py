import collections
import random

'''============================用于list======================================================================================='''
'''实现__getitem__()可对类取下标，切片'''
Card=collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)         #有__getitem__可不写__len__
    def __getitem__(self, position):
        return self._cards[position]
    def __setitem__(self, key, value):  #因为实现了__setitem__,所以才可以使用 random.shuffle(f)
        self._cards[key]=value

f=FrenchDeck()
print(len(f))           #__len__
print(f[1],f[-1])       #__getitem__&__setitem__
print(f[3:8:2])         #__getitem__&__setitem__
print()

f=FrenchDeck()
print(f[1:5])
random.shuffle(f)   #因为实现了__setitem__,所以才可以使用 random.shuffle(f)
print(f[1:5])
print()

'''实现了__getitem__的类可以切片，但是生成的为list。如果要生成类的切片对象，需要如下操作：'''
import numbers
class A:
    def __init__(self,a_list):
        self.a_list=a_list
    def __getitem__(self, item):#将A变成可切片的对象，生成的切片对象不是list数据类型而是A的对象类型
        cls=type(self)          #type(self)也可以写成A
        if isinstance(item,slice):
            return cls(a_list=self.a_list[item])
        elif isinstance(item,numbers.Integral):
            return cls(a_list=[self.a_list[item]])
    def __contains__(self, item):#有__getitem__可不写__contains__
        if item in self.a_list:
            print("yes")
            return True
        else:
            print("no")
            return False
a=A([1,2,3,4,5,6,7,8])
a_1=a[2:4]      #可切片的A对象
a_2=a[5]        #可切片的A对象
print(3 in a)   #__contains__
print()

'''__getitem__实现斐波那契数列'''
class Fib3:
    def __getitem__(self, item):
        a,b=1,1
        for i in range(item):
            a,b=b,a+b
        return a
f=Fib3()
for i in range(30):
    print(f[i],end=" ")
print()
print()

'''============================用于dict======================================================================================='''
class DictDemo:
    def __init__(self,key,value):
        self.dict = {}
        self.dict[key] = value
    def __getitem__(self,key):
        return self.dict[key]
    def __setitem__(self,key,value):
        self.dict[key] = value
    def __len__(self):
        return len(self.dict)       #有__getitem__可不写__len__
dictDemo = DictDemo('key0','value0')
print(dictDemo['key0']) #value0
dictDemo['key1'] = 'value1'
print(dictDemo['key1']) #value1
print(len(dictDemo)) #2

'''============================dict实现原理======================================================================================='''
'''dict实现原理--->restfulAPI'''
class QiYue:
    name='qiyue'
    age=18
    def __init__(self):
        self.gender='male'
    def keys(self):                     #dict一个类的时候会调用类的keys方法
        return ['name','age','gender']
    def __getitem__(self, item):
        return getattr(self,item)

o=QiYue()
print(dict(o))
print()
