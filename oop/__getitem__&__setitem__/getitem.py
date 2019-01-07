import collections
import random

'''实现dict(类)'''
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


'''实现__getitem__()可对类取下标，切片'''
Card=collections.namedtuple('Card',['rank','suit'])

class FrenchDeck(object):
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
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

class Fib3(object):
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

class DictDemo:
    def __init__(self,key,value):
        self.dict = {}
        self.dict[key] = value
    def __getitem__(self,key):
        return self.dict[key]
    def __setitem__(self,key,value):
        self.dict[key] = value
    def __len__(self):
        return len(self.dict)
dictDemo = DictDemo('key0','value0')
print(dictDemo['key0']) #value0
dictDemo['key1'] = 'value1'
print(dictDemo['key1']) #value1
print(len(dictDemo)) #2


